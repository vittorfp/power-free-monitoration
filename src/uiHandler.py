# -*- coding: utf-8 -*-
from PyQt4 import QtGui, uic, QtCore
import interface
import sys
import cv2

# Como gerar o .py de um .ui
#pyuic4 ../ui/power-free.ui > interface.py


class QtApp(object):
	def __init__(self):
		self.app = QtGui.QApplication(sys.argv)
		self.window = MyWindow()
		self.window.show()
		self.timer = []
		self.nowScene = QtGui.QGraphicsScene(self.window.now) 

	
	def createPeriodicTask(self,function,period):
		self.timer.append(QtCore.QTimer())
		self.timer[-1].timeout.connect(function)
		self.timer[-1].start(period)

	def updateNow(self,image):
		#image = imutils.resize(image, width = int(image.shape[1] * 0.8))
		height, width, _ = image.shape
		#image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)	
		img = QtGui.QImage(image.tobytes(), width, height, QtGui.QImage.Format_RGB888)
		pixmap = QtGui.QPixmap.fromImage(img)
		img = QtGui.QImage()

		self.nowScene.clear()
		self.nowScene.addPixmap(pixmap)
		self.window.now_graphicsView.setScene(self.nowScene)
		self.window.now_graphicsView.show()
		self.nowScene.update()

	
	def updateFrame(self):
		pass

	def initWindow(self):
		pass

	def showWindow(self):
		pass

	def fillTransporters(self):
		pass

	def run(self):
		sys.exit( self.app.exec_() )


class MyWindow(QtGui.QMainWindow, interface.Ui_MainWindow):

	def __init__(self):
		#Esseinicializa a classe mae
		super(MyWindow, self).__init__()
		self.setupUi(self)

		



	