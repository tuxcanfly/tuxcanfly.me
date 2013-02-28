Month of FOSS contributions - Feb '13
#####################################

:date: 2013-02-28 21:00
:tags: foss, contributions
:category: FOSS
:slug: month-of-foss-contributions-feb-13
:author: Javed Khan
:summary: Round up of my contributions to FOSS in Feb '13

About
=====

I'm documenting my contributions to FOSS every month from now for two purposes:

* As a log of my activity
* To serve as a motivation for further participation

Psst, also for boasting about it, wink wink.

Whoosh
======

While trying to work on django-haystack, I found a bug reported by Zed Shaw
where a search query would crash the search page provided by haystack.

Upon digging into haystack and whoosh, I found that there's a edge case in the
whoosh query parser where passing a query containg a stop word and negative
filter can raise an error (e.g: the query string `?q=-1`). I figured out a simple
fix and submitted a pull request which was promptly accepted.

I was hoping to find something to contribute to haystack and help with the
maintanance, but looks like it will have to wait untill I get some more time.

`362fc299`_

.. _362fc299: https://bitbucket.org/mchaput/whoosh/commits/362fc2999c8cabc51370f433de7402fafd536ec6

django-browserid
================

I have always been a fan of mozilla and django-browserid looks like the perfect
match for me to contribute towards. I tried out the library by going through
the docs and found it to be a breeze. I was able to improve the docs a bit and
triage a few bugs.

I have to say people working on this project are very helpful and
understanding. Looking forward to spending more time on this project in the
future.

`f5fc0f12`_

.. _f5fc0f12: https://github.com/mozilla/django-browserid/commit/f5fc0f124fda1fded862863ef56cab11f23c308d

`b9a17a408`_

.. _b9a17a408: https://github.com/mozilla/django-browserid/commit/b9a17a4088211908de2a17a57668a646555f068a

Conclusion
==========

I really enjoyed working on these projects, and I'm looking forward to speding more time to get more
comfortable with them and contributing even more. Here's to bigger, better things!
