import datetime
import unittest
from spacebodies import forecast


class TestForecast(unittest.TestCase):
    def test_nearest_fc_time(self):
        exeter_fc = forecast.Forecast(50.71, -3.53)
        dt = datetime.datetime(2014, 3, 2, 1, 30)
        self.assertEqual(exeter_fc._nearest_hour(dt),
                         datetime.datetime(2014, 3, 2, 2, 0))
        dt = datetime.datetime(2014, 3, 2, 1, 0)
        self.assertEqual(exeter_fc._nearest_hour(dt), dt)
        dt = datetime.datetime(2014, 3, 2, 1, 29)
        self.assertEqual(exeter_fc._nearest_hour(dt),
                         datetime.datetime(2014, 3, 2, 1, 0))

    def test_integration(self):
        #Will fail without an API key :(
        dt = datetime.datetime.now()
        forecaster = forecast.Forecast(50.71, -3.53)
        weather = forecaster.forecast(dt)
        self.assertIn(weather.cloud_cover, forecast.SKY_STATE)


if __name__ == '__main__':
    unittest.main()
