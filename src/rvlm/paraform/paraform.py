# -*- coding: utf-8 -*-
"""
Terminology:

 - Presence function
 - Surface function
 - Track function

"""
import rvlm.paraform.implementation as imp


class Object3D(object):

    def __init__(self, f):
        self.bounds     = None
        self.components = None
        self.pf = f

    def union(self, *others):
        pass

    def intersection(self, *others):
        pass

    def minus(self, *others):
        pass

    def mirror(self, **kwargs):
        pass


class Object2D(object):

    def __init__(self, f):
        self.sf = f


class Object1D(object):

    def __init__(self, f):
        self.tf = f


def union(*objs):
    pass


def intersection(*objs):
    pass


def difference(a, b):
    pass


def xunion(*objs):
    pass


def mirror(obj, plane=None, axis=None, center=None):
    pass


def rotate(obj, axis=None, radians=0.0, degrees=None):
    pass


def translate(obj, coords):
    pass

