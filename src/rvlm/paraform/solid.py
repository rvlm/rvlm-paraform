# -*- coding: utf-8 -*-
"""
Terminology:

 - Presence function
 - Surface function
 - Track function

"""


class Solid(object):

    def __init__(self, pf, nodes=[], genby=None):
        self.pf = pf
        self.nodes = nodes
        self.genby = genby

    def __and__(self, other):
        return intersection(self, other)

    def __or__(self, other):
        return union(self, other)

    def __xor__(self, other):
        return xunion(self, other)

    def __add__(self, other):
        return union(self, other)

    def __sub__(self, other):
        return difference(self, other)

    def union(self, *others):
        return union(self, *others)

    def intersection(self, *others):
        return intersection(self, *others)

    def plus(self, other):
        return union(self, other)

    def minus(self, other):
        return difference(self, other)

    def mirror(self, **kwargs):
        return mirror(self, **kwargs)


def intersection(*objs):
    def pf(x, y, z):
        return all(map(lambda obj: obj.pf(x, y, z), objs))

    return Solid(pf=pf, nodes=objs)


def union(*objs):
    def pf(x, y, z):
        return any(map(lambda obj: obj.pf(x, y, z), objs))

    return Solid(pf=pf, nodes=objs)


def xunion(obj1, obj2):
    def f(pf1, pf2):
        return lambda x, y, z: pf1(x, y, z) ^ pf2(x, y, z)

    return Solid(pf=f(obj1.pf, obj2.pf), nodes=[obj1, obj2])


def difference(obj1, obj2):
    def f(pf1, pf2):
        return lambda x, y, z: pf1(x, y, z) and not pf2(x, y, z)

    return Solid(pf=f(obj1.pf, obj2.pf), nodes=[obj1, obj2])


def translate(obj, dx=0.0, dy=0.0, dz=0.0):
    def f(pf):
        return lambda x, y, z: pf(x-dx, y-dy, z-dz)

    return Solid(pf=f(obj.pf), nodes=[obj])


def rotate(obj):
    raise NotImplementedError()


def scale():
    raise NotImplementedError()


def mirror(obj, plane=None, axis=None, center=None):
    raise NotImplementedError()
