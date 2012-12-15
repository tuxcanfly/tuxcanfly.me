Boost your productivity with compiz
####################################

:date: 2012-12-15 17:00
:tags: compiz
:category: tech
:slug: compiz-productivity
:author: Javed Khan
:summary: Tips for getting the most from compiz

Summary
========

Compiz provides powerful window control features which can be used to improve
daily work flow.


Installation
=============

To start off, you'll need to install the following additional packages:

.. code-block:: none

    compizconfig-settings-manager compiz-plugins-main compiz-plugins-extra


.. warning::
    Before you proceed, you should know that fiddling with compiz is risky and
    will probably cause your desktop session to freeze if something goes wrong.

    `Enable XServer Zap`_ keyboard shortcut and be prepared to use it.


.. _Enable XServer Zap: http://www.ubuntugeek.com/enable-ctrl-alt-backspace-in-ubuntukubuntu-10-04lucid-lynx.html

Preferences
============

Checkout the Preferences options. I prefer the Flat-file configuration backend
as I want to keep all my compiz configuration in a single file and version
control it.

Make sure you create a backup of your current config using the Export option
before you start.

Here's my `compiz config`_ if you want to import it.

.. _compiz config: https://gist.github.com/4296914


Commands
=========

.. figure:: /images/commands.gif
   :align: center
   :alt: Showcasing compiz commands
   :target: /images/commands.gif

   I've mapped <Super>Return to my terminal (urxvt) and
   <Super>e to my editor (gvim)

The Commands plugin gives you a simple way to assign keyboard shortcuts to any
command.

Figure out your most used commands/apps and assign shortcuts to them. No more
wading your way through menus and searching for apps. Some commands I use:

.. code-block:: none

    urxvt -> <Super>Return
    gvim -> <Super>e
    chromium-browser --incognito -> <Shift><Super>w
    nautilus -> <Super>t
    gnome-screensaver-command --lock -> <Super>b


General
=======

.. image:: /images/general.gif
   :align: center
   :alt: Showcasing general key bindings
   :target: /images/general.gif


I find the key-bindings in this section very useful. For example:

.. code-block:: none

    Close Window -> <Super>q
    Toggle Window Maximizes -> <Super>m

Combined with Commands plugin above, this configuration allows you to spawn,
close and maximize/restore your windows all with key-bindings!


Extra WM Actions
=================

.. image:: /images/extra.gif
   :align: center
   :alt: Showcasing extra wm actions
   :target: /images/extra.gif

Ever wanted to turn a window fullscreen but couldn't because the app doesn't
allow it?  Want to keep a window on top?

Extra WM actions provides key-bindings for these features. The mapping I use:

.. code-block:: none

    Toggle Fullscreen -> <Supfer>f


Grid
=====


.. image:: /images/grid.gif
   :align: center
   :alt: Showcasing grid plugin
   :target: /images/grid.gif

Grid provides a window tiling feature with intuitive key-bindings. It's great
for people coming from a tiling window manager (like me).


Desktop Wall/Cube
==================

.. image:: /images/desktops.gif
   :align: center
   :alt: Showcasing desktop wall
   :target: /images/desktops.gif

Both plugins provide an intuitive UI for multiple workspaces and are very
helpful for multitasking.

I map the Move Left/Right to keys on the home row:

.. code-block:: none

    Move Left -> <Shift><Control><Primary><Super>j
    Move Right -> <Shift><Control><Primary><Super>k

Conclusion
===========

I find compiz's features and customizability very useful and I hope you do too.

Let me know if you know any useful tips in comments.
