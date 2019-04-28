import cv2


def PrintLowH(x):
    #print("H value :" , x)
    pass

def PrintHighH(x):
	#print("HIgh H value:" , x)
	pass

def PrintLowS(x):
    #print("Low S value :" , x)
    pass

def PrintHighS(x):
	#print("High S value:" , x)
	pass

def PrintLowV(x):
    #print("Low v value :" , x)
    pass 

def PrintHighV(x):
	#print('High V value:' , x)
	pass


def Trackbar(window):
	cv2.createTrackbar('LowH',window, 0, 179, PrintLowH)
	cv2.createTrackbar('HighH',window, 0, 179, PrintHighH)
	cv2.createTrackbar('LowS',window, 0, 255, PrintLowS)
	cv2.createTrackbar('HighS',window, 0, 255, PrintHighS)
	cv2.createTrackbar('HighV',window, 0, 255, PrintHighV)
	cv2.createTrackbar('LowV',window, 0, 255, PrintLowV)

def PosValue(window):

	LH = cv2.getTrackbarPos('LowH' , window)
	HH = cv2.getTrackbarPos('HighH' , window)
	LS = cv2.getTrackbarPos('LowS' , window)
	HS = cv2.getTrackbarPos('HighS' , window)
	LV = cv2.getTrackbarPos('LowV' , window)
	HV = cv2.getTrackbarPos('HighV' , window)

	return LH , HH, LS , HS , LV , HV