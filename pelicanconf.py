#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Fabian Geiger'
SITENAME = 'Fabian Geiger'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Berlin'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = False
CSS_FILE = 'tailwind.css'

MARKUP = ("md")#, "ipynb")
# from pelican_jupyter import markup as nb_markup
THEME = 'theme'
PLUGIN_PATHS = ['plugins']
PLUGINS = ['gallery']#, nb_markup]
# IPYNB_MARKUP_USE_FIRST_CELL = True

GALLERY_PATH = 'images/gallery'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

DIRECT_TEMPLATES = ['index', 'archives', 'articles']

ARTICLES_SAVE_AS = 'articles/index.html'

DEFAULT_DATE_FORMAT = '%b %d, %Y'

IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_USE_METACELL = True

import datetime
JINJA_GLOBALS = {'current_year': datetime.datetime.now().year}
