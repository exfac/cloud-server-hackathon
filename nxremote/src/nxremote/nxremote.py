#!/usr/bin/env python 
# -*- coding: utf-8 -*-

"""
This package provides a Python API that subclasses the 
nexusformat package to work with HDF5 files served by h5serv. 

"""
from __future__ import (absolute_import, division, print_function)
import six

from copy import copy, deepcopy
import numbers
import os
import re
import sys

import numpy as np
import h5pyd as h5

from nexusformat.nexus import *

class NXRemoteFile(NXFile):

    """
    Structure-based interface to the NeXus file API.

    Usage::

      file = NXFile(filename, ['r','rw','w'])
        - open the NeXus file
      root = file.readfile()
        - read the structure of the NeXus file.  This returns a NeXus tree.
      file.writefile(root)
        - write a NeXus tree to the file.

    Example::

      nx = NXFile('REF_L_1346.nxs','r')
      tree = nx.readfile()
      for entry in tree.NXentry:
          process(entry)
      copy = NXFile('modified.nxs','w')
      copy.writefile(tree)

    Note that the large datasets are not loaded immediately.  Instead, the
    when the data set is requested, the file is reopened, the data read, and
    the file closed again.  open/close are available for when we want to
    read/write slabs without the overhead of moving the file cursor each time.
    The :class:`NXdata` objects in the returned tree hold the object values.
    """

    def __init__(self, name, mode=None, server='http://34.193.81.207:5000', 
                 **kwds):
        """
        Creates an h5py File object for reading and writing.
        """
        self.h5 = h5
        self.name = name
        if mode == 'w' or mode == 'w-' or mode == 'w5':
            if mode == 'w5':
                mode = 'w'
            self._server = server
            self._file = self.h5.File(self.domain, mode, endpoint=self._server)
            self._mode = 'rw'
        else:
            if mode == 'rw' or mode == 'r+':
                self._mode = 'rw'
                mode = 'r+'
            else:
                self._mode = 'r'
            self._server = server
            self._file = self.h5.File(self.domain, mode, endpoint=server)
        self._filename = self._file.filename                             
        self._path = '/'

    def __repr__(self):
        return '<NXRemoteFile "%s" (mode %s)>' % (os.path.basename(self._filename),
                                                  self._mode)

    def open(self, **kwds):
        if self._file.id.uuid == 0:
            self._file = self.h5.File(self._filename, 'r', endpoint=self._server)
            self.nxpath = '/'
        return self

    @property
    def domain(self):
        domain = self.name.split('.')[0].split('/')
        domain.reverse()
        domain.append('exfac')
        return '.'.join(domain)

    @property
    def file(self):
        if self._file.id.uuid == 0:
            self.open()
        return self._file

def loadremote(filename, endpoint, mode='r'):
    """
    Reads a NeXus file returning a tree of objects.

    This is aliased to 'nxload' because of potential name clashes with Numpy
    """
    with NXRemoteFile(filename, mode, endpoint) as f:
        tree = f.readfile()
    return tree

nxloadremote = load
