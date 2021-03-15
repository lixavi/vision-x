
    # Process video
    video_path = 'data/videos/sample.mp4'
    output_video_path = 'output/sample_output.mp4'
    video_processor = VideoProcessor(model_path, labels_path)
    video_processor.process_video(video_path, output_video_path)

    # Process image
    image_path = 'data/images/sample.jpg'
    output_image_path = 'output/sample_output.jpg'
    image_processor = ImageProcessor(model_path, labels_path)
    image_processor.process_image(image_path, output_image_path)

if __name__ == "__main__":
    main()
