#!/usr/bin/env python
from setuptools import setup

setup(
    name="tap-airtable",
    version="0.1.0",
    description="Singer.io tap for extracting data",
    author="ActBlue",
    url="http://singer.io",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_airtable"],
    install_requires=[
        # NB: Pin these to a more specific version for tap reliability
        "singer-python",
        "requests",
        "pyairtable"
    ],
    entry_points="""
    [console_scripts]
    tap-airtable=tap_airtable:main
    """,
    packages=["tap_airtable"],
    package_data = {
        "schemas": ["tap_airtable/schemas/*.json"]
    },
    include_package_data=True,
)
