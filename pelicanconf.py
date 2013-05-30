#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'tailvega'
SITENAME = u'Tailvega'
SITEURL = ''

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Github', 'http://github.com/egaburov'),
          ('Bonsai', 'http://github.com/Treecode/'),)
#LINKS= ()

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)
SOCIAL = ()

#THEME = "../pelican-themes/fresh"
#THEME = "../pelican-themes/irfan"
#THEME = "../pelican-themes/relapse"
#THEME = "../pelican-themes/sneakyidea"
#THEME = "../pelican-themes/subtle"
#THEME = "../pelican-themes/tuxlite_tbs"
THEME = "./notmyidea"
THEME = "./bootstrap-jerrykan"
#THEME = "./bootstrap2"
#THEME = "../pelican-themes/bootstrap2"

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
