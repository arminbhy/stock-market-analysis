# -*- coding: utf-8 -*-

import unittest

import stocks

# make sure all the required librarires can be imported
import pandas.io.data
import pyquery
import email.mime.multipart
import email.mime.text
import numpy
import pystache

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_absolute_truth_and_meaning(self):
        assert True


if __name__ == '__main__':
    unittest.main()