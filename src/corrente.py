# -*- coding: utf-8 -*-
import cv2

class ChainVerifier(object):
	"""Classe que vai realizar as verificacoes no componente trolley"""
	def __init__(self):
		super(ChainVerifier, self).__init__()
		self.template = 0
		

	def check(self):
		out   = frame.copy()
		#frame = frame[70:100,50:300]
		frame = self.preProcess(frame)
		if self.isGap(frame):
			(size,out) = self.meassureSize(frame, out)
			print(size)
		


	def isGap(self):
		pass

	def meassureSize(self):
		pass


	def preProcess(self,frame):
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.equalizeHist(frame)
		frame = adjust_gamma(frame, gamma=0.6)
		frame = cv2.equalizeHist(frame)
		frame = adjust_gamma(frame, gamma=0.8)
		frame = cv2.equalizeHist(frame)
		frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,4)
		frame = cv2.Canny(frame, 900, 1000)
		return frame
		