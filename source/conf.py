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
import sys
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
    "myst_parser",
    "sphinxext.opengraph",
    "sphinx_design",
]

myst_enable_extensions = [
    "attrs_inline",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "_static/takanory.jpg"

html_title = "takanory slides"

html_last_updated_fmt = '%Y-%m-%d'

html_css_files = [
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css",
]

html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        # "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

html_theme_options = {
    # https://pradyunsg.me/furo/customisation/footer/#using-icon-packs
    "source_repository": "https://github.com/takanory/slides/",
    "source_branch": "master",
    "source_directory": "source/",
    "footer_icons": [
        {
            "name": "GitHub",
            "url": "https://github.com/takanory/slides",
            "html": "",
            "class": "fa-brands fa-github fa-2x",
        },
    ],
}

# -- for sphinxext-opengraph
ogp_site_url = "https://slides.takanory.net/"
ogp_social_cards = {
    "image": "_static/takanory.jpg",
    "font": "Noto Sans CJK JP",
}
# font settings for macOS and Windows
if sys.platform == "darwin":
    ogp_social_cards["font"] = "Hiragino Maru Gothic Pro"
elif sys.platform == "win32":
    ogp_social_cards["font"] = "MS Gothic"
