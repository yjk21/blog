#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

#THEME = u'/home/ko/pelican-themes/tuxlite_tbs'
#THEME = u'/home/ko/pelican-themes/pelican-bootstrap3'
#THEME = u'themes/pelican-themes/bootstrap'
THEME = u'themes/pelican-themes/pelican-bootstrap3'
#THEME = u'themes/pelican-themes/pelican-octopress-theme'

AUTHOR = u'yjk21'
SITENAME = u'Learning Machine Learning'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

## Blogroll
#LINKS = (('Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
#
## Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = ['ipynb.markup', 'render_math']


INDEX_SAVE_AS = "blog_index.html"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (("Home","/"), ("Blog","/blog_index.html"))

IGNORE_FILES = ['.#*', '.ipynb_checkpoints']

PYGMENTS_STYLE = "friendly"
