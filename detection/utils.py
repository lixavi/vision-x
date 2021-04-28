import numpy as np


def postprocess_detections(boxes, classes, scores, confidence_threshold=0.5):
    valid_indices = np.where(scores > confidence_threshold)[0]
    return boxes[valid_indices], classes[valid_indices], scores[valid_indices]
