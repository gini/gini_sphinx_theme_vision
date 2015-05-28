# -*- coding: utf-8 -*-
"""
gini_sphinx theme
=================

Mainly based on the `sphinx_rtd_theme` by Dave Snider.

.. _github: https://www.github.com/snide/sphinx_rtd_theme

"""
from setuptools import setup
from gini_sphinx_theme import __version__

setup(
    name='gini_sphinx_theme',
    version=__version__,
    url='https://github.com/snide/sphinx_rtd_theme/',
    license='MIT',
    author='Lukas Stührk',
    author_email='l.stuehrk@gini.net',
    description='Sphinx theme for gini\'s documentation',
    long_description=open('README.rst').read(),
    zip_safe=False,
    packages=['gini_sphinx_theme'],
    package_data={'gini_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*',
        'static/*.svg'
    ]},
    include_package_data=True,
    install_requires=open('requirements.txt').read().splitlines(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: BSD License',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
        'Topic :: Documentation',
        'Topic :: Software Development :: Documentation',
    ],
)
