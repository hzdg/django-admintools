#!/usr/bin/env python

import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

README=read('README.rst')

setup(
    name='django-admintools',
    version='0.1',
    description='A collection of utilities that make dealing with the Django admin a hoot.',
    url='https://github.com/hzdg/django-admintools',
    long_description=README,
    author='chrismc@hzdg.com',
    packages=[
        'admintools',
    ],
)
