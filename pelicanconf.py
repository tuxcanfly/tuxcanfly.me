#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Javed Khan'
SITENAME = 'Does not compute'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('MerkleBlock', 'https://merkleblock.com/'),
        ('Bcoin', 'https://bcoin.io'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/tuxcanfly'),
          ('github', 'https://github.com/tuxcanfly'),)

DEFAULT_PAGINATION = 10

THEME='themes/pelican-blue/'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
AVATAR = "https://www.gravatar.com/avatar/aa005848320b65eeb0f3413c6adcead5?s=128"

STATIC_PATHS = [
    'images',
    'extra/robots.txt',
    'extra/favicon.ico',
    'extra/CNAME',
    'extra/resume.pdf'
]
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/CNAME': {'path': 'CNAME'},
    'extra/resume.pdf': {'path': 'resume.pdf'},
}

SIDEBAR_DIGEST = 'Blockchain Specialist'

FAVICON = '/favicon.ico'

DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_FOOTER = False
DISPLAY_SUMMARY = True

# TWITTER_USERNAME = 'tuxcanfly'

MENUITEMS = (('Blog', '/'),
             ('About', '/pages/about-me.html'),
             ('Resume', '/resume.pdf'),)
