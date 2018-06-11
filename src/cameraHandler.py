# -*- coding: utf-8 -*-
import pypylon

class cameraHandler(object):
	"""Essa classe eh responsavel pelas operacoes realizadas com a camera cameraHandler"""
	def __init__(self):

		super(cameraHandler, self).__init__()		
		
		self.version = pypylon.pylon_version.version
		self.camera =  self.capture.device_info
		
		self.capture.open()

	def findCameras(self):
		self.available_cameras = pypylon.factory.find_devices()

	def selectCamera(self,index = -1):
		self.capture = pypylon.factory.create_device(available_cameras[-1])
	
	def capture(self):
		if(self.capture is None):
			return None
		else:
			for image in self.capture.grab_images(1):
				return image
