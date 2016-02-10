#-*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os
import sys

PY3 = sys.version_info[0] == 3

if PY3:
  install_requires = ["six"]
else:
  install_requires = ["six", "simplejson"]

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='davpy',
    version='1.0.1',
    include_package_data=True,
    py_modules=['davpy'],
    url='https://github.com/dfranganillo/davpy',
    license='MIT',
    author='lexich, dfranganillo',
    author_email='lexich121@gmail.com, dfranganillo@gmail.com',
    description='Simple wrapper to work with Basic Auth webdavs',
    long_description=README,
    install_requires=install_requires
)
