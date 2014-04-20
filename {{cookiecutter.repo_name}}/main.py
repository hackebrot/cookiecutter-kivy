#!/usr/bin/env python
# -*- coding: utf-8 -*-

import kivy
kivy.require('{{ cookiecutter.minimum_kivy_version }}')

from {{ cookiecutter.repo_name }}.{{ cookiecutter.repo_name }}app import {{ cookiecutter.repo_name|capitalize }}App


if __name__ in ('__main__', '__android__'):
    {{ cookiecutter.repo_name|capitalize }}App().run()

