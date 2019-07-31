#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import drf_http_response


class UnitTests(unittest.TestCase):
    def test_import(self):
        self.assertIsNotNone(drf_http_response)

    def test_project(self):
        self.assertTrue(False, "write more tests here")