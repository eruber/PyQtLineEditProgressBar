# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
# root dir of project is two levels up from where this file lives
sys.path.insert(0, os.path.abspath('../..'))
sys.path.insert(1, os.path.abspath('../pyqtlineeditprogressbar'))
sys.setrecursionlimit(1500)


# -- Project information -----------------------------------------------------

project = 'PyQtLineEditProgressBar'
copyright = '2020, E.R. Uber'
author = 'E.R. Uber'

# The full version, including alpha/beta/rc tags
release = '0.3.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
	'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# The name of the entry point, without the ".rst" extension.
# By convention this will be "index"
#master_doc = "index"

# Disabling google docstring format and turning on Numpy Docstring format
# https://numpydoc.readthedocs.io/en/latest/format.htm
napoleon_google_docstring = False
napoleon_numpy_docstring = True

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
html_logo = "_static/logo.gif"

# https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html
html_theme_options = {
    'logo_only': False,      # Also dislays Project Name above Logo image
    'display_version': True,
    'navigation_depth': 2,
    'prev_next_buttons_location': 'both',
    'style_external_links': True,  # An icon next to external links
    #'style_nav_header_background': '#e6d1e4', 

    # BELOW ARE THE DEFAULTS OF EVERY AVAILABLE OPTION:
    # 'canonical_url': '',
    # 'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
    # 'logo_only': False,      
    # 'display_version': True,      
    # 'prev_next_buttons_location': 'bottom',
    # 'style_external_links': False,
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # # Toc options
    # 'collapse_navigation': True, 
    # 'sticky_navigation': True,   
    # 'navigation_depth': 4,       
    # 'includehidden': True,       
    # 'titles_only': False         
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']