# -*- coding: utf-8 -*-

"""
bodies
------

This module provides the subclasses of SpaceBody; these are the classes which
handle the calculation for each different type of astronomical object.

See the Abstract Base Class, SpaceBody on the required elements.

"""

import ephem

from .spacebody import SpaceBody

STAR_CATALOG = {
    'Sirrah': {
        'name': 'Sirrah',
        'id': 'sirrah'
    },
    'Caph': {
        'name': 'Caph',
        'id': 'caph'
    },
    'Algenib': {
        'name': 'Algenib',
        'id': 'algenib'
    },
    'Schedar': {
        'name': 'Schedar',
        'id': 'schedar'
    },
    'Mirach': {
        'name': 'Mirach',
        'id': 'mirach'
    },
    'Achernar': {
        'name': 'Achernar',
        'id': 'achernar'
    },
    'Almach': {
        'name': 'Almach',
        'id': 'almach'
    },
    'Hamal': {
        'name': 'Hamal',
        'id': 'hamal'
    },
    'Polaris': {
        'name': 'Polaris',
        'id': 'polaris'
    },
    'Menkar': {
        'name': 'Menkar',
        'id': 'menkar'
    },
    'Algol': {
        'name': 'Algol',
        'id': 'algol'
    },
    'Electra': {
        'name': 'Electra',
        'id': 'electra'
    },
    'Taygeta': {
        'name': 'Taygeta',
        'id': 'taygeta'
    },
    'Maia': {
        'name': 'Maia',
        'id': 'maia'
    },
    'Merope': {
        'name': 'Merope',
        'id': 'merope'
    },
    'Alcyone': {
        'name': 'Alcyone',
        'id': 'alcyone'
    },
    'Atlas': {
        'name': 'Atlas',
        'id': 'atlas'
    },
    'Zaurak': {
        'name': 'Zaurak',
        'id': 'zaurak'
    },
    'Aldebaran': {
        'name': 'Aldebaran',
        'id': 'aldebaran'
    },
    'Rigel': {
        'name': 'Rigel',
        'id': 'rigel'
    },
    'Capella': {
        'name': 'Capella',
        'id': 'capella'
    },
    'Bellatrix': {
        'name': 'Bellatrix',
        'id': 'bellatrix'
    },
    'Elnath': {
        'name': 'Elnath',
        'id': 'elnath'
    },
    'Nihal': {
        'name': 'Nihal',
        'id': 'nihal'
    },
    'Mintaka': {
        'name': 'Mintaka',
        'id': 'mintaka'
    },
    'Arneb': {
        'name': 'Arneb',
        'id': 'arneb'
    },
    'Alnilam': {
        'name': 'Alnilam',
        'id': 'alnilam'
    },
    'Alnitak': {
        'name': 'Alnitak',
        'id': 'alnitak'
    },
    'Saiph': {
        'name': 'Saiph',
        'id': 'saiph'
    },
    'Betelgeuse': {
        'name': 'Betelgeuse',
        'id': 'betelgeuse'
    },
    'Menkalinan': {
        'name': 'Menkalinan',
        'id': 'menkalinan'
    },
    'Mirzam': {
        'name': 'Mirzam',
        'id': 'mirzam'
    },
    'Canopus': {
        'name': 'Canopus',
        'id': 'canopus'
    },
    'Alhena': {
        'name': 'Alhena',
        'id': 'alhena'
    },
    'Sirius': {
        'name': 'Sirius',
        'id': 'sirius'
    },
    'Adara': {
        'name': 'Adara',
        'id': 'adara'
    },
    'Wezen': {
        'name': 'Wezen',
        'id': 'wezen'
    },
    'Castor': {
        'name': 'Castor',
        'id': 'castor'
    },
    'Procyon': {
        'name': 'Procyon',
        'id': 'procyon'
    },
    'Pollux': {
        'name': 'Pollux',
        'id': 'pollux'
    },
    'Naos': {
        'name': 'Naos',
        'id': 'naos'
    },
    'Alphard': {
        'name': 'Alphard',
        'id': 'alphard'
    },
    'Regulus': {
        'name': 'Regulus',
        'id': 'regulus'
    },
    'Algieba': {
        'name': 'Algieba',
        'id': 'algieba'
    },
    'Merak': {
        'name': 'Merak',
        'id': 'merak'
    },
    'Dubhe': {
        'name': 'Dubhe',
        'id': 'dubhe'
    },
    'Denebola': {
        'name': 'Denebola',
        'id': 'denebola'
    },
    'Phecda': {
        'name': 'Phecda',
        'id': 'phecda'
    },
    'Minkar': {
        'name': 'Minkar',
        'id': 'minkar'
    },
    'Megrez': {
        'name': 'Megrez',
        'id': 'megrez'
    },
    'Gienah Corvi': {
        'name': 'Gienah Corvi',
        'id': 'gienah_corvi'
    },
    'Mimosa': {
        'name': 'Mimosa',
        'id': 'mimosa'
    },
    'Alioth': {
        'name': 'Alioth',
        'id': 'alioth'
    },
    'Vindemiatrix': {
        'name': 'Vindemiatrix',
        'id': 'vindemiatrix'
    },
    'Mizar': {
        'name': 'Mizar',
        'id': 'mizar'
    },
    'Spica': {
        'name': 'Spica',
        'id': 'spica'
    },
    'Alcor': {
        'name': 'Alcor',
        'id': 'alcor'
    },
    'Alcaid': {
        'name': 'Alcaid',
        'id': 'alcaid'
    },
    'Agena': {
        'name': 'Agena',
        'id': 'agena'
    },
    'Thuban': {
        'name': 'Thuban',
        'id': 'thuban'
    },
    'Arcturus': {
        'name': 'Arcturus',
        'id': 'arcturus'
    },
    'Izar': {
        'name': 'Izar',
        'id': 'izar'
    },
    'Kochab': {
        'name': 'Kochab',
        'id': 'kochab'
    },
    'Alphecca': {
        'name': 'Alphecca',
        'id': 'alphecca'
    },
    'Unukalhai': {
        'name': 'Unukalhai',
        'id': 'unukalhai'
    },
    'Antares': {
        'name': 'Antares',
        'id': 'antares'
    },
    'Rasalgethi': {
        'name': 'Rasalgethi',
        'id': 'rasalgethi'
    },
    'Shaula': {
        'name': 'Shaula',
        'id': 'shaula'
    },
    'Rasalhague': {
        'name': 'Rasalhague',
        'id': 'rasalhague'
    },
    'Cebalrai': {
        'name': 'Cebalrai',
        'id': 'cebalrai'
    },
    'Etamin': {
        'name': 'Etamin',
        'id': 'etamin'
    },
    'Kaus Australis': {
        'name': 'Kaus Australis',
        'id': 'kaus_australis'
    },
    'Vega': {
        'name': 'Vega',
        'id': 'vega'
    },
    'Sheliak': {
        'name': 'Sheliak',
        'id': 'sheliak'
    },
    'Nunki': {
        'name': 'Nunki',
        'id': 'nunki'
    },
    'Sulafat': {
        'name': 'Sulafat',
        'id': 'sulafat'
    },
    'Arkab Prior': {
        'name': 'Arkab Prior',
        'id': 'arkab_prior'
    },
    'Arkab Posterior': {
        'name': 'Arkab Posterior',
        'id': 'arkab_posterior'
    },
    'Rukbat': {
        'name': 'Rukbat',
        'id': 'rukbat'
    },
    'Albereo': {
        'name': 'Albereo',
        'id': 'albereo'
    },
    'Tarazed': {
        'name': 'Tarazed',
        'id': 'tarazed'
    },
    'Altair': {
        'name': 'Altair',
        'id': 'altair'
    },
    'Alshain': {
        'name': 'Alshain',
        'id': 'alshain'
    },
    'Sadr': {
        'name': 'Sadr',
        'id': 'sadr'
    },
    'Peacock': {
        'name': 'Peacock',
        'id': 'peacock'
    },
    'Deneb': {
        'name': 'Deneb',
        'id': 'deneb'
    },
    'Alderamin': {
        'name': 'Alderamin',
        'id': 'alderamin'
    },
    'Alfirk': {
        'name': 'Alfirk',
        'id': 'alfirk'
    },
    'Enif': {
        'name': 'Enif',
        'id': 'enif'
    },
    'Sadalmelik': {
        'name': 'Sadalmelik',
        'id': 'sadalmelik'
    },
    'Alnair': {
        'name': 'Alnair',
        'id': 'alnair'
    },
    'Fomalhaut': {
        'name': 'Fomalhaut',
        'id': 'fomalhaut'
    },
    'Scheat': {
        'name': 'Scheat',
        'id': 'scheat'
    },
    'Markab': {
        'name': 'Markab',
        'id': 'markab'
    }
}


