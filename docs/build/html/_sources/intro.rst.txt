.. ############################################################################
   This file contains reStructuredText, please do not edit it unless you are
   familar with reStructuredText markup as well as Sphinx specific markup.

   For information regarding reStructuredText markup see
      http://sphinx.pocoo.org/rest.html

   For information regarding Sphinx specific markup see
      http://sphinx.pocoo.org/markup/index.html

   ############################################################################

.. ############################################################################
   Copyright 2020 E.R. Uber (eruber@gmail.com)
   ############################################################################

.. ########################### SECTION HEADING REMINDER #######################
   # with overline, for parts
   * with overline, for chapters
   =, for sections
   -, for subsections
   ^, for subsubsections
   ", for paragraphs

.. -----------------------------------------------------------------------------

.. _intro_label: 

Introduction
============

A PyQtLineEditProgressBar widget object can have its progressbar color and its progressbar behavior
configured either at the time of the constructor call or by using method calls after a
PyQtLineEditProgressBar widget has been initialized by the constructor call.

Configuring Color
-----------------
You may specify a custom color or choose between one of six built-in colors.

.. note:: When specifying a custom color, any color specification that the `colour package <https://pypi.org/project/colour/>`_
  can handle is legal.

The built-in colors are accessible via constants in the **pyqtlineeditprogressbar** module like this::

    import pyqtlineeditprogressbar as lepbar

    built_in_color_1 = lepbar.DEFAULT_COLOR_GREEN
    built_in_color_2 = lepbar.DEFAULT_COLOR_RED
    built_in_color_3 = lepbar.DEFAULT_COLOR_ORANGE
    built_in_color_4 = lepbar.DEFAULT_COLOR_BLUE
    built_in_color_5 = lepbar.DEFAULT_COLOR_YELLOW
    built_in_color_6 = lepbar.DEFAULT_COLOR_PURPLE

.. image:: _static/builtin_color_table.png
   :align: center

.. note:: If no color is specified, the default is **DEFAULT_COLOR_GREEN**.

Configuring Color When Calling Constructor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Choosing a progressbar color when calling the constructor looks like this::

    import pyqtlineeditprogressbar as LEPBAR
    from pyqtlineeditprogressbar import PyQtLineEditProgressBar

    lepbar = PyQtLineEditProgressBar(progressbar_color=LEPBAR.DEFAULT_COLOR_PURPLE)

Configuring Color via Method Call
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Choosing a progressbar color can be delayed until after the constructor call like this::

    import pyqtlineeditprogressbar as LEPBAR
    from pyqtlineeditprogressbar import PyQtLineEditProgressBar

    lepbar = PyQtLineEditProgressBar()

    lepbar.setProgressBarColor(LEPBAR.DEFAULT_COLOR_PURPLE)

Configuring Behavior
--------------------
You may specify one of four possible progressbar behaviors as described below.

Each behavior defines three aspects of the progressbar:

    1. How the progressbar appears when initialized -- empty or full
    2. How the progressbar reacts to an update -- fills or empties
    3. The direction the progressbar fills or empties -- from left to right, or from right to left

The four progressbar behaviors are defined by for string constants::

    import pyqtlineeditprogressbar as LEPBAR

    behavior_1 = LEPBAR.STARTS_EMPTY_FILLS_LEFT_TO_RIGHT
    behavior_1 = LEPBAR.STARTS_EMPTY_FILLS_RIGHT_TO_LEFT
    behavior_1 = LEPBAR.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT
    behavior_1 = LEPBAR.STARTS_FULL_EMPTIES_RIGHT_TO_LEFT

.. image:: _static/behaviors.gif
   :align: center

.. note:: If no behavior is specified, the default is **STARTS_EMPTY_FILLS_LEFT_TO_RIGHT**.


Configuring Behavior When Calling Constructor
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Choosing a progressbar behavior when calling the constructor looks like this::

    import pyqtlineeditprogressbar as LEPBAR
    from pyqtlineeditprogressbar import PyQtLineEditProgressBar

    lepbar = PyQtLineEditProgressBar(behavior=LEPBAR.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT)

Configuring Behavior via Method Call
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Choosing a behavior can be delayed until after the constructor call like this::

    import pyqtlineeditprogressbar as LEPBAR
    from pyqtlineeditprogressbar import PyQtLineEditProgressBar

    lepbar = PyQtLineEditProgressBar()

    lepbar.setProgressBarBehavior(LEPBAR.STARTS_FULL_EMPTIES_LEFT_TO_RIGHT)


The Demo Program
----------------
The demo program illustrates all the colors (including a custom color) and all the behaviors.
Run it from the root of the project like this::

    python demo.py

Caveat
------
This package uses Qt Palettes and LinearGradients to implement the progressbar in the background color of the LineEdit widget.

If you spend anytime whatsoever reading the Qt documentation on Palettes, it clearly states multiple times that the use of Palettes and Qt Style Sheets should not be mixed.

So its highly likely that if this package is used as part of an application that changes color themes via Qt Style Sheets
there might be compatibility issues.

I would like to understand and solve this issue in the future, if possible.

Further Reading
---------------
For more details see the :ref:`api_label` section.


