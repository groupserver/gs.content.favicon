======================
``gs.content.favicon``
======================
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``favicon`` for GroupServer
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:Authors: `Michael JasonSmith`_
:Contact: Michael JasonSmith <mpj17@onlinegroups.net>
:Date: 2014-06-27
:Organization: `GroupServer.org`_
:Copyright: This document is licensed under a
  `Creative Commons Attribution-Share Alike 4.0 International License`_
  by `OnlineGroups.Net`_.

Introduction
============

This product defines the *favicon* (also known as *favourite*
*icon,* *page icon,* *webpage icon,* and *shortcut icon*) for
GroupServer.

It provides a `resource directory`_. a viewlet_, and a page_ —
all of which contain `the icon`_ itself.

Resource directory
==================

The resource directory ``favicon-20140624a`` provides the favicon
at different sizes, including an SVG version.

Viewlet
=======

The viewlet ``gs-content-favicon`` viewlet slots into the
``gs.content.layout.interfaces.IFavicon`` viewlet manager. It
provides ``<link>`` and ``<meta>`` elements for the favicon,
Apple iOS touch icons, and Microsoft Windows 8 badges.

Page
====

The *page* ``favicon.ico`` provides the favicon in Microsoft ICO
format. An ICO is actually a *container*. The ``favicon.ico``
file provided by this product contains several PNG images at
different resolutions. It is created by using the ``convert``
utility provided by ImageMagic::

  $ convert gs-logo-16x16.png gs-logo-24x24.png gs-logo-32x32.png gs-logo-48x48.png gs-logo-64x64.png favicon.ico

The icon
========

The icon itself is an interlocking GS, in Helvetica, with the
descender on the ``G`` removed. It was created in Inkscape, and
the Inkscape SVG file is provided by ``gs-logo-orig.svg``.

Acknowledgements
================

Thanks to Audrey Roy for the wonderful `favicon-cheat-sheet`_.

.. favicon-cheat-sheet: https://github.com/audreyr/favicon-cheat-sheet

Resources
=========

- Code repository: https://source.iopen.net/groupserver/gs.content.favicon
- Questions and comments to http://groupserver.org/groups/development
- Report bugs at https://redmine.iopen.net/projects/groupserver

.. _GroupServer: http://groupserver.org/
.. _GroupServer.org: http://groupserver.org/
.. _OnlineGroups.Net: https://onlinegroups.net/
.. _Michael JasonSmith: http://groupserver.org/p/mpj17/
.. _Creative Commons Attribution-Share Alike 4.0 International License:
    http://creativecommons.org/licenses/by-sa/4.0/

..  LocalWords:  favicon IFavicon SVG ico PNG
