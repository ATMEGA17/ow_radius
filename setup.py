#!/usr/bin/env python
import os
import sys

from setuptools import find_packages, setup

from openwisp_radius import get_version

if sys.argv[-1] == 'publish':
    # delete any *.pyc, *.pyo and __pycache__
    os.system('find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf')
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload -s dist/*')
    os.system('rm -rf dist build')
    args = {'version': get_version()}
    print('You probably want to also tag the version now:')
    print("  git tag -a %(version)s -m 'version %(version)s'" % args)
    print('  git push --tags')
    sys.exit()


setup(
    platforms=['Platform Independent'],
    keywords=['django', 'freeradius', 'networking', 'openwisp'],
    packages=find_packages(exclude=['tests*', 'docs*']),
    include_package_data=True,
    zip_safe=False,
)
