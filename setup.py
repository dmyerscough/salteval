#!/usr/bin/env python

from setuptools import setup

kwargs = {
    "name": "salteval",
    "version": '0.0.1',
    "packages": ["salteval"],
    "scripts": ["bin/saltevl.py"],
    "description": "Perform functional testing of SaltStack States",
    "author": "Damian Myerscough",
    "maintainer": "Damian Myerscough",
    "author_email": "Damian.Myerscough@gmail.com",
    "maintainer_email": "Damian.Myerscough@gmail.com",
    "license": "MIT",
    "url": "https://github.com/dmyerscough/salteval",
    "download_url": "https://github.com/dmyerscough/salteval/archive/master.tar.gz",
}

setup(**kwargs)
