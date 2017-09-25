#!/usr/bin/env python
# coding=utf-8
# creater: Jiang Yingming
# date: 2017-05-17

"""Switch Gregorian date to day of year, GNSS calendar (GPS & BDS)."""

from __future__ import print_function
from __future__ import division
import datetime

__all__ = [
    'GPS_START_DATE', 'BDS_START_DATE',
    'bdswd2date', 'bdswd2yrdoy',
    'date2bdswd', 'date2doy', 'date2gpswd', 'date2yrdoy',
    'gpswd2date', 'gpswd2yrdoy',
    'yrdoy2bdswd', 'yrdoy2date', 'yrdoy2gpswd'
]

GPS_START_DATE = datetime.date(1980, 1, 6)
BDS_START_DATE = datetime.date(2006, 1, 1)


def __date2weeksday(date, start):
    """Convert date to spent weeks and day of week from a start date."""
    delta = date - start
    if delta.days >= 0:
        weeks = delta.days // 7
        dayofweek = delta.days % 7
        return weeks, dayofweek
    else:
        raise ValueError('Invalid date: %s, too early.' %date)


def __weeksday2date(weeks, dayofweek, start):
    """Convert spent weeks and day of week to date."""
    if weeks < 0 or dayofweek < 0 or dayofweek > 6:
        raise ValueError('Invalid week or day: %s, %s' %(weeks, dayofweek))
    delta = datetime.timedelta(weeks=weeks, days=dayofweek)

    return start + delta


def date2doy(date):
    """Convert date to day of year, return int doy.

    Example:

    >>> from datetime import date
    >>> date2doy(date(2017, 5, 17))
    137
    """
    first_day = datetime.date(date.year, 1, 1)
    delta = date - first_day

    return delta.days + 1


def date2yrdoy(date):
    """Convert date to year and day of year, return int tuple (year, doy).

    Example:

    >>> from datetime import date
    >>> date2yrdoy(date(2017, 5, 17))
    (2017, 137)
    """
    return date.year, date2doy(date)


def yrdoy2date(year, doy):
    """Convert year and day of year to date, return datetime.date.

    Example:

    >>> yrdoy2date(2017, 137)
    datetime.date(2017, 5, 17)
    """
    if year < 0 or doy < 1:
        raise ValueError('Invalid year or day of year: %s, %s' %(year, doy))
    if year < 100:
        year = year + 2000 if year < 80 else year + 1900
    first_day = datetime.date(year, 1, 1)
    delta = datetime.timedelta(days=doy-1)

    return first_day + delta


def date2gpswd(date):
    """Convert date to GPS week and day of week, return int tuple (week, day).

    Example:

    >>> from datetime import date
    >>> date2gpswd(date(2017, 5, 17))
    (1949, 3)
    >>> date2gpswd(date(1917, 5, 17))
    Traceback (most recent call last):
    ...
    ValueError: Invalid date: 1917-05-17, too early.
    """
    return __date2weeksday(date, GPS_START_DATE)


def date2bdswd(date):
    """Convert date to BDS week and day of week, return int tuple (week, day).

    Example:

    >>> from datetime import date
    >>> date2bdswd(date(2017, 5, 17))
    (593, 3)
    >>> date2bdswd(date(2003, 1, 17))
    Traceback (most recent call last):
    ...
    ValueError: Invalid date: 2003-01-17, too early.
    """
    return __date2weeksday(date, BDS_START_DATE)


def gpswd2date(gpsweek, dayofweek):
    """Convert GPS week and day of week to date, return datetime.date

    Example:

    >>> gpswd2date(1949, 3)
    datetime.date(2017, 5, 17)
    >>> gpswd2date(1949, 8)
    Traceback (most recent call last):
    ...
    ValueError: Invalid week or day: 1949, 8
    """
    return __weeksday2date(gpsweek, dayofweek, GPS_START_DATE)


