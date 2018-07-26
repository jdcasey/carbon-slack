#!/usr/bin/env python2

from setuptools import setup, find_packages
import sys

version='0.0.1'

test_deps=[
    "Mock",
    "nose",
    "responses",
  ]

extras = {
  'test':test_deps,
  'build':['tox'],
  'ci':['coverage']
}

setup(
    zip_safe=True,
    name='carbon-slack',
    version=version,
    long_description="Library for using Slack as a bus for sending data to GraphiteDB / Carbon",
    classifiers=[
      "Development Status :: 3 - Alpha",
      "Intended Audience :: Developers",
      "License :: OSI Approved :: GNU General Public License (GPL)",
      "Programming Language :: Python :: 2",
      "Topic :: Utilities",
    ],
    keywords='graphite carbon metrics monitoring ',
    author='John Casey',
    author_email='jdcasey@commonjava.org',
    url='https://github.com/jdcasey/carbon-slack',
    license='GPLv3+',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    install_requires=[
      "slackclient",
      "click",
      "PyYAML"
    ],
    tests_require=test_deps,
    extras_require=extras,
    test_suite="tests",
    entry_points={
      'console_scripts': [
        'telegram-recv = carbon_telegram:recv',
        'telegram-relay = carbon_telegram:relay',
        'telegram-send = carbon_telegram:send'
      ],
    }
)

