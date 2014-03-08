import datetime, forecast

import unittest


class TestForecast(unittest.TestCase):

    def test_nearest_fc_time(self):
        exeter_fc = forecast.Forecast(50.71, -3.53)
        dt = datetime.datetime(2014, 3, 2, 1, 30)
        self.assertEqual(exeter_fc._nearest_hour(dt),
                datetime.datetime(2014,3, 2, 2, 0))
        dt = datetime.datetime(2014, 3, 2, 1, 0)
        self.assertEqual(exeter_fc._nearest_hour(dt), dt)
        dt = datetime.datetime(2014, 3, 2, 1, 29)
        self.assertEqual(exeter_fc._nearest_hour(dt),
                datetime.datetime(2014, 3, 2, 1, 0))

    def test_integration_for_fun(self):
        dt = datetime.datetime.now()
        forecaster = forecast.Forecast(50.71, -3.53)
        weather = forecaster.forecast(dt)
        """ Will fail - just want to check I get something! """
        self.assertEqual(weather.cloud_cover, 'flamy')

        
if __name__ == '__main__':
    unittest.main()
