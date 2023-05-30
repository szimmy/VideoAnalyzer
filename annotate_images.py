import cv2
import mediapipe as mp
import numpy as np
import sys
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def annotate(video_file, output_dir):

    video = cv2.VideoCapture(video_file)

    current_frame = 0

    while(True):
        ret, frame = video.read()

        if ret:
            name = output_dir + r'\frame' + str(current_frame) + ".jpg"
            print(f'Frame {current_frame} to {name}')
            current_frame = current_frame + 1

            BG_COLOR = (192, 192, 192) # gray
            with mp_pose.Pose(
                static_image_mode=True, # TODO DO PERF TESTS WITH THIS SET TO FALSE!!!
                model_complexity=2,
                enable_segmentation=True,
                min_detection_confidence=0.5) as pose:
                # Convert the BGR image to RGB before processing.
                results = pose.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

                if not results.pose_landmarks:
                    continue

                annotated_image = frame.copy()
                # Draw segmentation on the image.
                # To improve segmentation around boundaries, consider applying a joint
                # bilateral filter to "results.segmentation_mask" with "image".
                condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
                bg_image = np.zeros(frame.shape, dtype=np.uint8)
                bg_image[:] = BG_COLOR
                annotated_image = np.where(condition, annotated_image, bg_image)
                # Draw pose landmarks on the image.
                # TODO see https://stackoverflow.com/questions/75365431/mediapipe-display-body-landmarks-only
                # to draw subset
                mp_drawing.draw_landmarks(
                    annotated_image,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())
                cv2.imwrite(name, annotated_image)
        else:
            break

    video.release()
    cv2.destroyAllWindows()