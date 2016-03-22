# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2016 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals, print_function
from mock import (patch, PropertyMock, MagicMock, )
from unittest import TestCase
from gs.content.favicon.icon import Icon


class TestIcon(TestCase):
    'Test the ``Icon`` class'
    notImage = b'This is not an image.'

    @patch.object(Icon, 'image', new_callable=PropertyMock)
    def test_call(self, m_image):

        m_image.return_value = self.notImage
        request = MagicMock()
        i = Icon(MagicMock(), request)
        r = i()

        self.assertEqual(self.notImage, r)
        request.RESPONSE.setHeader.assert_any_call(b'Content-Length', b'21')

    @patch('gs.content.favicon.icon.get_data')
    def test_image(self, m_get_data):
        m_get_data.return_value = self.notImage
        i = Icon(MagicMock(), MagicMock())
        r = i.image

        self.assertEqual(self.notImage, r)
        m_get_data.assert_called_once_with('gs.content.favicon', 'browser/images/favicon.ico')
