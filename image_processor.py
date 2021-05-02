
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
