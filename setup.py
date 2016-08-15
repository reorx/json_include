#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


# Use semantic versioning: MAJOR.MINOR.PATCH
version = '0.1.4'


def get_requires():
    with open('requirements.txt', 'r') as f:
        requires = [i for i in map(lambda x: x.strip(), f.readlines()) if i]
    return requires


def get_long_description():
    with open('README.rst', 'r') as f:
        return f.read()


setup(
    name='json-include',
    version=version,
    author='reorx',
    author_email='novoreorx@gmail.com',
    url='https://github.com/reorx/json_include',
    description='An extension for JSON to support file including',
    long_description=get_long_description(),
    py_modules=[
        'json_include',
    ],
    # Or use (make sure find_packages is imported from setuptools):
    # packages=find_packages()
    # install_requires=get_requires(),
    # package_data={}
    entry_points={
        'console_scripts': [
            'json-include=json_include:main'
        ]
    },
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
