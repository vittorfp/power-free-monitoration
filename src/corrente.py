# -*- coding: utf-8 -*-
import cv2
import numpy as np
from proc_tools import *

import matplotlib.pyplot as plt

class ChainVerifier(object):
	"""Classe que vai realizar as verificacoes no componente trolley"""
	def __init__(self):
		super(ChainVerifier, self).__init__()
		self.threshold = 70
		self.line1 = LineMeassure( 5 , (0,0,200) )
		self.line2 = LineMeassure( 10, (0,0,200) )
		self.line3 = LineMeassure( 15, (0,0,200) )
		self.line4 = LineMeassure( 20, (0,0,200) )
		self.line5 = LineMeassure( 25, (0,0,200) )
	
	def check(self,frame):
		out   = frame.copy()
		(detection,meassure) = self.preProcess(frame)
		if self.isGap(detection):
			(size, out) = self.meassureSize(meassure,out)
			return (size, out)
		else:
			return(None,out)


	def isGap(self,detection):
		s = np.sum( np.sum(detection) ) 
		if s > 680000:
			return True
		else:
			return False
			


	def meassureSize(self,frame,out):

		mx1 = self.line1.Update(frame)
		mx2 = self.line2.Update(frame)
		mx3 = self.line3.Update(frame)
		mx4 = self.line4.Update(frame)
		mx5 = self.line5.Update(frame)

		soma = 0

		if mx1 > self.threshold :
			out = self.line1.PlotLine(out)
			soma += 1
		
		if mx2 > self.threshold :
			out = self.line2.PlotLine(out)
			soma += 1
		
		if mx3 > self.threshold :
			out = self.line3.PlotLine(out)
			soma += 1
		
		if mx4 > self.threshold :
			out = self.line4.PlotLine(out)
			soma += 1
		
		if mx5 > self.threshold :
			out = self.line5.PlotLine(out)
			soma += 1
		
		if soma >= 1:
			return(max([mx1,mx2,mx3,mx4,mx5]),out )
		else:
			return(0,out)

	def preProcess(self,frame):
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = adjust_gamma(frame, gamma=0.3)
		frame = log_transform(frame,0.6)
		_,frame = cv2.threshold(frame,127,255,cv2.THRESH_BINARY)
		detection = frame.copy()
		#frame = cv2.equalizeHist(frame)
		#frame = cv2.adaptiveThreshold(frame,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,3)
		meassure = cv2.Canny(frame, 900, 1000)

		return (detection,meassure)


class LineMeassure(object):
	"""docstring for LineMeassure"""
	def __init__(self, height, color ):
		super(LineMeassure, self).__init__()
		self.height = height
		self.color = color

	def Update(self,frame):
		self.frame = frame
		self.line = frame[self.height,:]
		

		dists = np.squeeze( np.argwhere(self.line == 255) )
		try:
			dists.shape[0]
			dif = np.diff(dists)
			mx = np.max(dif)
			idx_dif = np.argwhere(dif == mx)
					
			self.init = np.squeeze(dists[idx_dif])
			self.end  = np.squeeze(dists[idx_dif+1])
		except:
			mx = 0
			#print(dists)
		return mx
		
		

	def PlotLine(self,frame):
		return cv2.line(frame,(self.init, self.height),(self.end, self.height),self.color, 2)
		