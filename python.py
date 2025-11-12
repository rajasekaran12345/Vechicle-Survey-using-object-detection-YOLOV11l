import cv2
from ultralytics import YOLO
from collections import defaultdict

# Load the YOLO model
model = YOLO('yolo11l.pt')
class_list = model.names
# Open the video file
cap = cv2.VideoCapture('video3840x2160.mp4')

line_y_red = 1200  # Red line position

# Dictionary to store object counts byVsurvey class
class_counts_IN = defaultdict(int)
class_counts_OUT = defaultdict(int)

# Dictionary to keep track of object IDs that have crossed the line
crossed_ids_IN = set()
crossed_ids_OUT = set()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO tracking on the frame
    results = model.track(frame, persist=True, classes = [1,2,3,5,6,7]) 
    #print(results)

    # Ensure results are not empty
    if results[0].boxes.data is not None:
        # Get the detected boxes, their class indices, and track IDs
        boxes = results[0].boxes.xyxy.cpu()
        track_ids = results[0].boxes.id.int().cpu().tolist()
        class_indices = results[0].boxes.cls.int().cpu().tolist()
        confidences = results[0].boxes.conf.cpu()

        cv2.line(frame, (690, line_y_red), (1700, line_y_red), (0, 0, 255), 3)
        cv2.putText(frame, 'Vechicle_incoming', (690, line_y_red - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 0,0), 3, cv2.LINE_AA)

        cv2.line(frame, (2100, line_y_red), (3200, line_y_red), (0, 0, 255), 3)
        cv2.putText(frame, 'Vechicle_Outgoing', (2100, line_y_red - 10), cv2.FONT_HERSHEY_SIMPLEX, 1.7, (0, 0,0), 3, cv2.LINE_AA)



        

        # Loop through each detected object
        for box, track_id, class_idx, conf in zip(boxes, track_ids, class_indices, confidences):
            x1, y1, x2, y2 = map(int, box)
            cx = (x1 + x2) // 2  # Calculate the center point
            cy = (y1 + y2) // 2            

            class_name = class_list[class_idx]

            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)
            
            cv2.putText(frame, f"ID: {track_id} {class_name}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255), 3)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 4) 


            # Check if the object has crossed the red line
            if cy > line_y_red and track_id not in crossed_ids_IN:
                # Mark the object as crossed
                crossed_ids_IN.add(track_id)
                class_counts_IN[class_name] += 1
            elif cy < line_y_red and track_id not in crossed_ids_OUT:
                # Mark the object as crossed
                crossed_ids_OUT.add(track_id)
                class_counts_OUT[class_name] += 1
            


        # Display the counts on the frame
        y_offset_IN = 60
        for class_name, count_IN in class_counts_IN.items():
            cv2.putText(frame, f"{class_name}_IN : {count_IN}", (50, y_offset_IN),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
            y_offset_IN += 50

        y_offset_OUT = 60
        for class_name, count_OUT in class_counts_OUT.items():
            cv2.putText(frame, f"{class_name}_OUT : {count_OUT}", (2100, y_offset_OUT),
                        cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 3)
            y_offset_OUT += 50

    
    
    cv2.namedWindow("vehicle counting", cv2.WINDOW_NORMAL)
    cv2.imshow("vehicle counting", frame)
    cv2.resizeWindow("vehicle counting", 1280, 720)  
    
    # Exit loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
