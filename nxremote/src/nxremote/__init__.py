#!/usr/bin/env python 
# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------
# Copyright (c) 2013-2014, NeXpy Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING, distributed with this software.
#-----------------------------------------------------------------------------

__package_name__ = u'nxremote'
from ._version import get_versions
__version__ = get_versions()['version']
del get_versions

__license__ = u'BSD'
__author__ = u'ExFaC'

__url__          = u'http://nexpy.github.io/nexpy/'
__download_url__ = u'https://github.com/nexpy/nexusformat/'

__description__ = u'nxremote: Python API to access h5serv data using h5pyd'
__long_description__ = \
"""
This package provides a Python API that subclasses the 
[nexusformat package](http://nexpy.github.io/nexusformat) 
to work with HDF5 files served by h5serv. 
"""
