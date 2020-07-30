# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in covid_plasma_donation/__init__.py
from covid_plasma_donation import __version__ as version

setup(
	name='covid_plasma_donation',
	version=version,
	description='COVID19 plasma registry',
	author='Hemolife Service Pvt Ltd',
	author_email='hemolifeservice@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
