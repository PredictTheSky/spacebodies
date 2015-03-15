import unittest
from spacebodies import tle_data


class TestTLEData(unittest.TestCase):
    def test_iss_tle_data(self):
        # Will fail without login and password :(
        tle_getter = tle_data.TLE_getter()
        iss_tle_data = tle_getter.get_data("25544")
        self.assertEqual(iss_tle_data.tle_line0, "ISS (ZARYA)")


if __name__ == '__main__':
    unittest.main()
