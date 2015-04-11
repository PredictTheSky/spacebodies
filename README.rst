Space Bodies
============

.. image:: https://secure.travis-ci.org/PredictTheSky/spacebodies.png?branch=master
           :target: http://travis-ci.org/PredictTheSky/spacebodies

Space Bodies is the library that powers `Predict the Sky
<http://predictthesky.org>`_. It handles calculating space object positions and
then combines that with weather data to tell you what you can see in the sky.
The library is named after the primary class. Astronomical objects are
sometimes called "bodies", thus the name.

All of the astronomical objects are provided from the same public interface,
using a string which defines which ones are supported.

.. code-block:: python

   >>> import spacebodies
   >>> sb = SpaceBodies('forecast_key', 'spacetrack_username',
                        'spacetrack_password')
   >>> sb.next_events("iss", lat=50.7184, lon=-3.5339)
   ...

Installation
------------

To install Space Bodies:

.. code-block:: bash

   $ pip install spacebodies

spacebodies requires Python 2.7.

Configuration
-------------

To determine both the Weather and Space Object positions, Space Bodies relies
on two external services. The first is `Forecast.io`_ for local weather
predictions and the second is `Space Track`_, a Joint Space Operations Center
project which exposes the position of a lot of known space objects.

When first configuring ``SpaceBodies`` you'll want to provide these in the
initialiser (as shown above).

.. _Forecast.io: 'https://developer.forecast.io'
.. _Space Track: 'https://www.space-track.org'

Supported Space Objects
-----------------------

All of these can be used as keys for ``next_events`` (in lowercase form).

Man Made Objects
^^^^^^^^^^^^^^^^

* ISS

Planets
^^^^^^^

* Mercury
* Venus
* Mars
* Jupiter
* Saturn
* Uranus
* Neptune
* Pluto

Stars
^^^^^

* Sirrah
* Caph
* Algenib
* Schedar
* Mirach
* Achernar
* Almach
* Hamal
* Polaris
* Menkar
* Algol
* Electra
* Taygeta
* Maia
* Merope
* Alcyone
* Atlas
* Zaurak
* Aldebaran
* Rigel
* Capella
* Bellatrix
* Elnath
* Nihal
* Mintaka
* Arneb
* Alnilam
* Alnitak
* Saiph
* Betelgeuse
* Menkalinan
* Mirzam
* Canopus
* Alhena
* Sirius
* Adara
* Wezen
* Castor
* Procyon
* Pollux
* Naos
* Alphard
* Regulus
* Algieba
* Merak
* Dubhe
* Denebola
* Phecda
* Minkar
* Megrez
* Gienah Corvi
* Mimosa
* Alioth
* Vindemiatrix
* Mizar
* Spica
* Alcor
* Alcaid
* Agena
* Thuban
* Arcturus
* Izar
* Kochab
* Alphecca
* Unukalhai
* Antares
* Rasalgethi
* Shaula
* Rasalhague
* Cebalrai
* Etamin
* Kaus Australis
* Vega
* Sheliak
* Nunki
* Sulafat
* Arkab Prior
* Arkab Posterior
* Rukbat
* Albereo
* Tarazed
* Altair
* Alshain
* Sadr
* Peacock
* Deneb
* Alderamin
* Alfirk
* Enif
* Sadalmelik
* Alnair
* Fomalhaut
* Scheat
* Markab

Contribute
----------

.. code-block:: bash

   $ pip install -r requirements.txt
   $ python setup.py test

The tests look for the following environment variables:

* ``FORECAST_KEY``: An API key from `Forecast.io`_
* ``SPACETRACK_USERNAME``: A username from `Space Track`_
* ``SPACETRACK_PASSWORD``: A password for the username above.

#. Check for open issues, or create a new one.
#. Fork `the repository`_, make your changes to **master** (or your own
   branch).
#. Make sure it's got a test to cover it (and you don't break any others).
#. Send a pull request and we'll make sure it gets merged.

But don't change any version numbers or any of the package metadata. But, do
open an issue if it's wrong!

.. _`the repository`: https://github.com/PredictTheSky/spacebodies

Credits
-------

- Nick Charlton <hello@nickcharlton.net> is the primary maintainer and setup
  the package and plugin system.
- Emma Hibling did all the actual smart bits.

