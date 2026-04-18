import os
import cv2
import time
import torch
from ultralytics import YOLO


plate_model = YOLO("/weights location") 
number_model = YOLO("weights location")


DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'


cap = cv2.VideoCapture(0) 


if not cap.isOpened():
    print("Error: Could not open video stream.")
    exit()

# Ensure the "Plates" folder exists
save_dir = "Plates"
os.makedirs(save_dir, exist_ok=True)

# Timer for saving numbers
last_save_time = 0
save_interval = 10  


def process_frame(frame):
    global last_save_time
    start_time = time.time()

    # Preprocess frame (on CPU)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Perform plate detection (on GPU)
    plate_results = plate_model.predict(rgb_frame, device=DEVICE)

    for plate_result in plate_results:
        if plate_result.boxes:
            for box in plate_result.boxes:

                x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
                plate_image = rgb_frame[y1:y2, x1:x2]  # Crop the image to the bounding box
                

                number_results = number_model.predict(plate_image, device=DEVICE)

\
                if number_results[0].boxes:
                    boxes_info = []
                    for num_box in number_results[0].boxes:
                        nx1, ny1, nx2, ny2 = map(int, num_box.xyxy[0].tolist())
                        label = int(num_box.cls[0])
                        class_name = number_results[0].names[label]
                        boxes_info.append((nx1, class_name))

                        # Draw bounding box around the number
                        cv2.rectangle(plate_image, (nx1, ny1), (nx2, ny2), (0, 255, 0), 2)
                        cv2.putText(plate_image, class_name, (nx1, ny1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

                    # Sort and print the detected numbers
                    boxes_info.sort(key=lambda x: x[0])
                    detected_number = ''.join(class_name for _, class_name in boxes_info)
                    print(f"Detected Number: {detected_number}")

                    # Draw the plate bounding box on the original frame
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
                    cv2.putText(frame, detected_number, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

                    # Save the number every 10 seconds
                    current_time = time.time()
                    if current_time - last_save_time >= save_interval:
                        timestamp = time.strftime("%Y%m%d_%H%M%S")
                        save_path = os.path.join(save_dir, f"{detected_number}_{timestamp}.jpg")
                        cv2.imwrite(save_path, plate_image[:, :, ::-1])  # Convert back to BGR for saving
                        print(f"Saved: {save_path}")
                        last_save_time = current_time


    end_time = time.time()
    processing_time = end_time - start_time
    cv2.putText(frame, f"FPS: {1 / processing_time:.2f}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    return frame


while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame.")
        break

    # Process the captured frame
    processed_frame = process_frame(frame)

    # Display the processed frame
    cv2.imshow("Real-Time Plate Detection", processed_frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
