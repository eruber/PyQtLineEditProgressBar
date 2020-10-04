import sys

from setuptools import setup

if sys.version_info[0] < 3:
	sys.exit('Error: Python 3.x is required.')

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='pyqtlineeditprogressbar',
		version='0.3.4',
		description='A custom PyQt widget that places a configurable progress bar in the background of a QLineEdit widget.',
		url='http://github.com/eruber/pyqtlineeditprogressbar',
		download_url="https://github.com/eruber/PyQtLineEditProgressBar/archive/v0.3.0.tar.gz",
		author='E.R. Uber',
		author_email='eruber@gmail.com',
		long_description=long_description,
		long_description_content_type='text/markdown',
		license='GPLv3',
		packages=['pyqtlineeditprogressbar'],
		install_requires=[
		'PyQt5>=5.14.0',
		'colour>=0.1.5',
		],
		classifiers = [
			'Development Status :: 4 - Beta',
			'Intended Audience :: Developers',
			'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
			'Programming Language :: Python :: 3.7',
			'Programming Language :: Python :: 3.8',
		],
	)
