# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright © 2014 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
from __future__ import unicode_literals
from pkgutil import get_data
from zope.cachedescriptors.property import Lazy
from Products.Five import BrowserView
from gs.core import to_ascii


class Icon(BrowserView):
    iconName = 'browser/images/favicon.ico'  # get_data actually wants '/'

    def __init__(self, context, request):
        super(Icon, self).__init__(context, request)

    @Lazy
    def image(self):
        retval = ''
        # Note:   Binary mode. In Python 3 retval will be a ``bytes`` object,
        #         in Python 2 retval will be a ``str``.
        retval = get_data('gs.content.favicon', self.iconName)
        return retval

    def __call__(self):
        # TODO: Add the x-sendfile suff
        # Note that most of the values below are hard-coded, because the image
        # name and type are also hard coded!
        self.request.RESPONSE.setHeader(to_ascii('Content-Disposition'),
                                    to_ascii('inline; filename=favicon.ico'))
        self.request.RESPONSE.setHeader(to_ascii('Cache-Control'),
                                        to_ascii('public; max-age=1200'))
        self.request.RESPONSE.setHeader(to_ascii('Content-Type'),
                                        to_ascii('image/x-icon'))
        self.request.RESPONSE.setHeader(to_ascii('Content-Length'),
                                        to_ascii(str(len(self.image))))
        retval = self.image
        return retval
