#! /usr/bin/env python3
# -*- coding: utf-8 -*-


from setuptools import setup


setup(name="additional_urwid_widgets",
      version="0.1",
      description="Some (in my opinion useful) widgets that extend the python library 'urwid'.",
      url="https://github.com/AFoeee/additional_urwid_widgets",
      author="Adrian Föhling",
      author_email="a.foehling@web.de",
      license="MIT",
      packages=["additional_urwid_widgets",
                "additional_urwid_widgets.assisting_modules",
                "additional_urwid_widgets.widgets"],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: unix-like OS"])