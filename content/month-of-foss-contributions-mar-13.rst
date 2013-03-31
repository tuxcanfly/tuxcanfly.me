Month of FOSS contributions - Mar '13
#####################################

:date: 2013-03-31 21:00
:tags: foss, contributions
:category: FOSS
:slug: month-of-foss-contributions-mar-13
:author: Javed Khan
:summary: Round up of my contributions to FOSS in Mar '13

About
=====

Stuff that I contributed to Open Source in Mar '13.

Django
======

I debugged an issue in django `ModelChoiceField` and `ModelMultipleChoiceField`
which was causing model forms to be validated even though they weren't changed.
The problem was that `has_changed` was comparing an `object_id` or list of
`ids` with an instance or queryset.

Even though the fix was a part of another branch, the tests I had proposed were
included in the commit.

`3318595c`_

`Pull request`_

.. _3318595c: https://github.com/django/django/commit/3318595c0bfeda9f6bae8aa11dda68647ae55fde

.. _Pull request: https://github.com/django/django/pull/660

Vimux-django-tests
==================

This is a pet project that I started to make it easier to run individual django
tests from within vim.

`Vimux-django-tests`_

.. _Vimux-django-tests: https://github.com/tuxcanfly/vimux-django-tests
