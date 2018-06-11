# -*- coding: utf-8 -*-
import cv2

from camera import *

import corrente
import trolley
import arrastador
import time

class imageProc(object):
	"""docstring for imageProc"""
	def __init__(self):
		super(imageProc, self).__init__()
		self.troley = trolley.TrolleyVerifier()
		self.arrastador = arrastador.arrastadorVerifier()
		self.chain = corrente.ChainVerifier()
		(self.x_topCorner_TROLLEY, self.y_topCorner_TROLLEY,self.x_botCorner_TROLLEY, self.y_botCorner_TROLLEY) = (300,30,400,280)
		(self.x_topCorner_ARRASTADOR, self.y_topCorner_ARRASTADOR,self.x_botCorner_ARRASTADOR, self.y_botCorner_ARRASTADOR) = (300,240,400,350)
		(self.x_topCorner_CORRENTE, self.y_topCorner_CORRENTE,self.x_botCorner_CORRENTE, self.y_botCorner_CORRENTE) = (260,190,440,260)
		

	def run(self,frame):
		(tr,arrast,chn,frame) = self.cropFrame(frame)

		(ok,tr) = self.troley.check(tr)
		(angle,arrast) = self.arrastador.check(arrast)
		#self.chain.meassure(chain)

		self.reinsertCrop(frame,tr,'trolley')
		self.reinsertCrop(frame,arrast,'arrastador')
		return frame

	def reinsertCrop(self,frame,new,type):
		if type == 'trolley':
			frame[ self.y_topCorner_TROLLEY:self.y_botCorner_TROLLEY,self.x_topCorner_TROLLEY:self.x_botCorner_TROLLEY] = new
		elif type == 'arrastador':
			frame[self.y_topCorner_ARRASTADOR:self.y_botCorner_ARRASTADOR,  self.x_topCorner_ARRASTADOR:self.x_botCorner_ARRASTADOR ] = new
		elif type == 'chain':
			frame[self.y_topCorner_CORRENTE:self.y_botCorner_CORRENTE,self.x_topCorner_CORRENTE:self.x_botCorner_CORRENTE ] = new

		return frame

	def cropFrame(self,frame):

		tr = frame[ self.y_topCorner_TROLLEY:self.y_botCorner_TROLLEY,self.x_topCorner_TROLLEY:self.x_botCorner_TROLLEY ]
		arrast = frame[self.y_topCorner_ARRASTADOR:self.y_botCorner_ARRASTADOR,  self.x_topCorner_ARRASTADOR:self.x_botCorner_ARRASTADOR ]
		chn = frame[self.y_topCorner_CORRENTE:self.y_botCorner_CORRENTE,self.x_topCorner_CORRENTE:self.x_botCorner_CORRENTE ]
	
		# TO-DO Tirar essa linha após ter escolhido o template
		#cv2.imwrite("../img/arrastadores/" +str(time.time() )+ '.png',arrast)
		
		cv2.rectangle(frame,(self.x_topCorner_TROLLEY,self.y_topCorner_TROLLEY),(self.x_botCorner_TROLLEY,self.y_botCorner_TROLLEY),(200,0,0),1)
		cv2.rectangle(frame,(self.x_topCorner_ARRASTADOR,self.y_topCorner_ARRASTADOR),(self.x_botCorner_ARRASTADOR,self.y_botCorner_ARRASTADOR),(200,0,0),1)
		cv2.rectangle(frame,(self.x_topCorner_CORRENTE,self.y_topCorner_CORRENTE),(self.x_botCorner_CORRENTE,self.y_botCorner_CORRENTE),(200,0,0),1)

		return (tr,arrast,chn,frame)
		# TO-DO: Fazer rotina que spega os parâmetros do local dos crops de um arquivo