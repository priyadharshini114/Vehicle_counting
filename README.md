# Traffic Object Counting with ultralytics and yolo:

This repository contains a Python script that utilizes the YOLOv8 object detection model and OpenCV to count objects crossing predefined lines in a video. The script processes a video file, tracks objects, and counts the number of times they cross specified lines, outputting the results to a new video file.

## Features:

- **YOLOv8 Model**: Leverages the state-of-the-art YOLOv8 model for object detection and tracking.
- **OpenCV Integration**: Utilizes OpenCV for video processing and visualization.
- **Multiple Counting Lines**: Configurable to count objects crossing multiple user-defined lines.
- **Video Output**: Generates an output video with object tracking and counting visualizations.
## Install Dependencies:
Ensure you have Python installed, then install the required packages:

pip install ultralytics opencv-python
pip install numpy
pip install opencv-python 


## Script Description:
The object_counting.py script performs the following steps:

Video Capture: Opens the tracked video file for processing.
Line Definition: Defines multiple lines for counting objects.
Video Writer: Initializes the video writer to save the output video.
Frame Processing: Processes each frame of the video to count objects crossing the lines.
Output Generation: Writes the processed frames to the output video file.
Cleanup: Releases video capture and writer resources.




