from ultralytics import YOLO
import cv2
import gradio as gr

# Load the YOLO model
model = YOLO("weights location")

def process_image(image):
    """
    Process a single image, detect objects, and label them.
    Args:
        image: Image array in RGB format.
    Returns:
        Processed image in RGB format.
    """
    # Convert image from RGB to BGR for OpenCV processing
    image_bgr = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Save the uploaded image temporarily
    temp_path = "temp_image.jpg"
    cv2.imwrite(temp_path, image_bgr)

    # Perform detection
    results = model(temp_path)[0]
    boxes = results.boxes
    confidences = [float(box.conf[0]) for box in boxes]
    xyxy_boxes = [list(map(int, box.xyxy[0])) for box in boxes]
    class_ids = [int(box.cls[0]) for box in boxes]  # Class IDs for each detection
    labels = results.names  # Labels from the model

    # Draw boxes and labels
    for i, (x1, y1, x2, y2) in enumerate(xyxy_boxes):
        label = labels[class_ids[i]] if class_ids[i] < len(labels) else "Unknown"
        confidence = confidences[i]
        label_text = f"{label} ({confidence:.2f})"
        
        cv2.rectangle(image_bgr, (x1, y1), (x2, y2), (0, 255, 0), 3)
        cv2.putText(image_bgr, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    # Convert back to RGB for Gradio output
    image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
    return image_rgb

# Define Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy", label="Upload Image", image_mode="RGB"),  # Single image input
    outputs=gr.Image(type="numpy", label="Detection Result"),
    title="Signs Detection",
    description="Upload an image to detect objects and label them with YOLO."
)

# Launch the Gradio interface
iface.launch(share=True)
