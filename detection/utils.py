import numpy as np

def resize_image(image, target_size=(300, 300)):
    return cv2.resize(image, target_size)

def preprocess_image(image):
    return image / 255.0

def postprocess_detections(boxes, classes, scores, confidence_threshold=0.5):
    valid_indices = np.where(scores > confidence_threshold)[0]
    return boxes[valid_indices], classes[valid_indices], scores[valid_indices]


    def get_language_code(self, lang_name):
        """
        Retrieves the code of a language given its name.

        Args:
        - lang_name (str): Name of the language.

        Returns:
        - str: Language code.
        """
        for code, name in self._supported_languages.items():
            if name.lower() == lang_name.lower():
                return code
        return None

    def get_language_code(self, lang_name):
        """
        Retrieves the code of a language given its name.

        Args:
        - lang_name (str): Name of the language.

        Returns:
        - str: Language code.
        """
        for code, name in self._supported_languages.items():
            if name.lower() == lang_name.lower():
                return code
        return None
