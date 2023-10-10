#!/usr/bin/python3.10

from setuptools import setup

'''
setup function to be run when creating packages.
command to be typed in:
python3 setup.py sdist bdist_wheel
python3 setup.py sdist sdist
python3 setup.py sdist sdist bdist_wheel
'''

setup(
    name='sensehat_assist',  # package name, used at pip or tar.
    version='0.0.0',  # version Nr.... whatever
    packages=["SenseHatCustomExceptions"],  # string list of packages to be translated
    url='',  # if url is used at all
    license='',  # ...
    author='sziller',  # well obvious
    author_email='sziller@gmail.com',  # well obvious
    description='SenseHat related custom-made Exceptions',  # well obvious
    install_requires=[                  # ATTENTION! Wheel file needed, depending on environment
                      ],
    dependency_links=[],  # if dependent on external projects
)
