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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'takanory slides'
copyright = '2022, takanory'
author = 'takanory'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_revealjs',
    "sphinx_fontawesome",
    "sphinxext.opengraph",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["**/env"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- for sphinxext-opengraph
ogp_site_url = "https://slides.takanory.net/"
ogp_image = "https://slides.takanory.net/_static/takanory.jpg"
ogp_type = "article"

# -- for revealjs --------
# https://github.com/attakei/sphinx-revealjs/blob/master/demo/revealjs4/conf.py

# https://revealjs.com/themes/
# revealjs_google_fonts = ["M PLUS 1p"]
# revealjs_google_fonts = ["Noto Sans JP"]
revealjs_style_theme = "white"
revealjs_script_conf = {
    "controls": True,
    "progress": False,
    "history": True,
    "center": True,
    "transition": "none",
    # "navigationMode": "linear",
}
revealjs_script_plugins = [
    {
        "name": "RevealNotes",
        "src": "revealjs4/plugin/notes/notes.js",
    },
    {
        "name": "RevealHighlight",
        "src": "revealjs4/plugin/highlight/highlight.js",
    },
    {
        "name": "RevealMath",
        "src": "revealjs4/plugin/math/math.js",
    },
]
revealjs_static_path = html_static_path
revealjs_css_files = [
    "https://netdna.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    "revealjs4/plugin/highlight/zenburn.css",
    'slides.css',
]