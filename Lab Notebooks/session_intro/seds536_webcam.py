import sys

import numpy as np
import cv2

cam = cv2.VideoCapture(0)
if not cam.isOpened():
    print('Could not open camera!')
    sys.exit();

cam_w = cam.get(cv2.CAP_PROP_FRAME_WIDTH)
cam_h = cam.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(f'Camera Backend: {cam.getBackendName()}')
print(f'Frame size: {cam_w}x{cam_h}')

win_title = 'Video'
cv2.namedWindow(win_title)

print('starting capture, press q to quit.')
while True:
    result, img = cam.read()

    cv2.imshow(win_title, img)

    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break;

cam.release()
cv2.destroyAllWindows()
