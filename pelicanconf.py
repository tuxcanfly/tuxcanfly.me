#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'tuxcanfly'
SITENAME = u'Does not compute'

DEFAULT_LANG = 'en'
LOCALE = ('en_IN',)

TIMEZONE = 'Asia/Kolkata'

SECTIONS = [('Blog', 'index.html'),
        ('Archive', 'archives.html'),
        ('Tags', 'tags.html'),
        ('Projects', 'tag/project.html'),
        ('Talks', 'tag/talk.html'),
        ('About', 'pages/about-me.html')]

DEFAULT_PAGINATION = 10
THEME = 'flasky'
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [
    'assets',
    'gravatar',
    'related_posts'
]

DISPLAY_PAGES_ON_MENU = True
REVERSE_ARCHIVE_ORDER = True
FEED_RSS = 'feeds/all.xml'
GRAVATAR = 'http://www.gravatar.com/avatar/aa005848320b65eeb0f3413c6adcead5.png'
AUTHOR_EMAIL = 'tuxcanfly@gmail.com'

DISQUS_SITENAME = 'tuxcanfly-github'
GOOGLE_ANALYTICS = 'UA-37076247-1'

FILES_TO_COPY = (('CNAME', 'CNAME'),)

# HTML related settings
ABOUT = u'Self-conscious life form, currently inhabiting the planet Earth. Writes code for a living.'
SITE_DESCRIPTION = u'Personal website and blog of Jakh Daven aka tuxcanfly.'
SITE_KEYWORDS = u'python, django, tuxcanfly, jakh daven'
WEBASSETS = True

GITHUB_URL = 'https://github.com/tuxcanfly'
LINKEDIN_URL = 'http://in.linkedin.com/tuxcanfly'
TWITTER_USERNAME = 'tuxcanfly'

DEFAULT_CATEGORY = 'Uncategorized'
DATE_FORMAT = {
    'en_IN': '%A, %d %B %Y',
}
DEFAULT_DATE_FORMAT = '%A, %d %B %Y'
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True

CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

OUTPUT_PATH = 'output'
GOOGLE_ANALYTICS_ACCOUNT = 'UA-37076247-1'

MAIL_USERNAME = 'tuxcanfly'
MAIL_HOST = 'gmail.com'

STATIC_PATHS = ["images"]
