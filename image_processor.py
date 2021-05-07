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


