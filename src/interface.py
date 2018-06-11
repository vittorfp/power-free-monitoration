# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../ui/power-free.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1367, 710)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 611, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(790, 50, 191, 31))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 90, 1001, 581))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.now = QtGui.QWidget()
        self.now.setObjectName(_fromUtf8("now"))
        self.label_5 = QtGui.QLabel(self.now)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.now_graphicsView = QtGui.QGraphicsView(self.now)
        self.now_graphicsView.setGeometry(QtCore.QRect(10, 50, 651, 361))
        self.now_graphicsView.setObjectName(_fromUtf8("now_graphicsView"))
        self.tabWidget.addTab(self.now, _fromUtf8(""))
        self.summary = QtGui.QWidget()
        self.summary.setAccessibleName(_fromUtf8(""))
        self.summary.setAccessibleDescription(_fromUtf8(""))
        self.summary.setObjectName(_fromUtf8("summary"))
        self.label_2 = QtGui.QLabel(self.summary)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 331, 91))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tabWidget.addTab(self.summary, _fromUtf8(""))
        self.trolley = QtGui.QWidget()
        self.trolley.setObjectName(_fromUtf8("trolley"))
        self.label_3 = QtGui.QLabel(self.trolley)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tabWidget.addTab(self.trolley, _fromUtf8(""))
        self.desgaste = QtGui.QWidget()
        self.desgaste.setObjectName(_fromUtf8("desgaste"))
        self.label_6 = QtGui.QLabel(self.desgaste)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.tabWidget.addTab(self.desgaste, _fromUtf8(""))
        self.arrastador = QtGui.QWidget()
        self.arrastador.setObjectName(_fromUtf8("arrastador"))
        self.label_7 = QtGui.QLabel(self.arrastador)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tabWidget.addTab(self.arrastador, _fromUtf8(""))
        self.velocidade = QtGui.QWidget()
        self.velocidade.setObjectName(_fromUtf8("velocidade"))
        self.label_9 = QtGui.QLabel(self.velocidade)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 331, 91))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tabWidget.addTab(self.velocidade, _fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(790, 30, 191, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(1030, 120, 321, 531))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_10 = QtGui.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(0, 40, 311, 91))
        self.label_10.setWordWrap(True)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1367, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Sistema de monitoramento", None))
        self.label.setText(_translate("MainWindow", "Monitoramento - Transportadores power-free ", None))
        self.label_5.setText(_translate("MainWindow", "Imagens ao vivo do transportador.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.now), _translate("MainWindow", "Now", None))
        self.label_2.setText(_translate("MainWindow", "Nessa aba será mostrado um resumo das condições do transportador. Haverá um box mostrando os principais avisos, componentes proximos do fim da vida util, etc.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.summary), _translate("MainWindow", "Resumo do transportador", None))
        self.label_3.setText(_translate("MainWindow", "Nessa aba será mostrada a avaliação por visão dos trolleys em tempo real, estatisticas e projeções de vida util dos trolleys.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.trolley), _translate("MainWindow", "Trolleys", None))
        self.label_6.setText(_translate("MainWindow", "Nessa aba será mostrada a medição por visão dos espaços entre elos em tempo real. Junto com estatisticas, projeções e históricos de vida util da corrente forjada.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.desgaste), _translate("MainWindow", "Desgaste", None))
        self.label_7.setText(_translate("MainWindow", "Nessa aba será mostrada a avaliação por visão da angulação dos arrastadores em tempo real, estatisticas, projeções e histórico de vida util do componente.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.arrastador), _translate("MainWindow", "Arrastadores", None))
        self.label_9.setText(_translate("MainWindow", "Nessa aba será mostrado o histórico de velocidades de operação do transportador.", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.velocidade), _translate("MainWindow", "Velocidade de operação", None))
        self.label_4.setText(_translate("MainWindow", "Selecione o transportador:", None))
        self.groupBox.setTitle(_translate("MainWindow", "Transportador", None))
        self.label_10.setText(_translate("MainWindow", "Aqui vai ter uma foto do layout do transportador e algumas outras informações genéricas.", None))

