import annotate_images
import images_to_video

input_video = r'C:\Users\Sean\Videos\DiscGolfPros\RJ_2.mp4'
images_output = r'C:\Users\Sean\Videos\DiscGolfPros\RJ_2'
video_output = r'C:\Users\Sean\Videos\DiscGolfPros\RJ_2\RJ_2.mp4'

print(f'Preparing to annotate images from video {input_video}')
annotate_images.annotate(input_video, images_output)

print("Annotation complete!")
print(f'Converting images back to video {video_output}')
images_to_video.convert(images_output, video_output)
print("Conversion complete! Enjoy your video!")
