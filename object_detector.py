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

    def draw_detections(self, image, boxes, classes, scores):
        for i in range(len(scores)):
            if scores[i] > 0.5:
                ymin, xmin, ymax, xmax = boxes[i]
                xmin = int(xmin * image.shape[1])
                ymin = int(ymin * image.shape[0])
                xmax = int(xmax * image.shape[1])
                ymax = int(ymax * image.shape[0])
                class_id = int(classes[i])
                label = self.la
                bels[class_id]
                color = (0, 255, 0)  # Green colo
                r for bounding box
                cv2.rectangle(image, (xmin, ymin)
                , (xmax, ymax), color, 2)
                cv2.putText(image, f'{label}: {sc}'
                ores[i]', (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        return image
        