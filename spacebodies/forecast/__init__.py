# -*- coding: utf-8 -*-

"""
forecast
~~~~~~~~

A client for Forecast.io which loads a full 7-day hourly forecast, for when
you're likely to query the full set in one go.
"""

from .forecast import Forecast, Weather
from .forecast import ForecastOutOfRangeError, ForecastNotLoadedError
