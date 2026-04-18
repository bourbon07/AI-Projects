from ultralytics import YOLO
import cv2
import gradio as gr

# Load the YOLO model
model = YOLO("weights location")

def process_image(image):
    """
    Process a single image, detect objects, and label them.
    Args:
        image: Image array.
    Returns:
        Processed image with detections.
    """
    # Save the uploaded image temporarily
    temp_path = "temp_image.jpg"
    cv2.imwrite(temp_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # Perform detection
    results = model(temp_path)[0]
    boxes = results.boxes
    labels = results.names  # Labels from the model
    confidences = [float(box.conf[0]) for box in boxes]
    xyxy_boxes = [list(map(int, box.xyxy[0])) for box in boxes]
    class_ids = [int(box.cls[0]) for box in boxes]  # Get class IDs for each detection

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

    # Draw boxes and add labels
    for i in indices.flatten() if len(indices) > 0 else []:
        x1, y1, x2, y2 = xyxy_boxes[i]
        label = labels[class_ids[i]] if class_ids[i] < len(labels) else "Unknown"
        confidence = confidences[i]
        label_text = f"{label} ({confidence:.2f})"
        
        # Draw rectangle and label
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert back to RGB for Gradio

# Define Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy", label="Upload Image", image_mode="RGB"),  # Single image input
    outputs=gr.Image(type="numpy", label="Detection Result"),
    title="Tree Detection ",
    description="Upload an image to detect trees and label them as straight or slanted."
)

# Launch the Gradio interface
iface.launch()
