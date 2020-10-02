"""
Demo source for PyQtLineEditProgressBar

"""
import time

from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

import pyqtlineeditprogressbar as pqtpbar
from pyqtlineeditprogressbar import PyQtLineEditProgressBar

def find_color_name(color_value):
	name = 'CUSTOM color'
	for color_name in pqtpbar.EMBEDDED_COLORS:
		if pqtpbar.EMBEDDED_COLORS[color_name] == color_value:
			name = "DEFAULT {}".format(color_name)

	return('with {} [{}]'.format(name, color_value))


default_color_value = pqtpbar.EMBEDDED_COLORS[pqtpbar.DEFAULT_COLOR_NAME]

class Dialog(QtWidgets.QDialog):

	def __init__(self, parent=None):
		QtWidgets.QDialog .__init__(self, parent)
		mainLayout = QtWidgets.QVBoxLayout()
		self.setWindowTitle("PyQtLineEditProgressBar Behaviors")
		self.lineedit1 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_EMPTY_FILLS_LEFT_TO_RIGHT)
		self.lineedit1.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit1.setText(self.lineedit1.getBehavior().upper().replace('-','_'))

		self.lineedit2 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT)
		self.lineedit2.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit2.setText(self.lineedit2.getBehavior().upper().replace('-','_'))

		self.lineedit3 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT)
		self.lineedit3.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit3.setText(self.lineedit3.getBehavior().upper().replace('-','_'))

		self.lineedit4 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT)
		self.lineedit4.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit4.setText(self.lineedit4.getBehavior().upper().replace('-','_'))

		mainLayout.addWidget(self.lineedit1)
		mainLayout.addWidget(self.lineedit2)
		mainLayout.addWidget(self.lineedit3)
		mainLayout.addWidget(self.lineedit4)

		button = QtWidgets.QPushButton('The Four Behaviors')
		button.clicked.connect(self.buttonClicked)
		mainLayout.addWidget(button)
		self.setLayout(mainLayout)

	def buttonClicked(self):
		self.lineedit1.updateProgress(0.1)
		#self.lineedit1.setText(self.lineedit1.getBehavior())

		self.lineedit2.updateProgress(0.1)
		#self.lineedit2.setText(self.lineedit2.getBehavior())

		self.lineedit3.updateProgress(0.1)
		#self.lineedit3.setText(self.lineedit3.getBehavior())

		self.lineedit4.updateProgress(0.1)
		#self.lineedit4.setText(self.lineedit4.getBehavior())

		time.sleep(0.5)

app = QtWidgets.QApplication([])
window = Dialog()
#window.resize(400, 50)
window.setFixedSize(250, 150)
window.setWindowFlags(QtCore.Qt.FramelessWindowHint)
window.show()
app.exec_()