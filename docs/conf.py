
import os
import sys


# Add your project root so Sphinx can find your modules
sys.path.insert(0, os.path.abspath(".."))


# Project info

project = "Playground"
author = "KZ"


# General config

extensions = [
    "sphinx.ext.autodoc",      # pull docstrings into docs
    "sphinx.ext.napoleon",     # support Google/NumPy docstrings
    "sphinx.ext.viewcode",  # add links to source code
    "sphinx.ext.autosummary" ,  
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# Options 

html_theme = "sphinx_rtd_theme"  # simple default; easy to change later
html_static_path = ["_themes/sphinx_rtd_theme/"]
html_show_source_link = False


# Autodoc
autodoc_default_options = {
    "members": True,
    "undoc-members": False,
    "private-members": False,
    "show-inheritance": True,
}

autodoc_typehints = "description"
autosummary_generate = True