#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import unittest
from parse_map import parse_map
from find_square import _find_square, get_map_with_square


def get_test(name, dir_path):
    """return string map with square for test file"""
    path = os.path.join(dir_path, "tests", name + "_test")
    map_info = parse_map(path)
    square = _find_square(map_info)
    return get_map_with_square(map_info, square)


def get_output(name, dir_path):
    """return output file content"""
    path = os.path.join(dir_path, "test_results", name + "_result")
    with open(path, "r") as f:
        return f.read()


class TestSequence(unittest.TestCase):
    """Test class to programmatically build unittests"""
    pass


class TestError(Exception):
    pass


dir_path = os.path.dirname(os.path.realpath(__file__))
test_path = os.path.join(dir_path, "tests")
result_path = os.path.join(dir_path, "test_results")
test_names = []
result_names = []

for filename in os.listdir(test_path):
    if filename.endswith("_test"):
        test_names.append(filename[:-5])
for filename in os.listdir(result_path):
    if filename.endswith("_result"):
        result_names.append(filename[:-7])


for name in test_names:
    if name not in result_names:
        raise TestError(
            f"{name}_test does not have its {name}_result in results"
            )
    testmethodname = f"test_{name}"
    print(testmethodname)
    testmethod = lambda self: self.assertEqual(get_test(name, dir_path), get_output(name, dir_path))
    setattr(TestSequence, testmethodname, testmethod)


if __name__ == '__main__':
    unittest.main()