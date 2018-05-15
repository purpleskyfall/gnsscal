#!/usr/bin/env python
# coding=utf-8

from setuptools import setup
import gnsscal

setup(
    name='gnsscal',
    version='1.1.1',
    description='Switch Gregorian date to GNSS calendar (GPS & BDS).',
    long_description=open("README.rst").read(),
    license='BSD',
    author='Jon Jiang',
    author_email='jiangyingming@live.com',
    url='https://github.com/purpleskyfall/gnsscal',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python',
    ],
    py_modules=['gnsscal']
)