Title: Ubuntu as a django development platform
Date: 2010-12-03 10:20
Tags: thats, awesome
Category: yeah
Slug: ubunt-dev
Author: Jakh Daven
Summary: Short version for index and feeds

Ubuntu as a django development platform
==================================

Introduction:
------------

  Hi, I am Javed Khan, also known as tuxcanfly elsewhere on the internets. I have recently joined [agiliq](http://agiliq.com/)
  and am thrilled to be a part of the team.

  This blog post covers the steps I took to convert a fresh ubuntu install to a full fledged django development platform.

Databases:
---------
  Mysql 
    sudo apt-get install mysql-server mysql-client python-mysqldb
  Postgresql 
    sudo apt-get install postgresql
  Sqlite
    sudo apt-get install sqlite python-sqlite

Version Control:
---------------
  Git  
[need help setting up git with github?](http://help.github.com/) 
    sudo apt-get install git-core git-gui git-svn
  Svn 
    sudo apt-get install subversion rapidsvn meld
  meld is a diff/merge tool that can be used with rapidsvn  
  [http://meld.sourceforge.net/](http://meld.sourceforge.net/)

  Mercurial
    sudo apt-get install mercurial mercurial-git hgsvn

IDEs:
-----
  WingIDE: not free, heavy on resources (reminds me of visual studio)  
  [http://www.wingware.com/downloads](http://www.wingware.com/downloads)

  Eclipse 
    sudo apt-get install eclipse
  Pydev for eclipse: better than WingIDE but still resource intensive
  [http://pydev.org/download.html](http://pydev.org/download.html)

  Gedit: can be quite handy for quickly editing files but somewhat lacking on decent plugins  
  gedit plugins: 
    sudo apt-get install gedit-plugins
  gedit file search plugin  
  [http://github.com/oliver/gedit-file-search](http://github.com/oliver/gedit-file-search)
  
  gedit autocomplete plugin  
  [http://github.com/nagaozen/gedit-plugin-autocomplete/](http://github.com/nagaozen/gedit-plugin-autocomplete/)

  gedit pyflakes support  
  [http://code.google.com/p/geditchecker/](http://code.google.com/p/geditchecker/)

  vim 
    sudo apt-get install vim vim-gtk vim-addon-manager vim-scripts
  django with vim:  
  [http://code.djangoproject.com/wiki/UsingVimWithDjango](http://code.djangoproject.com/wiki/UsingVimWithDjango)

  pida: reuses a lot of vim and its addons, lighter than most IDEs 
    sudo apt-get install pida  
  [http://pida.co.uk/](http://pida.co.uk/)

Tools:
------
  ipython: handy python shell 
    sudo apt-get install ipython
  bpython: another python shell, more interative
    sudo apt-get install bpython
  pyflakes code cheker: checks your code on the fly while editing, shows syntax errors, unused variables etc, useful tool to avoid n00bish mistakes 
    sudo apt-get install pyflakes
  vim plugin for pyflakes  
  [http://www.vim.org/scripts/script.php?script_id=2441](http://www.vim.org/scripts/script.php?script_id=2441)

  Omni completion with vim: very useful, somewhat like intellisense of visual studio  
  [http://vim.wikia.com/wiki/Omni_completion](http://vim.wikia.com/wiki/Omni_completion)

  Code completion with vim: python specific code completion  
  [http://www.vim.org/scripts/script.php?script_id=850](http://www.vim.org/scripts/script.php?script_id=850) 

  python debugger: remote debugger for python, can be used with any IDE, better than pdb from what I have heard 
    sudo apt-get install winpdb
  Debugging django:  
  [http://code.djangoproject.com/wiki/DebuggingDjangoWithWinpdb](http://code.djangoproject.com/wiki/DebuggingDjangoWithWinpdb)

  refactoring tool: haven't used it yet, but goes with vim/pida
    sudo apt-get install python-rope

  virtualenv, easy_install, pip: python package management
    sudo apt-get install python-setuptools
    sudo easy_install pip virtualenv virtualenvwrapper

  python-imaging: imaging library for python with jpeg and freetype support (previously known as PIL)
    sudo apt-get install libjpeg62 libjpeg-dev libfreetype6 libfreetype6-dev python-imaging

  python-crypto: 
    sudo apt-get install python-crypto

Communication:
--------------
  Dropbox  
  [https://www.dropbox.com/downloading?os=lnx](https://www.dropbox.com/downloading?os=lnx)

  Skype 
    sudo apt-get install skype

Django:
-------
  Django, of course  
  [http://www.djangoproject.com/download/](http://www.djangoproject.com/download/)

Suggestions:  
------------
  I am vim addict, so I was inclined towards making vim work with python. I have tried out a bunch of IDEs but I think I'll go with Pida + vim (let the editor wars begin!)

Do you have a virtual machine with your most loved tools pre-installed?  
What IDE do you use? (Vim is better, problem?)  
Am I missing something cool?  
Did you watch the latest futurama episode?  
Let me know :)
