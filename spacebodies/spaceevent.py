# -*- coding: utf-8 -*-

"""
spacebodies.spaceevent
---------------------

This module provides a data class for representing a space event.

"""


class SpaceEvent(object):

    """
    Refactoring notes

    too many args: need to wrap space body id attrs into class, as well as
    location and (in future) weather.
    """
    
    def __init__(self, body_id, name, category):
        self.id = body_id
        self.name = name
        self.category = category

    def start(self, start, location):
        self.start = start
        self.start_location = location

    def end(self, end, location):
        self.end = end
        self.end_location = location

    def __str__(self):
        return "%s start %s (%s), end %s (%s)" % (self.name, self.start,
                                                  self.start_location,
                                                  self.end, self.end_location)
