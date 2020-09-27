
"""
PyQtLineEditProgressBar

This module subclass Qt's QtLineEdit widget to manage a progress
bar the is displayed as the background color of the QtLineEdit.

REFERENCE:
https://stackoverflow.com/questions/36972132/how-to-turn-qlineedit-background-into-a-progress-bar

GPL LICENSE
This file is part of the PyQtLineEditProgressBar package.

AutoFoE is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

AutoFoE is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with AutoFoE in the file named COPYING. If not, 
see <https://www.gnu.org/licenses/>.

COPYRIGHT (C) 2019-2020 E.R. Uber (eruber@gmail.com)

"""
# ----------------------------------------------------------------------------
# ------------------------ Python Standard Library ---------------------------
# ----------------------------------------------------------------------------
import time

# ----------------------------------------------------------------------------
# -------------------------- Third Party Packages ----------------------------
# ----------------------------------------------------------------------------
from PyQt5 import QtCore
from PyQt5 import QtGui
from PyQt5 import QtWidgets

from colour import Color  # https://pypi.org/project/colour/

# ----------------------------------------------------------------------------
# ----------------------- Module Global & Constants --------------------------
# ----------------------------------------------------------------------------

# Default Embedded Color Names
DECN = ['green', 'red', 'blue', 'orange', 'yellow', 'purple']

DEFAULT_COLOR_GREEN  = '#aaff7f'   # A pastel mint green
DEFAULT_COLOR_RED    = '#ffa5aa'   # A pastel red
DEFAULT_COLOR_BLUE   = '#b3fff4'   # A pastel blue   
DEFAULT_COLOR_ORANGE = '#ffcc74'   # A pastel orange
DEFAULT_COLOR_YELLOW = '#ffff00'   # A pastel yellow
DEFAULT_COLOR_PURPLE = '#e4b7ff'   # A pastel yellow

EMBEDDED_COLORS = {
	DECN[0] : DEFAULT_COLOR_GREEN, 
	DECN[1] : DEFAULT_COLOR_RED,   
	DECN[2] : DEFAULT_COLOR_BLUE,  
	DECN[3] : DEFAULT_COLOR_ORANGE,
	DECN[4] : DEFAULT_COLOR_YELLOW,
	DECN[5] : DEFAULT_COLOR_PURPLE,
}

DEFAULT_COLOR_NAME = DECN[0]

STARTS_EMPTY_FILLS_LEFT_TO_RIGHT  = 'starts-empty-fills-left-to-right'
STARTS_EMPTY_FILLS_RIGHT_TO_LEFT  = 'starts-empty-fills-right-to-left'
STARTS_FULL_EMPTIES_LEFT_TO_RIGHT = 'starts-filled-empties-left-to-right'
STARTS_FULL_EMPTIES_RIGHT_TO_LEFT = 'starts-filled-empties-right-to-left'

BEHAVIORS = [STARTS_EMPTY_FILLS_LEFT_TO_RIGHT,  STARTS_EMPTY_FILLS_RIGHT_TO_LEFT,
			 STARTS_FULL_EMPTIES_LEFT_TO_RIGHT, STARTS_FULL_EMPTIES_RIGHT_TO_LEFT]

LEFT_2_RIGHT = [STARTS_EMPTY_FILLS_LEFT_TO_RIGHT, STARTS_FULL_EMPTIES_LEFT_TO_RIGHT]
RIGHT_2_LEFT = [STARTS_EMPTY_FILLS_RIGHT_TO_LEFT, STARTS_FULL_EMPTIES_RIGHT_TO_LEFT]

BEHAVIOR_MAP = { # init_value, set_color_at_1, set_color_at_3, delta_sign
	BEHAVIORS[0] : [0.001, -0.001,  0.001,  1],  # Count up
	BEHAVIORS[1] : [0.999,  0.001, -0.001, -1],  # Count up
	BEHAVIORS[2] : [0.001,  0.001, -0.001,  1],  # Count down
	BEHAVIORS[3] : [0.999, -0.001,  0.001, -1],  # Count down
}

DEFAULT_BEHAVIOR = STARTS_EMPTY_FILLS_LEFT_TO_RIGHT

