#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'tuxcanfly'
SITENAME = u'Does not compute'

DEFAULT_LANG = 'en'
LOCALE = ('en_IN')

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

# Blogroll
LINKS =  (('Pelican', 'http://docs.notmyidea.org/alexis/pelican/'),
          ('Python.org', 'http://python.org'),
          ('Jinja2', 'http://jinja.pocoo.org'),
         )

# Social widget
SOCIAL = (('Github', 'http://github.com/tuxcanfly'),
          ('Twitter', 'http://twitter.com/#!/tuxcanfly'),
          ('Bitbucket', 'http://bitbucket.org/tuxcanfly'),
          ('Google', 'http://plus.google.com/u/0/105411960072575411330/about'),
         )

DEFAULT_PAGINATION = 10
THEME = 'syte'
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [
    'assets',
    'gravatar',
    'related_posts'
]

DISPLAY_PAGES_ON_MENU = True
REVERSE_ARCHIVE_ORDER = True
DEFAULT_DATE_FORMAT = '%B %d, %Y'
FEED_RSS = 'feeds/all.xml'
GRAVATAR = 'http://www.gravatar.com/avatar/aa005848320b65eeb0f3413c6adcead5.png'
AUTHOR_EMAIL = 'tuxcanfly@gmail.com'

DISQUS_SITENAME = 'tuxcanfly-github'
GOOGLE_ANALYTICS = 'UA-37076247-1'

FILES_TO_COPY = (('CNAME', 'CNAME'),)

# Syte theme specific settings
##############################

# HTML related settings
ABOUT = u'Self-conscious life form, currently inhabiting the planet Earth. Writes code for a living.'
SITE_DESCRIPTION = u'Personal website and blog of Jakh Daven aka tuxcanfly.'
SITE_KEYWORDS = u'python, django, tuxcanfly, jakh daven'
WEBASSETS = True

# Links
DISPLAY_HOME_ON_MENU = False
GOOGLE_PLUSONE = True

GITHUB_URL = 'https://github.com/tuxcanfly'

# Social integration
GITHUB_INTEGRATION_ENABLED = True
GITHUB_USERNAME = 'tuxcanfly'
GPLUS_INTEGRATION_ENABLED = True
GPLUS_USERNAME = '105411960072575411330'
GPLUS_API_ACCESS = 'AIzaSyDB2JaMR42m43sJ06IYZV0s6H1JI4WyZT0'
TWITTER_INTEGRATION_ENABLED = True
TWITTER_USERNAME = 'tuxcanfly'
BITBUCKET_INTEGRATION_ENABLED = True
BITBUCKET_USERNAME = 'tuxcanfly'
CONTACT = u'tuxcanfly@gmail.com'
