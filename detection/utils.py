import numpy as np



def preprocess_image(image):
    return image / 255.0

def postprocess_detections(boxes, classes, scores, confidence_threshold=0.5):
    valid_indices = np.where(scores > confidence_threshold)[0]
    return boxes[valid_indices], classes[valid_indices], scores[valid_indices]
