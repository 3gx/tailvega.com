#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tailvega'
SITENAME = u'Tailvega'
SITEURL = 'http://www.tailvega.com'


TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('ParallelThinking', 'http://parallelthinking.org'),
          ('Github', 'http://github.com/egaburov'),
          ('Bonsai', 'http://github.com/Treecode'),
          ('Zerohedge', 'http://www.zerohedge.com'),)
#LINKS= ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = ()

THEME = "./bootstrap-jerrykan"
#THEME = "./foundation-default-colours"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ["images"]

PLUGIN_PATHS = ['/Users/evghenii/Work/web/pelican/pelican-plugins']
#PLUGINS = ['latex', 'neighbors', 'summary']
PLUGINS = ['latex', 'summary']
SUMMARY_MAX_LENGTH = 50
