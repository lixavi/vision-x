import cv2
from .object_detector import ObjectDetector

class VideoProcessor:
    def __init__(self, model_path, labels_path):
        self.object_detector = ObjectDetector(model_path, labels_path)

    def process_video(self, video_path, output_path=None):
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            print("Error: Couldn't open video file.")
            return

        fps = cap.get(cv2.CAP_PROP_FPS)
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if output_path:
            out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Perform object detection
            boxes, classes, scores = self.object_detector.detect_objects(frame)
            # Draw detection results on the frame
            self.object_detector.draw_detections(frame, boxes, classes, scores)

            # Display the frame
            cv2.imshow('Object Detection', frame)
            if output_path:
                out.write(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

