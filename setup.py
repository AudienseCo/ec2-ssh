#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

from setuptools import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')


console_scripts = [
    'ec2-ssh = ec2_ssh:main',
    'ec2-host = ec2_ssh:host',
]


setup(
    name="ec2-ssh",
    version="1.7.0",
    author="Adam Johnson",
    author_email="me@adamj.eu",
    description="SSH into EC2 instances via tag name",
    long_description=readme + '\n\n' + history,
    license="MIT",
    url="https://github.com/YPlan/ec2-ssh",
    keywords=["amazon", "aws", "ec2", "ami", "ssh", "cloud", "boto"],
    install_requires=['boto3>=1.1.0'],
    py_modules=['ec2_ssh'],
    entry_points={'console_scripts': console_scripts},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        "Programming Language :: Python :: 3",
        'Programming Language :: Python :: 3.5',
        "Topic :: Utilities"
    ],
)
