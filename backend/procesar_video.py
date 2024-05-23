import cv2
from ultralytics import YOLO
from threading import Thread
import os
import json
import datetime

def thread_safe_predict(video_path, save_folder):
    # Carga el modelo YOLO
    local_model = YOLO('C:\\Users\\Usuario\\Desktop\\MovieRec\\MovieRecognition\\backend\\best.pt')

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_number = 0

    # Get video filename without extension
    video_name = os.path.splitext(os.path.basename(video_path))[0].split("-")[-1]
    file_name = video_name.split("_")[0]
    date = datetime.datetime.now().strftime('%Y-%m-%d')

    # Create directory to save detections for this video
    detection_dir = os.path.join(save_folder, f"{file_name}_{date}_{video_name}")
    os.makedirs(detection_dir, exist_ok=True)

    # Dictionary with info:
    analysis_info = {}

    # Loop through the video frames
    while cap.isOpened():
        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Increment frame number
            frame_number += 1

            results = local_model.predict(source=frame, stream=False, save=False, imgsz=640, conf=0.75, half=False,
                                          device="cpu", verbose=False)

            names = results[0].names
            box = results[0].boxes.cpu()
            conf = box.conf.tolist()
            cls = box.cls.tolist()

            if len(conf) > 0:
                # Create a list of dictionaries for detections
                detections = []
                for cf, cl in zip(conf, cls):
                    detection = {
                        "Class": names.get(cl, "Unknown"),
                        "Confidence": cf
                    }
                    detections.append(detection)

                analysis_info[frame_number] = {
                    "Filename": video_name,
                    "Frame Number": frame_number,
                    "Frame Time (s)": frame_number / fps,
                    "Detections": detections
                }

                annotated_frame = results[0].plot()

                # Save the frame to a file
                frame_filename = os.path.join(detection_dir, f"frame_{frame_number}.jpg")
                cv2.imwrite(frame_filename, annotated_frame)
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    # Return the analysis_info dictionary
    return analysis_info

# Define function to process videos using threading
def process_videos_with_threading(video_paths, save_folder):

    # Dictionary to store results for each video
    results_dict = {}

    # Process each video in a separate thread
    threads = []
    for video_path in video_paths:
        video_name = os.path.splitext(os.path.basename(video_path))[0].split("-")[-1]
        thread = Thread(target=lambda name, path: results_dict.update({name: thread_safe_predict(path, save_folder)}),
                        args=(video_name, video_path))
        thread.start()
        threads.append(thread)

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

    # Save results as JSON
    json_file_path = os.path.join(save_folder, "results.json")
    with open(json_file_path, "w") as json_file:
        json.dump(results_dict, json_file)

    # Return the results dictionary
    return results_dict

