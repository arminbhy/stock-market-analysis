# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='stocks',
    version='0.0.1',
    description='Stock Market Analysis',
    long_description=readme,
    author='Armin Bahramshahry',
    author_email='arminbhy@gmail.com',
    url='https://github.com/arminbhy/stock-market-analysis',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

