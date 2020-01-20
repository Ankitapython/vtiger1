from setuptools import setup, find_packages

setup(
    name='vtiger1',
    version='1.0',
    author='ankita m',
    # email='ankita.m@testyantra.in',
    packages=find_packages(include=['source'],exclude=['resources'])
)