#!/usr/bin/env python
from setuptools import setup

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    long_description = ''

setup(
    name='django-zip-stream',
    version='0.0.1',
    description='Django extension to assemble ZIP archives dynamically using Nginx with mod_zip.',
    long_description=long_description,
    author='Travis Cunningham',
    author_email='tcunningham@smartfile.com',
    url='https://github.com/travcunn/django-zip-stream',
    license='MIT',
    packages=['django-zip-stream'],
    package_dir={'django-zip-stream': 'django-zip-stream'},
    install_requires=[
        'pytest',
        'pytest-cov',
        'mock',
        'tox',
    ], )
