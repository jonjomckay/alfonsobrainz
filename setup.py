#!/usr/bin/env python
from distutils.core import setup
from setuptools import find_packages

setup(
    name='alfonsobrainz',
    version='0.5',
    description='Python 3 bindings for the MusicBrainz /ws/2 web service',
    author='Jonjo McKay',
    author_email='jonjo@jonjomckay.com',
    url='https://github.com/jonjomckay/alfonsobrainz',
    packages=find_packages(),
    install_requires=['requests>=2.2.1'],
    extras_require={
        'requests-caching': ['requests-cache>=0.4.4']
    },
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Database :: Front-Ends',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)