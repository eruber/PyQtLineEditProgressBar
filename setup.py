from setuptools import setup

setup(name='pyqtlineeditprogressbar',
	  version='0.3.0',
	  description='A custom PyQt widget that places a configurable progress bar in the background of a QLineEdit widget.',
	  url='http://github.com/eruber/pyqtlineeditprogressbar',
	  author='E.R. Uber',
	  author_email='eruber@gmail.com',
	  license='GPLv3',
	  packages=['pyqtlineeditprogressbar'],
	  install_requires=[
	  	'PyQt5>=5.14.0',
	  	'colour>=0.1.5',
	  ],
	  zip_safe=False)
