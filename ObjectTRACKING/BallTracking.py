import cv2
import numpy as np
import argparse
from collections import deque
from utils import * 
import time
from imutils.video import VideoStream
import imutils

arg = argparse.ArgumentParser()
arg.add_argument("-v", "--video" , help="path to video file")
arg.add_argument("-b" , "--buffer" ,type=int ,default=64 , help="max buffer size")
args = vars(arg.parse_args())

#LH:10 , LS:181 , LV:82 , HH:42 , HS:225 , HV:207
lower_limit=(10,181,82)
upper_limit=(42,225,207)
#lower_limit = (87,72,45)
#upper_limit = (157 , 255 , 255)

pts = deque(maxlen=args['buffer'])

if not args.get('video' , False):
	vs = VideoStream(src=0).start()
else:
	vs = cv2.VideoCapture(0)
time.sleep(2.0)

while True:

	frame = vs.read()
	frame = frame[1] if args.get('video' , False) else frame

	if frame is None:
		break

	frame = imutils.resize(frame , width=600)
	blurred = cv2.GaussianBlur(frame , (11,11) , 0)
	canny = cv2.Canny(blurred , 100 ,200)
	hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
	mask = cv2.inRange(hsv  , lower_limit , upper_limit)
	mask = cv2.erode(mask  , None , iterations=2)
	mask = cv2.dilate(mask , None , iterations=2)


	#calling contours function from utils
	pts = CONTOURS(mask=mask ,frame=frame , pts=pts)
	POINTS(pts=pts , frame=frame , args =args)

	cv2.imshow('tracking' , frame)
	cv2.imshow("mask" , mask)
	#cv2.imshow("edges" ,canny)
	if cv2.waitKey(1)==32:
		break


if not args.get("video", False):
	vs.stop()
# otherwise, release the camera
else:
	vs.release()
 
# close all windows
cv2.destroyAllWindows()