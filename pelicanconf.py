#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

THEME = u'../pelican-themes/pelican-bootstrap3'

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

JINJA_ENVIRONMENT = {
            'extensions': ['jinja2.ext.i18n'],
        }

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

#PLUGIN_PATHS = ['../', '../pelican-plugins']
PLUGIN_PATHS = ['../', './pelican-plugins']
PLUGINS = ['pelican-ipynb.markup', 'render_math','sitemap', 'i18n_subsites']


INDEX_SAVE_AS = "blog.html"

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
MENUITEMS = (("Home","/"), ("Blog","/blog.html"), ("Projects", "/projects.html"), ("CV","https://github.com/yjk21/blog/raw/master/content/files/cv.pdf"))

IGNORE_FILES = ['.#*', '.ipynb_checkpoints']

PYGMENTS_STYLE = "friendly"

GOOGLE_ANALYTICS = "UA-83216470-1"

SITEMAP = {
        'format': 'xml',
        'priorities': {
            'articles': 0.5,
            'indexes': 0.5,
            'pages': 0.5
            },
        'changefreqs': {
            'articles': 'monthly',
            'indexes': 'daily',
            'pages': 'monthly'
            },
        'exclude': ['tag/', 'category/']
        }
SUMMARY_MAX_LENGTH = 10
STATIC_PATHS=['js']
