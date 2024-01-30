import cv2
from .detection.object_detector import ObjectDetector

class VideoProcessor:
    def __init__(self, model_path):
        self.object_detector = ObjectDetector(model_path)

    def process_video(self, video_path):
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            # Process frame
            detections = self.object_detector.detect_objects(frame)
            # Render detections on frame
            cv2.imshow('Object Detection', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows()
