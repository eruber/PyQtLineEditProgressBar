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
		self.setWindowTitle("PyQtLineEditProgressBar Demo")
		self.lineedit1 = PyQtLineEditProgressBar()
		self.lineedit1.setAlignment(QtCore.Qt.AlignCenter)
		#self.lineedit1.setSizePolicy()
		self.lineedit1.setText(self.lineedit1.getBehavior() + " {}".format(find_color_name(default_color_value)) )

		self.lineedit2 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT,
								progressbar_color=pqtpbar.DEFAULT_COLOR_RED)
		self.lineedit2.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit2.setText(self.lineedit2.getBehavior() + " {}".format(find_color_name(pqtpbar.DEFAULT_COLOR_RED)) )

		self.lineedit3 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT,
								progressbar_color=pqtpbar.DEFAULT_COLOR_ORANGE)
		self.lineedit3.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit3.setText(self.lineedit3.getBehavior() + " {}".format(find_color_name(pqtpbar.DEFAULT_COLOR_ORANGE)) )

		self.lineedit4 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT,
								progressbar_color=pqtpbar.DEFAULT_COLOR_BLUE)
		self.lineedit4.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit4.setText(self.lineedit4.getBehavior() + " {}".format(find_color_name(pqtpbar.DEFAULT_COLOR_BLUE)) )

		self.lineedit5 = PyQtLineEditProgressBar(progressbar_color=pqtpbar.DEFAULT_COLOR_YELLOW)
		self.lineedit5.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit5.setText(self.lineedit5.getBehavior() + " {}".format(find_color_name(pqtpbar.DEFAULT_COLOR_YELLOW)) )

		self.lineedit6 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT,
								progressbar_color=pqtpbar.DEFAULT_COLOR_PURPLE)
		self.lineedit6.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit6.setText(self.lineedit6.getBehavior() + " {}".format(find_color_name(pqtpbar.DEFAULT_COLOR_PURPLE)) )

		self.lineedit7 = PyQtLineEditProgressBar(behavior=pqtpbar.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT,
								progressbar_color="#32a893")
		self.lineedit7.setAlignment(QtCore.Qt.AlignCenter)
		self.lineedit7.setText(self.lineedit7.getBehavior() + " {}".format(find_color_name("#32a893")) )

		mainLayout.addWidget(self.lineedit1)
		mainLayout.addWidget(self.lineedit2)
		mainLayout.addWidget(self.lineedit3)
		mainLayout.addWidget(self.lineedit4)
		mainLayout.addWidget(self.lineedit5)
		mainLayout.addWidget(self.lineedit6)
		mainLayout.addWidget(self.lineedit7)

		button = QtWidgets.QPushButton('Update Progress')
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

		self.lineedit5.updateProgress(0.1)
		#self.lineedit5.setText(self.lineedit5.getBehavior())

		self.lineedit6.updateProgress(0.1)
		#self.lineedit6.setText(self.lineedit6.getBehavior())

		self.lineedit7.updateProgress(0.1)

		time.sleep(1)

# ----------------------------------------------------------------------------
def main():
	app = QtWidgets.QApplication([])
	window = Dialog()
	#window.resize(400, 50)
	window.setFixedSize(350, 350)
	window.show()
	app.exec_()

# ----------------------------------------------------------------------------
# ----------------------------- main -----------------------------------------
# ----------------------------------------------------------------------------
if __name__ == "__main__":
	main()