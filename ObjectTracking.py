import cv2 
import numpy as np 
from utils import *

kernel = np.ones((5,5) , np.uint8)
cap = cv2.VideoCapture(0)

black = np.zeros((500,400,3) , np.uint8)
cv2.namedWindow('black')

#creating trackbar
Trackbar('black')

while True:

	ret, frame = cap.read()
	resize = cv2.resize(frame , (500,400)) #resize the frame
	hsv = cv2.cvtColor(resize , cv2.COLOR_BGR2HSV)  #converting frame into hsv 
	
	LH , HH, LS , HS , LV , HV = PosValue('black') # getting values from track bar

	lower_limit = np.array([LH,LS,LV])
	upper_limit = np.array([HH,HS,HV])
	
	#creating mask with hsv values
	mask = cv2.inRange(hsv , lower_limit , upper_limit)
	#res = cv2.bitwise_and(resize , resize , mask=mask )

	#morphological opening & closing 
	mask =cv2.morphologyEx(mask ,cv2.MORPH_OPEN, kernel)
	mask=cv2.morphologyEx(mask , cv2.MORPH_CLOSE, kernel )

	#edge detection
	edges = cv2.Canny(mask , 100 , 200)

	#finding contours
	image , contours , hier = cv2.findContours(mask , cv2.RETR_TREE ,cv2.CHAIN_APPROX_SIMPLE)

	if len(contours)>0:
		#drawing contours
		#cnts = contours[len(contours)-1]
		
		img = cv2.drawContours(resize.copy() , contours , -1 , (0,255,0) , 3)
		c= max(contours , key=cv2.contourArea)
		x,y,w,h = cv2.boundingRect(c)
		cv2.rectangle(resize,(x,y),(x+w,y+h),(0,255,0),2)
		cv2.imshow('contours' , img)

	cv2.imshow('edges' , edges)
	cv2.imshow( 'black' , mask)
	cv2.imshow('frame ' , resize)
	
	if cv2.waitKey(1)==32:
		break

print("The values for LH:{} , LS:{} , LV:{} , HH:{} , HS:{} , HV:{}".format(LH,LS,LV,HH,HS,HV))
cv2.destroyAllWindows()
cap.release()