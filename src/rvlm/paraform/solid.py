"""
Solid bodies
============

"""
import math as _math
import dataclasses as _dc
import numpy as _np


@_dc.dataclass(frozen=True)
class Material:
    epsilon : float = 1.0
    mu      : float = 1.0
    sigma   : float = 0.0
    sigmaH  : float = 0.0


def _wrapMaterial(material):
    if material is None:
        return lambda p: Material()

    if isinstance(material, Material):
        return lambda p: material

    if callable(material):
        return material

    raise ValueError("material: unsupported type")


def _combine(sdf, material):
    material = _wrapMaterial(material)
    def probeFunc(p):
        sd = sdf(p)
        if sd > 0.0:
            return sd, None

        mat = material(p)
        return sd, mat

    return probeFunc


def _blend(*materials):
    assert len(materials) > 0
    return materials[0]


class Solid(object):

    def __init__(self, probeFunc):
        self._probeFunc = probeFunc

    @property
    def probe(self):
        return self._probeFunc

    def __and__(self, other):
        return intersection(self, other)

    def __or__(self, other):
        return union(self, other)

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


class Cuboid(Solid):

    def __init__(self, dimensions : _np.ndarray, material = None):

        dimensions = _np.copy(dimensions)
        self._dimentions = dimensions

        def sdf(p : _np.ndarray):
            q = _np.abs(p) - 0.5 * dimensions
            u = _np.maximum(q, 0.0)
            uMag = _np.linalg.norm(u)

            qx, qy, qz = q
            return uMag + min(max(qx, max(qy, qz)), 0.0)

        super().__init__(_combine(sdf, material))

    @property
    def dimensions(self):
        return self._dimentions


class Ellipsoid(Solid):

    def __init__(self, dimensions : _np.ndarray, material = None):

        dimensions = _np.copy(dimensions)
        self._dimentions = dimensions

        def sdf(p : _np.ndarray):
            v = 2 * p / dimensions
            u = 2 * v / dimensions
            vMag = _np.linalg.norm(v)
            uMag = _np.linalg.norm(u)
            return vMag * (vMag - 1) / uMag

        super().__init__(_combine(sdf, material))

    @property
    def dimensions(self):
        return self._dimentions


def intersection(*solids):

    def probeFunc(p):

        if len(solids) == 0:
            return _np.inf, None

        maxSdf = -_np.inf
        mats = []
        for s in solids:
            sdf, mat = s.probe(p)

            if sdf > maxSdf:
                maxSdf = sdf

            if sdf <= 0.0:
                mats.append(mat)

        return maxSdf, _blend(mats)

    return Solid(probeFunc)


def union(*solids):

    def probeFunc(p):

        if len(solids) == 0:
            return _np.inf, None

        minSdf = _np.inf
        mats = []
        for s in solids:
            sdf, mat = s.probe(p)

            if sdf < minSdf:
                minSdf = sdf

            if sdf <= 0.0:
                mats.append(mat)

        return minSdf, _blend(mats)

    return Solid(probeFunc)


def difference(obj1, obj2):

    def probeFunc(p):
        sdf1, mat1 = obj1.probe(p)
        sdf2, mat2 = obj2.probe(p)
        sdf = max(sdf1, -sdf2)

        mat = None
        if sdf1 <= 0.0 and sdf2 > 0.0:
            mat = _blend(mat1, mat2)

        return sdf, mat

    return Solid(probeFunc)


def translate(obj, dx=0.0, dy=0.0, dz=0.0):
    raise NotImplementedError()


def rotate(obj):
    raise NotImplementedError()


def mirror(obj, plane=None, axis=None, center=None):
    raise NotImplementedError()
