#!/usr/bin/env python

from distutils.core import setup

setup(
        name="java-random",
        version="1.0",
        description="Implementation of Java's Random",
        long_description=open("README.rst").read(),
        author="Corbin Simpson",
        author_email="MostAwesomeDude@gmail.com",
        url="http://github.com/MostAwesomeDude/java-random",
        py_modules=[
            "javarandom",
            ],
        )
