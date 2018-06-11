# -*- coding: utf-8 -*-
import numpy as np
import cv2


from imageProc import *
from uiHandler import *
from camera import *


def openCap():
	global cap
	cap = cv2.VideoCapture('../img/sample1.mp4')

def getFrame():
	global cap
	if cap.isOpened():
		ret, frame = cap.read()
		return frame
	
def cicle():
	global app, proc
	frame = getFrame()
	if not(frame is None):
		frame = proc.run(frame)
		app.updateNow(frame)



if (__name__ == '__main__'):
	
	global app, proc
	cam = cameraHandler()
	openCap()

	app = QtApp()

	proc = imageProc()
	app.createPeriodicTask(cicle,50)
	app.run()


