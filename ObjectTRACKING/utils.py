import cv2
import imutils
import numpy as np

def CONTOURS(mask , frame ,pts):

	cnts = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	centre = None

	if len(cnts)>0:

		for c in cnts:
		#c = max(cnts , key=cv2.contourArea)
			if cv2.contourArea(c)>300:
				
				x,y,w,h = cv2.boundingRect(c)
				M = cv2.moments(c)
				centre = (int(M["m10"]/M["m00"]) , int(M["m01"]/M["m00"]))
				cv2.rectangle(frame , (x,y) , (x+w , y+h) ,(0,255,0) , 2)
				cv2.circle(frame, centre, 5, (0, 0, 255), -1)

	pts.appendleft(centre)

	return pts


def POINTS(pts , frame , args):

	for i in range(1, len(pts)):
		if pts[i-1] is None or pts[i] is None:
			continue

		thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
		cv2.line(frame, pts[i-1], pts[i], (0, 0, 255), thickness)

