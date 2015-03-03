#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from {{cookiecutter.repo_name}}.{{cookiecutter.repo_name}}app import {{cookiecutter.repo_name|capitalize}}App


class Test{{cookiecutter.repo_name|capitalize}}App(unittest.TestCase):
    """TestCase for {{cookiecutter.repo_name|capitalize}}App.
    """
    def setUp(self):
        self.app = {{cookiecutter.repo_name|capitalize}}App()

    def test_name(self):
        self.assertEqual(self.app.name, '{{cookiecutter.repo_name}}')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
