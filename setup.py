__author__ = 'IGulyaev'

from setuptools import setup, find_packages

setup(
    name = "bottle-gae-boilerplate",
    version = "1.0",
    url = 'http://github.com/robotsarelame/bottle-gae-boilerplate',
    license = 'BSD',
    description = "A basic boilerplate to develop python projects using Bottle.py and deploy them on Google App Engine",
    author = 'Igor Gulyaev',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['setuptools'],
)