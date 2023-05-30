import cv2
import os
import sys

ext = ".jpg"

def convert(input_dir, output_file):
    os.chdir(input_dir)

    images = []
    for f in os.listdir(input_dir):
        if f.endswith(ext):
            images.append(f)

    images.sort(key=lambda x: os.path.getmtime(x))

    if not images:
        print("Error! No frames to analyze. Check original video file path.")
        sys.exit(-1)

    frame = cv2.imread(images[0])
    cv2.imshow('video', frame)
    height, width, channels = frame.shape

    # Construct codec and VideoWriter
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_file, fourcc, 20.0, (width, height))

    for image in images:
        frame = cv2.imread(image)

        # Write frame to video
        out.write(frame)

    out.release()
    cv2.destroyAllWindows()