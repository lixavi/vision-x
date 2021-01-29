from src.processing.video_processor import VideoProcessor
from src.processing.image_processor import ImageProcessor

def main():
    model_path = 'data/pretrained_models/model.pb'
    labels_path = 'data/pretrained_models/labels.txt'


    # Process image
    image_path = 'data/images/sample.jpg'
    output_image_path = 'output/sample_output.jpg'
    image_processor = ImageProcessor(model_path, labels_path)
    image_processor.process_image(image_path, output_image_path)

if __name__ == "__main__":
    main()
