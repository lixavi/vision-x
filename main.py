from src.processing.video_processor import VideoProcessor

def main():
    model_path = 'data/pretrained_models/model.pb'  # Example path
    video_path = 'data/videos/sample.mp4'  # Example path
    processor = VideoProcessor(model_path)
    processor.process_video(video_path)

if __name__ == "__main__":
    main()