def bdswd2date(bdsweek, dayofweek):
    """Convert BDS week and day of week to date, return datetime.date

    Example:

    >>> bdswd2date(593, 3)
    datetime.date(2017, 5, 17)
    >>> bdswd2date(-1, 3)
    Traceback (most recent call last):
    ...
    ValueError: Invalid week or day: -1, 3
    """
    return __weeksday2date(bdsweek, dayofweek, BDS_START_DATE)


def yrdoy2gpswd(year, doy):
    """Convert year and day of year to GPS week and day of week,
    return int tuple (week, day).

    Example:

    >>> yrdoy2gpswd(2017, 137)
    (1949, 3)
    >>> yrdoy2gpswd(1937, 147)
    Traceback (most recent call last):
    ...
    ValueError: Invalid date: 1937-05-27, too early.
    """
    date = yrdoy2date(year, doy)
    return date2gpswd(date)


def yrdoy2bdswd(year, doy):
    """Convert year and day of year to BDS week and day of week,
    return int tuple (week, day).

    Example:

    >>> yrdoy2bdswd(2017, 137)
    (593, 3)
    """
    date = yrdoy2date(year, doy)
    return date2bdswd(date)


def gpswd2yrdoy(gpsweek, dayofweek):
    """Convert GPS week and day of week to year and day of year,
    return int tuple (year, doy).

    Example:

    >>> gpswd2yrdoy(1949, 3)
    (2017, 137)
    """
    date = gpswd2date(gpsweek, dayofweek)
    return date2yrdoy(date)


def bdswd2yrdoy(bdsweek, dayofweek):
    """Convert GPS week and day of week to year and day of year,
    return int tuple (year, doy).

    Example:

    >>> bdswd2yrdoy(593, 3)
    (2017, 137)
    """
    date = bdswd2date(bdsweek, dayofweek)
    return date2yrdoy(date)


def gpsw2bdsw(gpsweek):
    """Convert GPS week to BDS week, return int bdsweek.

    Example:

    >>> gpsw2bdsw(1949)
    593
    """
    date = gpswd2date(gpsweek, 0)
    return date2bdswd(date)[0]


def bdsw2gpsw(bdsweek):
    """Convert BDS week to GPS week, return int gpsweek.

    Example:

    >>> bdsw2gpsw(593)
    1949
    """
    date = bdswd2date(bdsweek, 0)
    return date2gpswd(date)[0]


def __handle_cmd(args):
    """Handle command line arguments."""
    # Calculate Gregorian date from arguments
    if args.date:
        date = datetime.date(*args.date)
    elif args.ydoy:
        date = yrdoy2date(*args.ydoy)
    elif args.gpswd:
        date = gpswd2date(*args.gpswd)
    elif args.bdswd:
        date = bdswd2date(*args.bdswd)
    else:
        date = datetime.date.today()
    print('Gregorian date: %s' %date.strftime('%Y-%m-%d'))
    # Convert date into doy, GPS week and BDS week
    doy = date2doy(date)
    print('year, doy: %d, %03d' %(date.year, doy))
    if date >= GPS_START_DATE:
        gpsw, dow = date2gpswd(date)
        print('GPS week: %04d, %d' %(gpsw, dow))
    else:
        print('GPS week: date too early!')
    if date >= BDS_START_DATE:
        bdsw, _ = date2bdswd(date)
        print('BDS week: %04d, %d' %(bdsw, dow))
    else:
        print('BDS week: date too early!')

    return 0


def __init_args():
    """Parse user input from command line."""
    import argparse
    # initilize a argument parser
    parser = argparse.ArgumentParser(
        description='Convert Gregorian date to GNSS calendar, or vice versa.'
    )
    # add arguments
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s 1.1.0')
    parser.add_argument('-date', metavar='<n>', nargs=3, type=int,
                        help='year, month, day')
    parser.add_argument('-ydoy', metavar='<n>', nargs=2, type=int,
                        help='year, day of year')
    parser.add_argument('-gpswd', metavar='<n>', nargs=2, type=int,
                        help='GPS week, day of week')
    parser.add_argument('-bdswd', metavar='<n>', nargs=2, type=int,
                        help='BDS week, day of week')

    return __handle_cmd(parser.parse_args())


if __name__ == '__main__':
    __init_args()
