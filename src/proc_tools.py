# -*- coding: utf-8 -*-
import numpy as np
import cv2
import imutils



def template_match(img,template):
	found = None
	#print(template.shape)
	(tH,tW) = img.shape

	for scale in np.linspace(0.2, 1.0, 30)[::-1]:

		resized = imutils.resize(img, width = int(img.shape[1] * scale))
		r = img.shape[1] / float(resized.shape[1])
		
		if resized.shape[0] < tH or resized.shape[1] < tW:
			break

		resized = cv2.GaussianBlur(resized,(3,3),0)
		#edged = cv2.Canny(resized, 30, 50)
	
		result = cv2.matchTemplate(resized, template, cv2.TM_CCOEFF)
		(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)
		
		if found is None or maxVal > found[0]:
			found = (maxVal, maxLoc, r)
	
	return found

def plotCircles(circles,image):
	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		for (x, y, r) in circles:

			x_centro = x 
			y_centro = y 

			cv2.circle( image, ( x_centro, y_centro ), r, (0, 255, 0), 2)
			cv2.rectangle( image, (x_centro - 2, y_centro - 2), (x_centro + 2, y_centro + 2), (0, 128, 255), -1)
		return image
	return image


def log_transform(img,param):
	img = img.astype(np.float) # Cast to float
	c = (img.max()) / (img.max()**(param))
	img = (c*img**(param)).astype(np.uint8)
	return img


def adjust_gamma(image, gamma=1.0):
	# build a lookup table mapping the pixel values [0, 255] to
	# their adjusted gamma values
	invGamma = 1.0 / gamma
	table = np.array([((i / 255.0) ** invGamma) * 255
		for i in np.arange(0, 256)]).astype("uint8")
 
	# apply gamma correction using the lookup table
	return cv2.LUT(image, table)