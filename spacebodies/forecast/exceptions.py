# -*- coding: utf-8 -*-


class ForecastException(Exception):
    """There was an ambiguous exception that occurred."""


class ForecastNotLoadedError(ForecastException):
    """The forecast wasn't loaded before being requested."""


class ForecastOutOfRangeError(ForecastException):
    """There's no forecast available for that time."""
