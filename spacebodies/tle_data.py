# -*- coding: utf-8 -*-

"""
spacebodies.tle_data
-----------------------

This module provides latest TLE data from space-track.com

"""
import json
import requests


class TLE_getter(object):

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._api_auth_url = 'https://www.space-track.org/ajaxauth/login'
        self.session = requests.session()
        data = {"identity": self._username, "password": self._password}
        self.session.post(self._api_auth_url, data)

    def get_data(self, id):
        self._api_data_url = 'https://www.space-track.org/basicspacedata/' \
                             'query/class/tle_latest/NORAD_CAT_ID/' \
                             '%s/ORDINAL/1/' % (id)
        r = self.session.get(self._api_data_url)
        self.session.close()
        json_data = json.loads(r.text)[0]
        return TLE_data(json_data)


def _normalize_data_string(data_string):
    return data_string.encode('ascii', 'ignore')


class TLE_data(object):
    """
    Data class to store attrs required for space body's TLE data
    Construct with a space-track.org tle_latest data object.
    """

    def __init__(self, data):
        self.tle_line0 = _normalize_data_string(data['OBJECT_NAME'])
        self.tle_line1 = _normalize_data_string(data['TLE_LINE1'])
        self.tle_line2 = _normalize_data_string(data['TLE_LINE2'])
