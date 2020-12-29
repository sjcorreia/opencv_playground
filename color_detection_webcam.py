import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
	_, frame = cap.read()

    # Convert BGR to HSV
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of yellow color in HSV
	lower_yellow = np.array([20,100,100])
	upper_yellow = np.array([40,255,255])
    # define range of red color in HSV
	lower_red = np.array([0,100,100])
	upper_red = np.array([20,255,255])
    # define range of magenta color in HSV
	lower_magenta = np.array([140,100,100])
	upper_magenta = np.array([160,255,255])
    # define range of blue color in HSV
	lower_blue = np.array([110,50,50])
	upper_blue = np.array([130,255,255])
    # define range of cyan color in HSV
	lower_cyan = np.array([80,100,100])
	upper_cyan = np.array([100,255,255])
    # define range of green color in HSV
	lower_green = np.array([50,100,100])
	upper_green = np.array([70,255,255])
	
    # Threshold the HSV image to get only yellow colors
	mask_yellow = cv2.inRange(hsv, lower_yellow, upper_yellow)
	mask_red = cv2.inRange(hsv, lower_red, upper_red)
	mask_magenta = cv2.inRange(hsv, lower_magenta, upper_magenta)
	mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)
	mask_cyan = cv2.inRange(hsv, lower_cyan, upper_cyan)
	mask_green = cv2.inRange(hsv, lower_green, upper_green)

    # Bitwise-AND mask and original image
	res_yellow = cv2.bitwise_and(frame,frame, mask=mask_yellow)
	res_red = cv2.bitwise_and(frame,frame, mask=mask_red)
	res_magenta = cv2.bitwise_and(frame,frame, mask=mask_magenta)
	res_blue = cv2.bitwise_and(frame,frame, mask=mask_blue)
	res_cyan = cv2.bitwise_and(frame,frame, mask=mask_cyan)
	res_green = cv2.bitwise_and(frame,frame, mask=mask_green)
	
	cv2.imshow('frame',frame)
	#cv2.imshow('mask',mask)
	cv2.imshow('res_yellow',res_yellow)
	cv2.imshow('res_red',res_red)
	cv2.imshow('res_magenta',res_magenta)
	cv2.imshow('res_blue',res_blue)
	cv2.imshow('res_cyan',res_cyan)
	cv2.imshow('res_green',res_green)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break

cv2.destroyAllWindows()
