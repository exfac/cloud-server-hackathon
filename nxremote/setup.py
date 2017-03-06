#!/usr/bin/env python

from setuptools import setup, find_packages, Extension

import os, sys
import pkg_resources
pkg_resources.require('numpy')
import numpy
import versioneer

# pull in some definitions from the package's __init__.py file
sys.path.insert(0, os.path.join('src', ))
import nxremote
import nxremote.requires

verbose=1

setup (name =  nxremote.__package_name__,
       version=versioneer.get_version(),
       cmdclass=versioneer.get_cmdclass(),
       license = nxremote.__license__,
       description = nxremote.__description__,
       long_description = nxremote.__long_description__,
       author=nxremote.__author__,
       platforms='any',
       install_requires = nxremote.requires.pkg_requirements,
       package_dir = {'': 'src'},
       packages = find_packages('src'),
       classifiers= ['Development Status :: 4 - Beta',
                     'Intended Audience :: Developers',
                     'Intended Audience :: Science/Research',
                     'License :: OSI Approved :: BSD License',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 2',
                     'Programming Language :: Python :: 2.7',
                     'Programming Language :: Python :: 3',
                     'Programming Language :: Python :: 3.3',
                     'Programming Language :: Python :: 3.4',
                     'Programming Language :: Python :: 3.5',
                     'Topic :: Scientific/Engineering',
                     'Topic :: Scientific/Engineering :: Visualization'],
      )
