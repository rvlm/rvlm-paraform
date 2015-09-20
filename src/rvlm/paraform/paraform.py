# -*- coding: utf-8 -*-
"""
Terminology:

 - Presence function
 - Surface function
 - Track function

"""


class Object3D(object):

    def __init__(self, pf, components):
        self.pf = pf
        self.components = None

    def union(self, *others):
        return union(self, *others)

    def intersection(self, *others):
        return intersection(self, *others)

    def minus(self, other):
        return difference(self, other)

    def mirror(self, **kwargs):
        return mirror(self, **kwargs)


def union(*objs):
    def pf(x, y, z):
        return any(map(lambda obj: obj.pf(x, y, z), objs))

    return Object3D(pf=pf, components=objs)


def intersection(*objs):
    def pf(x, y, z):
        return all(map(lambda obj: obj.pf(x, y, z), objs))

    return Object3D(pf=pf, components=objs)


def difference(obj1, obj2):
    def f(pf1, pf2):
        return lambda x, y, z: pf1(x, y, z) and not pf2(x, y, z)

    return Object3D(pf=f(obj1.pf, obj2.pf), components=[obj1, obj2])


def translate(obj, dx=0.0, dy=0.0, dz=0.0):
    def f(pf):
        return lambda x, y, z: pf(x-dx, y-dy, z-dz)

    return Object3D(pf=f(obj.pf), components=[obj])


def rotate(obj):
    raise NotImplementedError()


def scale():
    raise NotImplementedError()


def mirror(obj, plane=None, axis=None, center=None):

    if plane and not (axis or center):
        def f(pf):
            return lambda x, y, z: pf(x, y, z)

        return Object3D(pf=f(obj.pf), components=[obj])

    if axis and not (plane or center):
        def f(pf):
            return lambda x, y, z: pf(x, y, z)

        return Object3D(pf=f(obj.pf), components=[obj])

    if center and not (plane or axis):
        def f(pf):
            return lambda x, y, z: pf(x, y, z)

        return Object3D(pf=f(obj.pf), components=[obj])

    raise ValueError()
