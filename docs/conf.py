"""Sphinx configuration."""
project = "Scikit Jade"
author = "Timothy H. Click, Ph.D."
copyright = "2022, Timothy H. Click, Ph.D."
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
