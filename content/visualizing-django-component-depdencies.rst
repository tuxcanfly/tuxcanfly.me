Visualizing Django Component Dependencies
#########################################

:date: 2014-03-09 17:00
:tags: project, django, visualization
:category: project
:slug: visualizing-django-component-dependencies
:author: Javed Khan
:summary: A visualization of dependencies between django components using snakefood, graphviz and dagre, D3.js

.. figure:: |filename|/images/django-dep-graph.png
   :align: center
   :alt: Django dependency graph
   :target: /raw/django-dependencies.html

Problem
=======

Browsing through Django's ideas for GSOC 2014, I came across a `proposal`_ to
reduce coupling and package each component separately. I have often wondered
how complex such a task would be as Django claims and encourages `loose
coupling`_.

So, I tried to naively separate a module such as `django.forms` and found that
it depends on atleast four other modules to just intialize. Similarly trying
out other modules, I found varying complexity in the dependencies most of which
were atleast depedent on `django.apps` for apps and `django.conf` for settings.

I wanted to figure out how complex the dependencies between various modules are
and I started looking at code analysis tools to visualize them. I settled on
Snakefood for generating the dependency graph and dagre-d3 for the rendering.

.. _proposal: https://code.djangoproject.com/wiki/SummerOfCode2014#ReducingcouplinginDjangocomponents
.. _loose coupling: https://docs.djangoproject.com/en/dev/misc/design-philosophies/#loose-coupling

Snakefood
=========

I used `snakefood`_ to get a graphviz dot format representation of the dependencies:

.. _snakefood: http://furius.ca/snakefood/

.. code-block:: none

    sfood django/ --internal | sfood-cluster -f clusters | sfood-graph | dot -o django.dot

here `clusters` is a file containing the modules we want to restrict the dependency level to:

.. code-block:: none

    django/apps
    django/bin
    django/conf
    django/contrib
    django/core
    django/db
    django/dispatch
    django/forms
    django/http
    django/middleware
    django/template
    django/templatetags
    django/test
    django/utils
    django/views

Dagre
=====

Next, I used `dagre-d3`_ to visualize the output:

.. _dagre-d3: https://github.com/cpettitt/dagre-d3

Result
======

Here's `the final result`_

.. _the final result: /raw/django-dependencies.html

Conclusion
==========

Some things that caught my eye:

* `django.template` depends on `django.http` - familiar but probably shouldn't
* `django.forms` depends on `django.db` - again familiar but probably shouldn't
* Cyclic dependency between `django.core` and `django.conf` - maybe unavoidable?

I think most of the coupling stems from the fact that modules assume we have
configured settings and have installed apps. So, decoupling `django.conf` and
`django.apps` could probably be a first step. Decoupling other modules would
require some analysis of the dependency graph and refactoring but overall I'm
hopeful that Django could be broken down into smaller, better components and
allow developers to pick and choose the modules they need.
