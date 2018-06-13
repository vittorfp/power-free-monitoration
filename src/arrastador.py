# -*- coding: utf-8 -*-
from proc_tools import *
import cv2

class arrastadorVerifier(object):
	"""Classe que vai realizar as verificacoes no componente trolley"""
	def __init__(self):
		super(arrastadorVerifier, self).__init__()
		self.template = cv2.imread('../img/template/template_arrastador2.png')
		self.template = self.preProcess(self.template)
		#cv2.imshow("dffsd",self.template)
		#cv2.waitKey(0)
		#self.template_pos = cv2.cvtColor(cv2.imread('../img/template/template_arrastador_pos.jpg'), cv2.COLOR_BGR2GRAY)
		self.font = cv2.FONT_HERSHEY_SIMPLEX
		
	def check(self, frame):
		out = frame.copy()
		frame = self.preProcess(frame)
		if self.isArrastador(frame):
			(max_angle, out) = self.meassureAngle(frame,out)
			return (max_angle, out)
			print(max_angle)
		else:
			return (None, out)


	def isArrastador(self,frame):
		a = template_match(frame,self.template)
		#b = template_match(frame,template_pos)
		if(a is None):# | (b is None):
			pass
		else:
			(maxVal_pre, maxLoc1,_) = a
			#(maxVal_pos, maxLoc2) = b
		#if(  maxVal_pos > 1.4e8 ) | ( maxVal_pre > 1.05e8 ):
		#print maxVal_pre  
		if(  maxVal_pre > 100000000  ):
			return True
		else:
			return False

	def meassureAngle(self,frame,out):

		#TO-DO Definir parâmetros do processamento como atributos da classe
		#out = frame.copy()
		frame = cv2.Canny(frame,120,150,apertureSize = 3)
		lines = cv2.HoughLinesP(
			image = frame,
			rho = 1, 
			theta = np.pi/180, 
			threshold = 20,
			lines = np.array([]), 
			minLineLength = 25,
			maxLineGap = 10
			)

		vectors = [[0,0]]
		if lines is None:
			pass
		else:
			a,b,c = lines.shape
			for i in range(a):
				cv2.line(out, (lines[i][0][0], lines[i][0][1]), (lines[i][0][2], lines[i][0][3]), (0, 0, 255), 2, cv2.LINE_AA)
				vec = [[abs(lines[i][0][2] - lines[i][0][0]), abs(lines[i][0][3]-lines[i][0][1]) ]]
				vectors = np.append(vectors,vec,axis= 0)
				
			vectors = np.squeeze(vectors[1:])
			
			angles = []
			for vec1 in vectors:
				for vec2 in vectors:
					angle = np.arccos( np.inner(vec1,vec2)/(np.linalg.norm(vec1) * np.linalg.norm(vec2)))
					angles.append(angle*57.2958)

			max_angle = max(angles)
			cv2.putText(out,str(max_angle),(30,80), self.font, 1,(255,0,0),2,cv2.LINE_AA)
			return (max_angle, out)

	def preProcess(self,frame):
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		frame = cv2.equalizeHist(frame)
		frame = adjust_gamma(frame, gamma=10)
		frame = cv2.GaussianBlur(frame,(3,3),0)
		_, frame = cv2.threshold(frame,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
		
		return frame