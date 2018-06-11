# -*- coding: utf-8 -*-
import pypylon

class cameraHandler(object):
	"""
	Essa classe é responsável pelas operacoes realizadas com a camera cameraHandler
	"""
	
	def __init__(self):
		super(cameraHandler, self).__init__()		
		self.version = pypylon.pylon_version.version
		self.findCameras()
		if not(self.selectCamera() is None):
			self.initCapture()
		else:
			self.capture = None

	def findCameras(self):
		self.available_cameras = pypylon.factory.find_devices()

	def selectCamera(self,index = -1):
		if(len(self.available_cameras) != 0):
			self.capture = pypylon.factory.create_device(self.available_cameras[index])
			self.camera =  self.capture.device_info		
		else:
			return None

	def initCapture():
		self.capture.open()

	def capture(self):
		if(self.capture is None):
			return None
		else:
			for image in self.capture.grab_images(1):
				return image
