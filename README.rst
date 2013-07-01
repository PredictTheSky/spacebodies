============
Space Bodies
============

Space Bodies is the library that powers `Predict the Sky
<http://predictthesky.org>`_. It handles calculating space object positions and
then combines that with weather data to tell you what you can see in the sky.
The library is named after the primary class. Astronomical objects are
sometimes called "bodies", thus the name.

It uses a simple plugin system for supporting different astronomical objects,
which is exposed as a standardised interface.

.. code-block:: pycon
   
   >>> sb = SpaceBodies()
   >>> sb.next_events("iss", lat=50.7184, lon=-3.5339)
   ...

Installation
------------

To install Space Bodies:

.. code-block:: bash

   $ pip install spacebodies

Contribute
----------

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

