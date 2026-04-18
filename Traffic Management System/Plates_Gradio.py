import os
import cv2
from ultralytics import YOLO
import gradio as gr

# Load the models
plate_model = YOLO("weights location")  # Model for plate detection
number_model = YOLO("weights location")  # Model for number detection
jordan_model = YOLO("weights location")  # Model for Jordan detection

def process_image(image):
    """
    Process an uploaded image to detect plates, check for "Jordan," 
    and extract numbers, including support for multi-row plates.
    """
    # Save the uploaded image temporarily
    temp_input_path = "temp_input.jpg"
    cv2.imwrite(temp_input_path, cv2.cvtColor(image, cv2.COLOR_RGB2BGR))

    # Step 1: Plate detection
    plate_results = plate_model(temp_input_path)
    if not plate_results[0].boxes:
        return "No plate detected.", None

    # Save detected plate image
    plate_result_dir = "plate_result"
    os.makedirs(plate_result_dir, exist_ok=True)
    plate_results[0].save(filename=os.path.join(plate_result_dir, "detected_plate.jpg"))

    # Step 2: Crop the detected plate
    for box in plate_results[0].boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
        cropped_plate = plate_results[0].orig_img[y1:y2, x1:x2]
        cropped_plate_path = os.path.join(plate_result_dir, "cropped_plate.jpg")
        cv2.imwrite(cropped_plate_path, cropped_plate)

        # Step 3: Check if "Jordan" is detected
        jordan_results = jordan_model(cropped_plate_path)
        if not jordan_results[0].boxes:
            return "Unknown plate: No 'Jordan' detected.", None

        # Step 4: Number detection
        number_results = number_model(cropped_plate_path)
        if not number_results[0].boxes:
            return "No numbers detected on the plate.", None

        # Analyze detected numbers for multi-row detection
        boxes_info = []
        for box in number_results[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            y_center = (y1 + y2) // 2
            label = int(box.cls[0])  # Get class ID
            class_name = number_results[0].names[label]
            boxes_info.append((x1, y_center, class_name))

        # Sort by y-center and identify rows
        boxes_info.sort(key=lambda x: x[1])
        gap_threshold = 40  # Adjust based on image resolution
        split_index = None
        for j in range(len(boxes_info) - 1):
            if abs(boxes_info[j + 1][1] - boxes_info[j][1]) > gap_threshold:
                split_index = j
                break

        # Prepare result text
        if split_index is not None:
            upper_row_numbers = boxes_info[:split_index + 1]
            lower_row_numbers = boxes_info[split_index + 1:]

            upper_numbers = ' '.join(number for _, _, number in sorted(upper_row_numbers, key=lambda x: x[0]))
            lower_numbers = ' '.join(number for _, _, number in sorted(lower_row_numbers, key=lambda x: x[0]))
            result_text = f"Upper Row: {upper_numbers}\nLower Row: {lower_numbers}"
        else:
            single_row_numbers = ' '.join(number for _, _, number in sorted(boxes_info, key=lambda x: x[0]))
            result_text = f"Single Row: {single_row_numbers}"

        return result_text, cropped_plate_path

# Define Gradio interface
iface = gr.Interface(
    fn=process_image,
    inputs=gr.Image(type="numpy"),  # Accept uploaded image
    outputs=[
        "text",         # Text output for detected numbers
        gr.Image(type="filepath")  # Display cropped plate image (optional)-
    ],
    title="Car Plate Detection ",
    description="Upload a car image to detect plates and numbers, including multi-row plates."
)

# Launch the interface
iface.launch(share=True)
