import unittest
import os
from spacebodies import tle_data


class TestTLEData(unittest.TestCase):
    def test_iss_tle_data(self):
        username = os.getenv('SPACETRACK_USERNAME', '')
        password = os.getenv('SPACETRACK_PASSWORD', '')

        tle_getter = tle_data.TLE_getter(username, password)
        iss_tle_data = tle_getter.get_data("25544")
        self.assertEqual(iss_tle_data.tle_line0, "ISS (ZARYA)")


if __name__ == '__main__':
    unittest.main()
