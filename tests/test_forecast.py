import datetime
import unittest
import os

from spacebodies import forecast


class TestForecast(unittest.TestCase):
    def test_nearest_fc_time(self):
        api_key = os.getenv('FORECAST_KEY', '')
        exeter_fc = forecast.Forecast(api_key, 50.71, -3.53)
        dt = datetime.datetime(2014, 3, 2, 1, 30)
        self.assertEqual(exeter_fc._nearest_hour(dt),
                         datetime.datetime(2014, 3, 2, 2, 0))
        dt = datetime.datetime(2014, 3, 2, 1, 0)
        self.assertEqual(exeter_fc._nearest_hour(dt), dt)
        dt = datetime.datetime(2014, 3, 2, 1, 29)
        self.assertEqual(exeter_fc._nearest_hour(dt),
                         datetime.datetime(2014, 3, 2, 1, 0))

    def test_integration(self):
        api_key = os.getenv('FORECAST_KEY', '')
        dt = datetime.datetime.now()
        forecaster = forecast.Forecast(api_key, 50.71, -3.53)
        weather = forecaster.forecast(dt)
        self.assertIn(weather.cloud_cover, forecast.SKY_STATE)


if __name__ == '__main__':
    unittest.main()
