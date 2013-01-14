Testing
#######

:date: 2013-01-15 17:00
:tags: ubuntu, editorize, project
:category: project
:slug: announcing-editorize-beta
:author: Javed Khan
:summary: Editorize is a Ubuntu app I've been working on during the past few weekends

Summary
========

Editorize summons up your favorite text editor with a global shortcut so that
you can edit your text the way you want it. Close the file and the text
automagically gets pasted in to the text field you were editing.

Editorize is in beta and needs some bugfixes/cleanup before it can be
considered stable.

Installation
=============

The easiest way to install editorize is by `using the ppa`_:

.. code-block:: none

    sudo apt-add-repository ppa:tuxcanfly/editorize

.. _using the ppa: https://launchpad.net/~tuxcanfly/+archive/editorize

After that, updated and install the `editorize` package:

.. code-block:: none

    sudo apt-get update
    sudo apt-get install editorize

Source packages are available from the `launchpad project page`_.

.. _launchpad project page: https://launchpad.net/editorize

Now you should be able to launch the app from the start menu / dash or using
the command `editorize`

Usage
=====

The default global keyboard shortcut for launching your default text editor is:

.. code-block:: none

    <Ctrl><Alt>i

Both the shortcut and text editor can be customized from the `Preferences` menu
of the App Indicator.

Just go to a text input field on any app and use the above keyboard shortcut
and your text editor should pop open. Now enter your text, save and close the
editor. The input text should get copied to the app.


Help/Bugs:
==========

Please report `bugs on launchpad`_

.. _bugs on launchpad: https://bugs.launchpad.net/editorize
