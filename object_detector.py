import numpy as np
import tensorflow as tf
import cv2

class ObjectDetector:
    def __init__(self, model_path, labels_path):
        self.model = tf.saved_model.load(model_path)
        self.labels = self.load_labels(labels_path)
        self.detect_fn = self.model.signatures['serving_default']

    def load_labels(self, labels_path):
        with open(labels_path, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def detect_objects(self, image):
        input_tensor = tf.convert_to_tensor(image)
        detections = self.detect_fn(input_tensor)
        boxes = detections['detection_boxes'][0].numpy()
        classes = detections['detection_classes'][0].numpy().astype(np.uint8)
        scores = detections['detection_scores'][0].numpy()
        return boxes, classes, scores

 
