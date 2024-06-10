import cv2

# Global variables to store click coordinates
points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        if len(points) == 2:
            cv2.line(frame, points[0], points[1], (0, 255, 0), 2)
            cv2.imshow('Frame', frame)
            print(f'Line coordinates: {points}')
            points.clear()

# Specify the path to your video file
video_path = 'final traffic.mp4'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame', click_event)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize the frame if the width is greater than 1200
    height, width, _ = frame.shape
    if width > 1200:
        new_width = 600
        new_height = int(new_width * height / width)
        frame = cv2.resize(frame, (new_width, new_height))

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
