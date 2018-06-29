# -*- coding: utf-8 -*-
import cv2
from proc_tools import *

class TrolleyVerifier(object):
	"""Classe que vai realizar as verificacoes no componente trolley"""
	def __init__(self):
		super(TrolleyVerifier, self).__init__()
		self.template = self.loadTemplate()
		
		# Setar parametros de detecção
		# TO-DO: Fazer buscar esses parametros de um arquivo
		self.limiar = 0.45e7
		
		self.max_wheelRadius = 37
		self.min_wheelRadius = 30
		self.sens_wheelRadius = 4

		self.max_centerRadius = 20
		self.min_centerRadius = 9
		self.sens_centerRadius = 20
		
	def check(self,frame):
		out = frame.copy()
		(detection, circle) = self.preProcess(frame)
		if self.isTrolley(detection):
			(has, wheel) = self.hasWheel(circle)
			if has:
				(has, center) = self.detectCenter(circle, wheel)
				#print(center)
				out = plotCircles(wheel,out)
				if has:
					out = plotCircles(center,out)
			else:
				return (False,out)

		return (True,out)
	
	def preProcess(self,frame):
		frame = cv2.GaussianBlur(frame,(3,3),0)
		circle = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		detection = cv2.Canny(frame, 30, 50)
		return (detection, circle)
	
	def isTrolley(self,frame):
		a = template_match(frame,self.template)
		if not(a is None):
			(maxVal, _, _) = a
		else:
			return False
		#print maxVal
		return maxVal > self.limiar

	def hasWheel(self,frame):
		whl = self.detectWheel(frame)
		if(whl is None):
			return (False,None)
		else:
			frame = plotCircles(whl,frame)
			return (True, whl)

	def detectCenter(self,frame, wheel):
		wheel = np.squeeze(wheel)
		
		[x,y,r] = wheel
		x = int(x)
		y = int(y)
		r = int(r)
		# delimita o quadrado inscrito no circulo para a busca pelo centro do trolley
		dentro_bola = frame[ y - r : y + r,   x - r : x + r ]
		#print(dentro_bola)
		#print(wheel)
		if(dentro_bola == []):
			circulo_interno = cv2.HoughCircles(
				dentro_bola, 
				cv2.HOUGH_GRADIENT, 
				self.sens_centerRadius,
				300, 
				maxRadius = self.max_centerRadius, 
				minRadius = self.min_centerRadius
			)
		else:
			circulo_interno = None
		if not (circulo_interno is None):
			# Parametros do circulo externo
			x_ext_s = x  
			y_ext_s = y 
			r_ext_s = r
			
			x_centro_interno = x  #+ r_ext_s
			y_centro_interno = y  #+ r_ext_s 
			circulo_interno[0][0][0] = x_centro_interno
			circulo_interno[0][0][1] = y_centro_interno
			#print(circulo_interno)
			return (True,circulo_interno)
		else:
			return (False,None)

	def loadTemplate(self):

		template = cv2.imread("../img/template/trolley.png")
		template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
		return template

	def detectWheel(self,frame):
		circles = cv2.HoughCircles(
			frame, 
			cv2.HOUGH_GRADIENT, 
			self.sens_wheelRadius,
			300, 
			maxRadius = self.max_wheelRadius, 
			minRadius = self.min_wheelRadius
		)
		return circles

	def bearing(self):
		pass