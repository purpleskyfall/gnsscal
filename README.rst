gnsscal
=======

This module contains functions for converting between Gregorian date, day of year and GNSS calendar, now support GNSS calendar for GPS and BDS.

There are 3 functions for converting between Gregorian date and day of year (doy):

.. code-block:: python

    date2doy(date)
    date2yrdoy(date)
    yrdoy2date(year, doy)

Using them like:

.. code-block:: python

    >>> from datetime import date

    >>> date2doy(date(2017, 5, 17))
    137

    >>> date2yrdoy(date(2017, 5, 17))
    (2017, 137)

    >>> yrdoy2date(2017, 137)
    datetime.date(2017, 5, 17)

There are 4 functions for converting between Gregorian date and GNSS calendars (GPS or BDS):

.. code-block:: python

    date2gpswd(date)
    date2bdswd(date)
    gpswd2date(gpsweek, dayofweek)
    bdswd2date(bdsweek, dayofweek)

Using them like:

.. code-block:: python

    >>> from datetime import date

    >>> date2gpswd(date(2017, 5, 17))
    (1949, 3)

    >>> date2bdswd(date(2017, 5, 17))
    (593, 3)

    >>> gpswd2date(1949, 3)
    datetime.date(2017, 5, 17)

    >>> bdswd2date(593, 3)
    datetime.date(2017, 5, 17)

There are 4 functions for converting between year, day of year (doy) and GNSS calendars (GPS or BDS):

.. code-block:: python

    yrdoy2gpswd(year, doy)
    yrdoy2bdswd(year, doy)
    gpswd2yrdoy(gpsweek, dayofweek)
    bdswd2yrdoy(bdsweek, dayofweek)

Using them like:

.. code-block:: python

    >>> yrdoy2gpswd(2017, 137)
    (1949, 3)

    >>> yrdoy2bdswd(2017, 137)
    (593, 3)

    >>> gpswd2yrdoy(1949, 3)
    (2017, 137)

    >>> bdswd2yrdoy(593, 3)
    (2017, 137)

There are also 2 functions for converting between GPS calendar and BDS calendar:

.. code-block:: python

    gpsw2bdsw(gpsweek)
    bdsw2gpsw(bdsweek)

Using them like:

.. code-block:: python

    >>> gpsw2bdsw(1949)
    593

    >>> bdsw2gpsw(593)
    1949

Where the type of date is `datetime.date` and others are `int` or tuple of `int`.

Zero point of GPS and BDS are also given as module level constains in Gregorian date.


Examples
--------

.. code-block:: python

    import gnsscal
    from datetime import date

    # Convert Gregorian date to GPS calendar
    today = date.today()
    gpsweek, days = gnsscal.date2gpswd(today)

    # Convert GPS week to BDS week
    gpsweek = 1812
    bdsweek = gnsscal.gpsw2bdsw(gpsweek)

    # Get zero point of GPS and BDS calendar
    gps_zero = gnsscal.GPS_START_DATE
    bds_zero = gnsscal.BDS_START_DATE


CLI mode
--------

You can also using gnsscal in CLI mode::

    $ python -m gnsscal [options]

Set input date using the optional arguments::

-h, --help                          show this help message and exit
-v, --version                       show program's version number and exit
-date <year> <month> <day>          year, month, day
-ydoy <year> <doy>                  year, day of year
-gpswd <GPS week> <day of week>     GPS week, day of week
-bdswd <BDS week> <day of week>     BDS week, day of week

Example, typing this command in terminal::

    $ python -m gnsscal -date 2017 5 17

Then it will print::

    Gregorian date: 2017-05-17
    year, doy: 2017, 137
    GPS week: 1949, 3
    BDS week: 0593, 3

Installation
------------

The module can be installed using pip::

    $ pip install gnsscal


Test
----

Test gnsscal.py using command::

    $ python test_gnsscal.py


License
-------

Released under BSD, see LICENSE for more details.

For comments and suggestions, please send email to: jiangyingming(at)live.com
