# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='vie-summarizer',
    version='0.1.0',
    description='Summarizes VIE chat rooms',
    long_description=readme,
    author='Yuzhou Liu',
    url='https://github.com/yuzhouliu9/vie-summarizer',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    entry_points = {
        'console_scripts': ['vie_summarizer=vie_summarizer.main:main'],
    },
)
