#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QMainWindow, QLabel, QAction, QFileDialog, QApplication, QMessageBox, QPushButton)
from PyQt5.QtGui import QIcon
import sys
import os

import imagefunctions

class Example(QMainWindow):
	
	def __init__(self):
		super().__init__()
		
		self.initUI()
		self.selectedFile = ""                    
 
		if 'HOME' in os.environ:
			self.home = os.environ['HOME']
		elif os.name == 'posix':
			self.home = os.path.expanduser("~/")
		elif os.name == 'nt':
			if 'HOMEPATH' in os.environ and 'HOMEDRIVE' in os.environ:
				self.home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
		else:
			self.home = os.curdir
		
	def initUI(self):      


		btn_1 = QPushButton( "convert",self )
		btn_1.clicked.connect( self.convertFile( "Hermann") ) 
		btn_1.move(10,10)
		btn_2 = QPushButton( "select",self )
		btn_2.clicked.connect( self.showDialog ) 
		btn_2.move(130,10)
		
		self.statusBar()
		self.fileLable = QLabel("File: ")

		openFile = QAction(QIcon('open.png'), 'Open', self)
		openFile.setShortcut('Ctrl+O')
		openFile.setStatusTip('Open new File')
		openFile.triggered.connect(self.showDialog)

		menubar = self.menuBar()
		fileMenu = menubar.addMenu('&File')
		fileMenu.addAction(openFile)       
		
		self.setGeometry(300, 300, 350, 300)
		self.setWindowTitle('Convert HEIC to JPEG')
		self.show()
		
		
	def showDialog(self):

		fname = QFileDialog.getOpenFileName(self, 'Open file', self.home)
		
		self.selectedPath = fname[0]
		if self.selectedPath:
			self.selectedFile = fname[0][fname[0].rfind('/')+1: ]
			self.selectedFileEnd = fname[0][fname[0].rfind('.'):]
			self.statusBar().addPermanentWidget(self.fileLable)
			self.fileLable.setText("File: " + self.selectedFile)
			self.statusBar().showMessage('file selected')


	def on_button_clicked(self, name):
		# parameter name currently not used

		# alert if no file is selected
		if self.selectedFile == "":
			alert = QMessageBox()
			alert.setText('first select a file!')
			self.statusBar().showMessage('no file selected')
			alert.exec_()

		# start converting file
		elif (self.selectedFileEnd == '.HEIC' ) | (self.selectedFileEnd == '.heic' ):
			self.statusBar().showMessage('start converting')
			if imagefunctions.convFile(self.selectedPath) == 1:
				self.statusBar().showMessage('file converted')
			elif imagefunctions.convFile(self.selectedPath) == 2:
				self.statusBar().showMessage('file exits')
			else:
				self.statusBar().showMessage('Something went wrong')
		else:
			# alert if not supported file is selected
			self.statusBar().showMessage('file type not supported')


	def convertFile(self, parameter):
		return lambda : self.on_button_clicked( parameter )


		
if __name__ == '__main__':
	
	app = QApplication(sys.argv)
	ex = Example()
	sys.exit(app.exec_())