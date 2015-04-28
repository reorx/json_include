#!/usr/bin/env python
# coding: utf-8

import sys
sys.path.insert(0, '..')

import os
from json_include import build_json_include, read_file


root_path = os.path.dirname(__file__)


def _path(dir):
    return os.path.join(root_path, dir)


def get_files(dirpath):
    return next(os.walk(dirpath))[2]


def test_build_json_include():
    dirpath = _path('source')
    for i in get_files(dirpath):
        yield run_build_json_include, dirpath, i


def run_build_json_include(dirpath, i):
    rv = build_json_include(dirpath, i)
    expect = read_file(os.path.join(_path('expect'), i))
    print rv
    assert rv.strip() == expect.strip()
