#!/usr/bin/env python

from distutils.core import setup

setup(name='ebisu',
      version='0.1dev',
      packages=['ebisu'],
      license='BSD',
      description='Ebisu Health Checker',
      long_description=open('README.rst').read(),
      author='Lucas Waye',
      author_email='wayetender@gmail.com',
      classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: Jython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: BSD License",
    ],
      )
