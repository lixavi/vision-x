import cv2
from .object_detector import ObjectDetector

class ImageProcessor:
    def __init__(self, model_path, labels_path):
        self.object_detector = ObjectDetector(model_path, labels_path)

    def process_image(self, image_path, output_path=None):
        # Load image
        image = cv2.imread(image_path)
        if image is None:
            print("Error: Couldn't open image file.")
            return

        # Perform object detection
        boxes, classes, scores = self.object_detector.detect_objects(image)
        # Draw detection results on the image
        self.object_detector.draw_detections(image, boxes, classes, scores)

        # Display or save the processed image
        if output_path:
            cv2.imwrite(output_path, image)
            print(f"Processed image saved to {output_path}")
        else:
            cv2.imshow('Object Detection', image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            #end
