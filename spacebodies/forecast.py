import datetime, forecastio

SKY_STATE = ['clear', 'scattered cloud', 'cloudy with breaks', 'cloudy']

class Forecast():

    """
    For an event, we need to get a forecast from the api for the datetime.
    For the specified timestamp, find the closest appropriate forecast and
    pull out the required forecast attrs.
    """
    
    def __init__(self, lat, lon):
        self._api_key = '35753e2516b4b687b9d7eedc924069bd'
        self.lat = lat
        self.lon = lon

    def forecast(self, event_dt):
        nearest_forecast_time = self._nearest_hour(event_dt)
        forecast_day = forecastio.load_forecast(self._api_key,
                self.lat, self.lon, nearest_forecast_time)
        hourly_forecast = forecast_day.hourly()
        for hour in hourly_forecast.data:
            if hour.time == nearest_forecast_time:
               return Weather(hour)
        return

    def _nearest_hour(self, dt):
        cutoff = datetime.datetime(dt.year, dt.month, dt.day, 23, 30)
        if dt >= cutoff:
            """ We'll use tomorrow's 00Z forecast. """
            return datetime.datetime(dt.year, dt.month, dt.day, 0, 0) + \
                   datetime.timedelta(1)
        if dt.minute >= 30:
            return datetime.datetime(dt.year, dt.month, dt.day, dt.hour, 0) + \
                   datetime.timedelta(hours=1)
        return datetime.datetime(dt.year, dt.month, dt.day, dt.hour, 0)


class Weather():

    """
    Data class to store attrs required for space event forecasts.
    Construct with a forecastio data point object.
    """

    def __init__(self, forecast_datapoint):
        self.cloud_cover = self._cloud_to_summary(forecast_datapoint.cloudcover)
        self.chance_of_prep = forecast_datapoint.precipProbability
        self.temperature = forecast_datapoint.temperature
        self.feels_like_temperature = forecast_datapoint.apparentTemperature
        

    def _cloud_to_summary(self, cloud_fraction):
        if cloud_fraction < .1:
            return SKY_STATE[0]
        if cloud_fraction < .4:
            return SKY_STATE[1]
        if cloud_fraction < .75:
            return SKY_STATE[2]
        return SKY_STATE[3]
