import cv2
import os

# Specify the path to the video file
video_path = '/home/kalpit/Documents/dataset/openhand.mov'

# Create a directory to store the output images
output_dir = '/home/kalpit/Documents/dataset/open_hand'
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize a counter for naming the output image files
count = 569

# Open the video file
cap = cv2.VideoCapture(video_path)

# Set the frame rate to 20 frames per second
fps = 10
delay = int(1000 / fps)

# Loop through the frames of the video
while cap.isOpened():
    # Read a frame from the video
    ret, frame = cap.read()

    # If the frame was read successfully, save it to a file
    if ret:
        # Increment the counter
        count += 1

        # Save the frame to a file in the output directory
        filename = os.path.join(output_dir, 'open_hand{:04d}.png'.format(count))
        cv2.imwrite(filename, frame)
        # Delay to achieve the desired frame rate
        cv2.waitKey(delay)
    else:
        # Break the loop if the end of the video is reached
        break

# Release the video capture object
cap.release()
cv2.destroyAllWindows()
