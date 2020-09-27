# PyQtLineEditProgressBar
 A custom PyQt widget that creates a configurable progress bar as the background color of a QLineEdit widget.

This widget sub-classes the [QLineEdit](https://doc.qt.io/qtforpython/PySide2/QtWidgets/QLineEdit.html) widget to add a progress bar as its background and 
provide the following features:

- Six built in pastel colors to configure as the progress bar color or specify your own custom color
- Select  from one of four progress bar behaviors as listed and shown below:
	- Start Empty and Fill from Left to Right
	- Start Empty and Fill from Right to Left
	- Start Full and Empty from Left to Right
	- Start Full and Empty from Right to Left

      ![Demo GIF](https://imgur.com/BhvKrkd.gif)

# Dependencies #
PyQtLineEditProgressBar depends on the following third-party packages:

- [PyQt5](https://pypi.org/project/PyQt5/)

- [colour](https://pypi.org/project/colour/)


# Installation #
Via Python's package installer:

	pip install PyQtLineEditProgressBar

or from the package source as a user:

	pip install . 

or from the package source as a developer:

	pip install -e .

# Testing #
Once installed the **demo.py** file can be executed to demonstrate usage:

	python demo.py

The results of executing this file should look similar to the animation in the introduction above

# License #

PyQtLineEditProgressBar is GPLv3 licensed. See LICENSE file for details.

# Attributions #
This code is based off of a discussion at [StackOverflow](https://stackoverflow.com/questions/36972132/how-to-turn-qlineedit-background-into-a-progress-bar).

