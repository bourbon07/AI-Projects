from ultralytics import YOLO
import cv2
import gradio as gr
import torch
print("CUDA available:", torch.cuda.is_available())
# Load the YOLO model
model = YOLO("/weights location")

def process_multiple_images(image1, image2, image3, image4):
    """
    Process multiple images, detect cars, count them, and provide the final decision.
    Args:
        image1, image2, image3, image4: Image arrays in RGB format.
    Returns:
        Processed images and final decision based on the highest car count.
    """
    images = [image1, image2, image3, image4]
    results_images = []
    car_counts = []

    for image in images:
        if image is None:
            results_images.append(None)
            car_counts.append(0)
            continue

        # Save the uploaded image temporarily
        temp_path = "temp_image.jpg"
        cv2.imwrite(temp_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

        # Perform detection
        results = model(temp_path)[0]
        boxes = results.boxes
        confidences = [float(box.conf[0]) for box in boxes]
        xyxy_boxes = [list(map(int, box.xyxy[0])) for box in boxes]

        # Non-Maximum Suppression (NMS)
        if len(xyxy_boxes) > 0:
            indices = cv2.dnn.NMSBoxes(
                bboxes=xyxy_boxes,
                scores=confidences,
                score_threshold=0.2,
                nms_threshold=0.8
            )
        else:
            indices = []

        # Draw boxes and count cars
        car_count = 0
        for i in indices.flatten() if len(indices) > 0 else []:
            x1, y1, x2, y2 = xyxy_boxes[i]
            car_count += 1
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            label = "Car"
            cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # Add count text on the image
        text = f"Count: {car_count}"
        font = cv2.FONT_HERSHEY_SIMPLEX
        font_scale = 1
        color = (125, 0, 0)
        thickness = 2
        text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
        text_x = (image.shape[1] - text_size[0]) // 2  # Center the text horizontally
        text_y = 30  # Place the text near the top of the image

        # Create a background rectangle for the text
        cv2.rectangle(image, (text_x - 10, text_y - 30), (text_x + text_size[0] + 10, text_y + 10), (255, 255, 255), -1)
        cv2.putText(image, text, (text_x, text_y), font, font_scale, color, thickness)

        results_images.append(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))  # Convert back to RGB for Gradio
        car_counts.append(car_count)

    # Determine which image has the most cars
    max_count = max(car_counts)
    max_index = car_counts.index(max_count) + 1  # Indices are 1-based for the output
    final_decision = f"Traffic Light {max_index} +10 seconds"

    return results_images + [final_decision]

# Define Gradio interface
iface = gr.Interface(
    fn=process_multiple_images,
    inputs=[
        gr.Image(type="numpy", label="Upload Image 1", image_mode="RGB"),
        gr.Image(type="numpy", label="Upload Image 2", image_mode="RGB"),
        gr.Image(type="numpy", label="Upload Image 3", image_mode="RGB"),
        gr.Image(type="numpy", label="Upload Image 4", image_mode="RGB")
    ],
    outputs=[
        gr.Image(type="numpy", label="Detection Result 1"),
        gr.Image(type="numpy", label="Detection Result 2"),
        gr.Image(type="numpy", label="Detection Result 3"),
        gr.Image(type="numpy", label="Detection Result 4"),
        gr.Textbox(label="Final Decision")  # Output final decision text
    ],
    title="Car Detection and Counting",
    description="Upload up to 4 images to detect cars, count them, and get the final decision."
)

# Launch the Gradio interface
iface.launch(share=True)
