from ultralytics import YOLO
import cv2
import argparse
import numpy as np

def main(args):
    model = YOLO(args.model)
    class_names = model.names
    colorList = np.random.uniform(low=0,high=255,size=(len(class_names),3))
    # Open the video file
    cap = cv2.VideoCapture(args.source)
    
    # Check if the video file was opened successfully
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return
    
    # Get video properties
    if args.save_result:
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        # Define the codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Use appropriate codec (e.g., 'XVID', 'MJPG', 'H264', etc.)
        out = cv2.VideoWriter(args.save_dir, fourcc, fps, (width, height))

    while True:

        # Read a frame from the video
        ret, frame = cap.read()
        
        # Break the loop if we have reached the end of the video
        if not ret:
            break
        results = model.track(frame,persist=True)[0]
        boxes = results.cpu().numpy().boxes.data
        for output in boxes:
            bbox_tl_x = int(output[0])
            bbox_tl_y = int(output[1])
            bbox_br_x = int(output[2])
            bbox_br_y = int(output[3])
  
            id = int(output[4])
            class_ = int(output[6])
            score = int(output[5])
            classColor = [int(c) for c in colorList[class_]]


            cv2.rectangle(frame, (bbox_tl_x, bbox_tl_y),(bbox_br_x, bbox_br_y), color=classColor, thickness=2) #Draw detection rectangle
            cv2.putText(frame, f"{class_names[class_].capitalize()}- {id}", (bbox_tl_x, bbox_tl_y), cv2.FONT_HERSHEY_COMPLEX, 1, color=classColor, thickness=1) #Draw detection value

        if args.show:
            cv2.imshow("",frame)
            cv2.waitKey(1)
        if args.save_result:
            out.write(frame)
    if args.save_result:
        # Release the video capture and writer objects
        cap.release()
        out.release()    




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Argument parser for run.py")
    parser.add_argument("--model", type=str, default="yolov8s.pt", help="Path to the model")
    parser.add_argument("--source", type=str, default="test.mp4", help="Path to the source video")
    parser.add_argument("--show", type=bool, default=True, help="Show the output")
    parser.add_argument("--save_result", type=bool, default=True, help="Save result to file")
    parser.add_argument("--save_dir", type=str, default="output.pm4", help="Path to the source video")

    args = parser.parse_args()



    main(args)
