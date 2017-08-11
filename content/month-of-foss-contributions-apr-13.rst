Month of FOSS contributions - Apr '13
#####################################

:date: 2013-05-5 21:00
:tags: foss, contributions
:category: FOSS
:slug: month-of-foss-contributions-apr-13
:author: Javed Khan
:summary: Round up of my contributions to FOSS in Apr '13

About
=====

Stuff that I contributed to Open Source in Apr '13.

Merchant
========

django-merchant is a Django app to accept payments from various payment
processors via Pluggable backends.

I'm glad to have the chance the contribute to merchant again; I was previously
involved in the design as well as eWay and bitcoin backends.

I have added a Continuous Integration build for merchant over at `Travis`_

What's more, the `demo`_ is less of an eyesore now; it has been revamped using
bootstrap

.. _Travis: https://travis-ci.org/agiliq/merchant

.. _demo: http://merchant.agiliq.com

We received contributions to Braintree, Google Checkout, and eWay backends
which I have reviewed and merged.

Overall, it’s been a really good month for django-merchant, here's to hoping
this continues.

.. figure:: |filename|/images/merchant-progress.png
   :align: center
   :alt: Merchant Progress
   :target: |filename|/images/merchant-progress.png

   GitHub pulse for django-merchant
