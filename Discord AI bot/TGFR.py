import os
import io
import asyncio
from concurrent.futures import ThreadPoolExecutor

import nest_asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv
from google import genai
import fitz  # PyMuPDF
import pytesseract
from PIL import Image

# === SETUP ===
nest_asyncio.apply()
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
TESSERACT_PATH = os.getenv("TESSERACT_PATH")  # e.g. Windows: C:\Program Files\Tesseract-OCR\tesseract.exe

if not DISCORD_TOKEN:
    raise ValueError("DISCORD_TOKEN is missing in .env")

if TESSERACT_PATH:
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

MODEL_NAME = "gemini-2.0-flash"
executor = ThreadPoolExecutor(max_workers=4)

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

client_gemini = genai.Client(api_key=GOOGLE_API_KEY) if GOOGLE_API_KEY else None

chat_history = {}  # user_id -> [str]
last_uploaded_file = {}  # channel_id -> (filename, bytes)

# === Gemini text generation ===
def genai_generate(prompt: str) -> str:
    if not client_gemini:
        return "(Gemini API key not set, skipping AI response)"
    response = client_gemini.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return getattr(response, "text", "(no text returned)")

async def generate_text_async(prompt: str) -> str:
    loop = asyncio.get_running_loop()
    return await loop.run_in_executor(executor, genai_generate, prompt)

# === File text extraction from bytes ===
async def extract_text_from_file(file_info):
    filename, file_bytes = file_info
    ext = os.path.splitext(filename)[1].lower()
    file_stream = io.BytesIO(file_bytes)

    if ext == ".pdf":
        text = ""
        pdf = fitz.open(stream=file_stream.read(), filetype="pdf")
        for page in pdf:
            text += page.get_text()
        return text if text.strip() else "No text found in PDF."

    elif ext in [".png", ".jpg", ".jpeg"]:
        image = Image.open(file_stream)
        text = pytesseract.image_to_string(image)
        return text if text.strip() else "No text found in image."

    elif ext in [".txt", ".md"]:
        try:
            text = file_stream.read().decode("utf-8")
            return text
        except Exception:
            return "Error decoding text file."

    else:
        return "Unsupported file type."

# === Bot events ===
@bot.event
async def on_ready():
    print(f"🤖 Logged in as {bot.user} (ID: {bot.user.id})")
    print("Commands available: !ask <prompt>, !read after uploading a file")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.attachments:
        attachment = message.attachments[0]
        file_bytes = await attachment.read()
        last_uploaded_file[message.channel.id] = (attachment.filename, file_bytes)
        await message.channel.send(f"📂 File `{attachment.filename}` received! Type `!read` to process it.")

    await bot.process_commands(message)

# === Commands ===
@bot.command(name="ask")
async def ask_command(ctx, *, prompt: str):
    if not prompt:
        await ctx.send("Please provide a prompt after `!ask`")
        return

    user_id = ctx.author.id
    history = chat_history.get(user_id, [])

    async with ctx.typing():
        try:
            history.append(f"User: {prompt}")

            if len(history) > 6:
                history = history[-6:]

            combined_prompt = "\n".join(history) + "\nAI:"
            reply = await generate_text_async(combined_prompt)

            history.append(f"AI: {reply}")
            chat_history[user_id] = history

        except Exception as e:
            reply = f"Error: {e}"
            chat_history[user_id] = []

    await ctx.send(reply[:1900])

@bot.command(name="read")
async def read_file(ctx):
    file_info = last_uploaded_file.get(ctx.channel.id)
    if not file_info:
        await ctx.send("❌ No file uploaded yet. Please upload a file first.")
        return

    async with ctx.typing():
        text = await extract_text_from_file(file_info)

    if len(text) > 1900:
        with open("output.txt", "w", encoding="utf-8") as f:
            f.write(text)
        await ctx.send("📄 Text too long. Sending as file:", file=discord.File("output.txt"))
    else:
        await ctx.send(f"📜 Extracted text:\n{text}")

@bot.command(name="ping")
async def ping(ctx):
    await ctx.send("Pong!")

# === Run bot ===
if __name__ == "__main__":
    asyncio.run(bot.start(DISCORD_TOKEN))
