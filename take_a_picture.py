from imutils.video import VideoStream
import imutils
import time
import cv2

vs = VideoStream(src=0).start()
time.sleep(2.0)

# grab just a single frame
frame = vs.read()

# maybe you want to shrink the frame, maybe not
# frame = imutils.resize(frame, width=400)

# save the image
cv2.imwrite("test.jpg", frame)
