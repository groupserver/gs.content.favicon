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
GroupServer. It provides a `resource directory`_, a viewlet_, and
a page_ — all of which contain `the icon`_ itself.

Resource directory
==================

The resource directory ``favicon-20140624a`` provides the favicon
at different sizes, including an SVG version. It maps onto the
``browser/images`` folder in this product.

Viewlet
=======

The viewlet ``gs-content-favicon`` viewlet slots into the
``gs.content.layout.interfaces.IFavicon`` viewlet manager. It
provides the elements necessary to link to the favicon from all
HTML pages.

HTML 5:
  Two ``<link>`` elements with ``rel="icon"`` attributes::

    <link rel="icon" sizes="any" type="image/svg+xml"
          href="/++resource++favicon-20140624a/gs-logo.svg" />
    <link rel="icon" sizes="256x256" type="image/png"
          href="/++resource++favicon-20140624a/gs-logo-256x256.png" />

Apple iOS:
  One ``<link>`` element, with ``rel="apple-touch-icon"``::

    <link rel="apple-touch-icon" sizes="152x152" type="image/png"
          href="/++resource++favicon-20140624a/gs-logo-152x152.png" />

Microsoft Windows 8:
  Two ``<meta>`` elements for the *badge* (or *tile*)::

    <meta name="msapplication-TileColor" content="#CCCCCC" />
    <meta name="msapplication-TileImage"
          content="/++resource++favicon-20140624a/gs-logo-144x144.png" />

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
descender on the ``G`` removed. It was created in Inkscape; the
original Inkscape SVG file is ``gs-logo-orig.svg``, in the same
``browser/images`` directory as the other versions of the icon.

Acknowledgements
================

Thanks to Audrey Roy for the wonderful `favicon-cheat-sheet`_.

.. _favicon-cheat-sheet: https://github.com/audreyr/favicon-cheat-sheet

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
