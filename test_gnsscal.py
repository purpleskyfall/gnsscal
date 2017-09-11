#!/usr/bin/env python
# coding=utf-8
# creater: Jiang Yingming
# date: 2017-05-17

"""Test gnsscal module."""

import datetime
import unittest
import gnsscal


class Tests(unittest.TestCase):
    """Unit test for gnsscal."""
    def test_date2doy(self):
        """Test date2doy function,
        use date: 2017-5-17, doy: 137.
        """
        date = datetime.date(2017, 5, 17)
        doy = gnsscal.date2doy(date)

        self.assertEqual(doy, 137)

    def test_date2yrdoy(self):
        """Test date2yrdoy function,
        use date: 2017-5-17, doy: 137.
        """
        date = datetime.date(2017, 5, 17)
        year, doy = gnsscal.date2yrdoy(date)

        self.assertEqual(year, 2017)
        self.assertEqual(doy, 137)

    def test_yrdoy2date(self):
        """Test yrdoy2date function,
        use date: 2017-5-17, doy: 137.
        """
        date = gnsscal.yrdoy2date(2017, 137)
        self.assertEqual(date, datetime.date(2017, 5, 17))
        with self.assertRaises(ValueError):
            gnsscal.yrdoy2date(1991, 0)
            gnsscal.yrdoy2date(-1, 1)
            gnsscal.yrdoy2date(-1, 0)

    def test_date2gpswd(self):
        """Test date2gpswd function,
        use date: 2017-5-17, GPS week: 1949, day of week: 3.
        """
        date = datetime.date(2017, 5, 17)
        gpsweek, dayofweek = gnsscal.date2gpswd(date)

        self.assertEqual(gpsweek, 1949)
        self.assertEqual(dayofweek, 3)
        date = datetime.date(1980, 1, 1)
        with self.assertRaises(ValueError):
            gnsscal.date2gpswd(date)

    def test_date2bdswd(self):
        """Test date2bdswd function,
        use date: 2017-5-17, BDS week: 593, day of week: 3."""
        date = datetime.date(2017, 5, 17)
        bdsweek, dayofweek = gnsscal.date2bdswd(date)

        self.assertEqual(bdsweek, 593)
        self.assertEqual(dayofweek, 3)
        date = datetime.date(1980, 1, 1)
        with self.assertRaises(ValueError):
            gnsscal.date2bdswd(date)

    def test_gpswd2date(self):
        """Test gpswd2date function,
        use date: 2017-5-17, GPS week: 1949, day of week: 3.
        """
        date = gnsscal.gpswd2date(1949, 3)

        self.assertEqual(date, datetime.date(2017, 5, 17))
        with self.assertRaises(ValueError):
            gnsscal.gpswd2date(-1, 0)
            gnsscal.gpswd2date(0, -1)
            gnsscal.gpswd2date(-1, -1)

    def test_bdswd2date(self):
        """Test bdswd2date function,
        use date: 2017-5-17, BDS week: 593, day of week: 3.
        """
        date = gnsscal.bdswd2date(593, 3)

        self.assertEqual(date, datetime.date(2017, 5, 17))
        with self.assertRaises(ValueError):
            gnsscal.gpswd2date(-1, 0)
            gnsscal.gpswd2date(0, -1)
            gnsscal.gpswd2date(-1, -1)

    def test_yrdoy2gpswd(self):
        """Test yrdoy2gpswd function,
        use date: 2017-5-17, doy: 137, GPS week: 1949, day of week: 3.
        """
        gpsweek, dayofweek = gnsscal.yrdoy2gpswd(2017, 137)

        self.assertEqual(gpsweek, 1949)
        self.assertEqual(dayofweek, 3)

    def test_yrdoy2bdswd(self):
        """Test yrdoy2bdswd function,
        use date: 2017-5-17, doy: 137, BDS week: 593, day of week: 3.
        """
        bdsweek, dayofweek = gnsscal.yrdoy2bdswd(2017, 137)

        self.assertEqual(bdsweek, 593)
        self.assertEqual(dayofweek, 3)

    def test_gpswd2yrdoy(self):
        """Test gpswd2yrdoy function,
        use date: 2017-5-17, doy: 137, GPS week: 1949, day of week: 3.
        """
        year, doy = gnsscal.gpswd2yrdoy(1949, 3)

        self.assertEqual(year, 2017)
        self.assertEqual(doy, 137)

    def test_bdswd2yrdoy(self):
        """Test bdswd2yrdoy function,
        use date: 2017-5-17, doy: 137, GPS week: 593, day of week: 3.
        """
        year, doy = gnsscal.bdswd2yrdoy(593, 3)

        self.assertEqual(year, 2017)
        self.assertEqual(doy, 137)

    def test_gpsw2bdsw(self):
        """Test gpsw2bdsw function,
        use GPS week 1949.
        """
        bdsweek = gnsscal.gpsw2bdsw(1949)

        self.assertEqual(bdsweek, 593)

    def test_bdsw2gpsw(self):
        """Test bdsw2gpsw function,
        use BDS week 593.
        """
        gpsweek = gnsscal.bdsw2gpsw(593)

        self.assertEqual(gpsweek, 1949)


if __name__ == '__main__':
    unittest.main()