class ISS(SpaceBody):
    def __init__(self):
        """ TLE from Space-Trak, 6th July. """
        self.body = ephem.readtle("ISS (ZARYA)",
                                  "1 25544U 98067A   13187.51770631  .00005346  00000-0  99606-4 0  1286",
                                  "2 25544 051.6495 012.5195 0008764 133.4934 272.3907 15.50559659837702")
        self.id = "25544"
        self.name = "International Space Station"
        self.category = "satellite"

    def nudge_date(self):
        return ephem.Date(self.body.set_time + ephem.hour)


class Mercury(SpaceBody):
    def __init__(self):
        self.body = ephem.Mercury()
        self.id = "mercury"
        self.name = "Mercury"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Venus(SpaceBody):
    def __init__(self):
        self.body = ephem.Venus()
        self.id = "venus"
        self.name = "Venus"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Mars(SpaceBody):
    def __init__(self):
        self.body = ephem.Mars()
        self.id = "mars"
        self.name = "Mars"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Jupiter(SpaceBody):
    def __init__(self):
        self.body = ephem.Jupiter()
        self.id = "jupiter"
        self.name = "Jupiter"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Saturn(SpaceBody):
    def __init__(self):
        self.body = ephem.Saturn()
        self.id = "saturn"
        self.name = "Saturn"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Uranus(SpaceBody):
    def __init__(self):
        self.body = ephem.Uranus()
        self.id = "uranus"
        self.name = "Uranus"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Neptune(SpaceBody):
    def __init__(self):
        self.body = ephem.Neptune()
        self.id = "neptune"
        self.name = "Neptune"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Pluto(SpaceBody):
    def __init__(self):
        self.body = ephem.Pluto()
        self.id = "pluto"
        self.name = "Pluto"
        self.category = "planet"

    def nudge_date(self):
        return self.body.rise_time + 1


class Star(SpaceBody):
    def __init__(self, name):
        self.body = ephem.star(STAR_CATALOG[name]['name'])
        self.id = STAR_CATALOG[name]['id']
        self.name = STAR_CATALOG[name]['name']
        self.category = "star"

    def nudge_date(self):
        return self.body.rise_time + 1