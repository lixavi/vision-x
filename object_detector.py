import tensorflow as tf
import cv2

class ObjectDetector:
    def __init__(self, model_path):
        self.model = tf.saved_model.load(model_path)
        self.detect_fn = self.model.signatures['serving_default']

    def detect_objects(self, image):
        input_tensor = tf.convert_to_tensor(image)
        detections = self.detect_fn(input_tensor)
        return detections
