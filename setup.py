#!/usr/bin/env python

import os
import setuptools
import mula

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setuptools.setup(
    name="pymula",
    version=mula.__version__,
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='GPLv3+',
    description='Cellulant Mula Python adapter',
    long_description='Python adapter for Cellulant Mula.',
    url="https://goodup.com",
    author="Loek van Gent",
    author_email="hallo@loekvan.gent",
    install_requires=[
        'suds',
        'requests[security]==2.8.1'
    ],
    tests_require=[
        'nose'
    ],
    test_suite='nose.collector',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content'
    ]
)
