
"""
.. module:: pyqtlineeditprogressbar

.. moduleauthor: E.R. Uber <eruber@gmail.com>


**PyQtLineEditProgressBar**

This module subclasses Qt's QtLineEdit widget to manage a progress bar
that is displayed as the background color of the QtLineEdit widget.

REFERENCE
---------
The idea for this package came from a `discussion on StackOverflow <https://stackoverflow.com/questions/36972132/how-to-turn-qlineedit-background-into-a-progress-bar>`_.

GPL LICENSE
-----------
This file is part of the PyQtLineEditProgressBar package.

PyQtLineEditProgressBar is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PyQtLineEditProgressBar is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PyQtLineEditProgressBar in the file named LICENSE. If not, 
see <https://www.gnu.org/licenses/>.

COPYRIGHT (C) 2019-2020 E.R. Uber (eruber@gmail.com)

Class PyQtLineEditProgressBar
-----------------------------

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
DEFAULT_COLOR_PURPLE = '#e4b7ff'   # A pastel purple

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
		"""Constructor for the PyQtLineEditProgressBar Class

		Parameters
		----------
		contents : str, optional
		  Text displayed in the LineEdit widget (optional, can be set later with setText() method).

		parent : widget reference, optional
		  The parent widget.

		read_only : bool, optional
		  Defaults to True which makes the LineEdit widget read only.

		progressbar_color : str, optional
		  This must be a string describing a color, such as #1435fe. This field 
		  is validated using the `colour package <https://pypi.org/project/colour/>`_. 
		  Any color specifier accepted by **colour** will pass input validation.

		  If you're not feeling creative enough to specify your own custom color via
		  the **progressbar_color** parameter, there are six built-in color constants 
		  that can be specified here:

		    **pyqtlineeditprogressbar.DEFAULT_COLOR_GREEN**
		    **pyqtlineeditprogressbar.DEFAULT_COLOR_RED**
		    **pyqtlineeditprogressbar.DEFAULT_COLOR_ORANGE**
		    **pyqtlineeditprogressbar.DEFAULT_COLOR_BLUE**
		    **pyqtlineeditprogressbar.DEFAULT_COLOR_YELLOW**
		    **pyqtlineeditprogressbar.DEFAULT_COLOR_PURPLE**

		  If not specified, **DEFAULT_COLOR_GREEN**, is used.

		  See the :ref:`intro_label` for a visual of the colors.

		behavior : str, optional
		  A rather complicated looking string that identifies one of the four possible
		  behaviors of the progress bar:

		  	**pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_LEFT_TO_RIGHT**
			**pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT**
			**pyqtlineeditprogressbar.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT**
			**pyqtlineeditprogressbar.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT**

		  See the :ref:`intro_label` for a visual of the above four behaviors.

		text_for_bounding_rect : str, optional
		  If you have trouble in layout sizing the LineEdit widget's width, and the 
		  contents of this LineEdit widget have a fixed format, then this parameter 
		  may be specified to be used by the overridden sizeHint() method to access
		  the Qt Font Metrics sub-system to specify a width width for the font 
		  being used. For example:

		  	text_for_bounding_rect=" 888/888 [88] "

		  If not specified, then the standard Qt sizeHint() is called.


		Returns
		-------
		PyQtLineEditProgressBar object
			An initialized PyQtLineEditProgressBar object with all the power
			of a normal QLineEdit widget plus a progressbar!!

		"""
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
		"""This overrides QLineEdit's sizeHint() method only if the constructor
		parameter **text_for_bounding_rect** is specified. In which case the
		**text_for_bounding_rect** is used to produce a bounding rectangle that is
		used to return a QSize item from sizeHint(); otherwise, Qt's standard
		sizeHint() method is called.

		Parameters
		----------
		None
		  Nothing

		Returns
		-------
		QSize object
		  The width, height size hint for the PyQtLineEditProgressBar widget.

		"""
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
		"""This is the method that needs to be called periodically to update
		the LineEdit's progressbar.

		Parameters
		----------
		delta_float : float
		  A float that must be between 0.0 and 1.0. Represents the incremental
		  progress of the progress bar for a single progress bar update cycle.

		  For example, if the progress bar represents 6 seconds of work and its
		  updated every second, then delta_float = 1/6.

		Returns
		-------
		None
		  Nothing
		"""

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
		"""This method removes the ProgressBar from the LineEdit background.

		Parameters
		----------
		None
		  Nothing

		Returns
		-------
		None
		  Nothing
		"""
		self._clear_progress_bar()

	def setProgressBarColor(self, color_text):
		"""Iniitalize the color used for the ProgressBar.

		Parameters
		----------
		color_text : str
		  A string describing a color value that is verifiable by the `colour package <https://pypi.org/project/colour/>`_. 

		Returns
		-------
		None
		  Nothing

		Note
		----
		  If this method detects an invalid **color_text** parameter has been specified, the color will be set to the default color
		  which is **pyqtlineeditprogressbar.DEFAULT_COLOR_GREEN**.
		"""
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
		"""Returns the color value associated with the ProgressBar."""
		return(self._color)

	def setProgressBarBehavior(self, behavior):
		"""Configures the behavior of the ProgressBar based on the value of the **behavior** parameter.


		Parameters
		----------
		behavior: str
		  Must be one of four constant string values that describe the behavior of the ProgressBar:

			**pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_LEFT_TO_RIGHT**
			**pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT**
			**pyqtlineeditprogressbar.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT**
			**pyqtlineeditprogressbar.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT**

		Returns
		-------
		None
		  Nothing

		Note
		----
		If the behavior is not one of the four acceptable values, it will be set to the default
		value of **pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_LEFT_TO_RIGHT**.

		"""
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
		"""Returns the how the ProgressBar is configured to behave.

		Parameters
		----------
		None
		  Nothing

		Returns
		-------
		str
		  A string describing how the ProgressBar is configured to behave. It will
		  be one four string values:

		  	**pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_LEFT_TO_RIGHT**
			**pyqtlineeditprogressbar.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT**
			**pyqtlineeditprogressbar.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT**
			**pyqtlineeditprogressbar.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT**

		"""
		return(self._progressbar_behavior)

	def getValue(self):
		"""Returns the current value of the ProgressBar, which is between 0.0 and 1.0.

		Parameters
		----------
		None
		  Nothing

		Returns
		-------
		float
		  Current value of the ProgressBar, between 0.0 and 1.0.
		"""
		return(self._value)
