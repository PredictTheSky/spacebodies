# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import unittest
import httpretty
import os

from utils import fixture

from spacebodies import tle_data


class TestTLEData(unittest.TestCase):
    @httpretty.activate
    def test_iss_tle_data(self):
        httpretty.register_uri(httpretty.POST,
                               'https://www.space-track.org/ajaxauth/login',
                               body="")

        url = 'https://www.space-track.org/basicspacedata/query/class/' \
              'tle_latest/NORAD_CAT_ID/25544/ORDINAL/1/'
        httpretty.register_uri(httpretty.GET, url,
                               body=fixture('spacetrack_tle.json'))

        username = os.getenv('SPACETRACK_USERNAME', '')
        password = os.getenv('SPACETRACK_PASSWORD', '')

        tle_getter = tle_data.TLE_getter(username, password)
        iss_tle_data = tle_getter.get_data("25544")
        self.assertEqual(iss_tle_data.tle_line0, "ISS (ZARYA)")


if __name__ == '__main__':
    unittest.main()