# ----------------------------------------------------------------------------
# --------------------- Module Classes & Functions ---------------------------
# ----------------------------------------------------------------------------
# https://doc.qt.io/qt-5/qlineedit.html
class PyQtLineEditProgressBar(QtWidgets.QLineEdit):

	def __init__(self, contents=None, parent=None, 
				read_only=True, 
				progressbar_color=EMBEDDED_COLORS[DECN[0]], 
				behavior=DEFAULT_BEHAVIOR,
				text_for_bounding_rect=None,
				):

		super(PyQtLineEditProgressBar, self).__init__(parent=parent) 

		self._parent   = parent
		self._contents = contents
		self._text_for_bounding_rect = text_for_bounding_rect
		
		self._size_hint_qrect = None

		if self._contents:
			self.setText(self._contents)
		self.setReadOnly(read_only)
		self.setProgressBarColor(progressbar_color)
		self.setProgressBarBehavior(behavior)

		self._update_progress_bar()

	# https://doc.qt.io/qtforpython/PySide2/QtGui/QLinearGradient.html#detailed-description
	# https://doc.qt.io/qt-5/qlineargradient.html#details
	def _update_progress_bar(self):

		palette = self.palette()
		QRectF = QtCore.QRectF(self.rect())
		gradient = QtGui.QLinearGradient(QRectF.topLeft(), QRectF.topRight())
		# https://doc.qt.io/qt-5/qgradient.html#setColorAt
		gradient.setColorAt(self._value+self._param_1, QtGui.QColor(self._color))
		gradient.setColorAt(self._value, QtGui.QColor('#ffffff'))
		gradient.setColorAt(self._value+self._param_3, QtGui.QColor('#ffffff'))
		palette.setBrush(QtGui.QPalette.Base, QtGui.QBrush(gradient))
		self.setPalette(palette)		
	
	def _clear_progress_bar(self):
		palette = self.palette()
		QRectF = QtCore.QRectF(self.rect())
		gradient = QtGui.QLinearGradient(QRectF.topLeft(), QRectF.topRight())
		# https://doc.qt.io/qt-5/qgradient.html#setColorAt
		gradient.setColorAt(0, QtGui.QColor('#ffffff'))
		#gradient.setColorAt(value, QtGui.QColor('#ffffff'))
		gradient.setColorAt(1, QtGui.QColor('#ffffff'))
		palette.setBrush(QtGui.QPalette.Base, QtGui.QBrush(gradient))
		self.setPalette(palette)		

	# -------------------------------------------------------------------------
	# QLineEdit Methods that are over-ridden
	# -------------------------------------------------------------------------
	
	def sizeHint(self):
		if self._text_for_bounding_rect:
			if self._size_hint_qrect:
				# We cache these rather than doing the expensive font calls 
				# over and over
				w = self._size_hint_qrect.width()
				h = self._size_hint_qrect.height()
			else:	
				metrics = QtGui.QFontMetrics(self.font())

				# These are probably the widest integers...
				self._size_hint_qrect = metrics.boundingRect(self._text_for_bounding_rect)
				w = self._size_hint_qrect.width()
				h = self._size_hint_qrect.height()

			return(QtCore.QSize(w, h))
		else:  
			return(super(PyQtLineEditProgressBar, self).sizeHint())

	# -------------------------------------------------------------------------
	# Public API
	# -------------------------------------------------------------------------

	def updateProgress(self, delta_float):
		if self._progressbar_behavior in LEFT_2_RIGHT:
			if self._value >= 0.998:
				self._value = 0.001
			elif self._value > 0.9:
				self._value = 0.999
			else:
				self._value = self._value + (self._delta_sign * delta_float)
		elif self._progressbar_behavior in RIGHT_2_LEFT:
			if self._value <= 0.0010:
				self._value = 0.999
			elif self._value < 0.100:
				self._value = 0.001
			else:
				self._value = self._value + (self._delta_sign * delta_float)

		if self._value > 0.999:
			self._value = 0.999
		if self._value < 0.001:
			self._value = 0.001

		self._update_progress_bar()

	def removeProgressBar(self):
		self._clear_progress_bar()

	def setProgressBarColor(self, color_text):
		if isinstance(color_text, str):
			color_text = color_text.lower()
			try:
				c = Color(color_text)
				self._color = c.hex_l
			except ValueError:
				self._color  = EMBEDDED_COLORS[DEFAULT_COLOR_NAME]
		else:
			self._color  = EMBEDDED_COLORS[DEFAULT_COLOR_NAME]

	def getProgressBarColor(self):
		return(self._color)

	def setProgressBarBehavior(self, behavior):
		if isinstance(behavior, str):
			behavior = behavior.lower()
			if behavior in BEHAVIORS:
				self._progressbar_behavior = behavior
			else:
				self._progressbar_behavior = DEFAULT_BEHAVIOR
		else:
			self._progressbar_behavior = DEFAULT_BEHAVIOR

		self._value, self._param_1, self._param_3, self._delta_sign = BEHAVIOR_MAP[self._progressbar_behavior]

	def getBehavior(self):
		return(self._progressbar_behavior)

	def getValue(self):
		return(self._value)
