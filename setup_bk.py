#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
--------------------------------------------------------------
describe:
    setup config

base_info:
    __version__ = "v.10"
    __author__ = "mingliang.gao"
    __time__ = "2020/5/19 3:41 PM"
    __mail__ = "mingliang.gao@163.com"
--------------------------------------------------------------
"""

# ------------------------------------------------------------
# usage: /usr/bin/python setup.py.py
# ------------------------------------------------------------
from setuptools import setup, find_packages


setup(
    name="deploy",
    version="1.0",
    keywords=[
        "python2", "sdk",
        "web", "frame"
    ],
    description="python project sdk",
    long_description_content_type='text/markdown',
    long_description="this is the python project sdk by pygo to develop",
    license="MIT Licence",

    classifiers=[
        "Development Status :: 1 - Developing",
        "Intended Audience :: Developers",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
    ],

    url="http://pygo2.cn",
    author="pygo",
    author_email="gaoming971366@163.com",
    download_url="",

    packages=find_packages(),
    py_modules=[],
    include_package_data=True,
    platforms=["Windows", "Linux"],

    scripts=[],
    python_requires='>=2.7',
    install_requires=[
        "setuptools>=16.0"
    ],
    entry_points={
        'console_scripts': [
        ]
    },

    zip_safe=False
)



