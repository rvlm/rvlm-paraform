"""
Solid bodies
============

"""
import math as _math

class Solid(object):

    def __init__(self, *, sdf, underlying=None):
        """
        """

        if underlying is None:
            underlying = []

        self._sdf = sdf
        self._underlying   = underlying

    @property
    def sdf(self):
        return self._sdf

    @property
    def underlying(self):
        return self._underlying

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
    """
    """

    def __init__(self, x_edge, y_edge, z_edge, **kwargs):
        """
        """

        self._x_edge = x_edge
        self._y_edge = y_edge
        self._z_edge = z_edge

        bx = x_edge / 2
        by = y_edge / 2
        bz = z_edge / 2

        def sdf(x, y, z):
            qx = abs(x) - bx
            qy = abs(y) - by
            qz = abs(z) - bz

            ux = max(qx, 0.0)
            uy = max(qy, 0.0)
            uz = max(qz, 0.0)
            uMag = _math.sqrt(ux * ux + uy * uy + uz * uz)

            return uMag + min(max(qx, max(qy, qz)), 0.0)

        super().__init__(sdf=sdf, **kwargs)

    @property
    def x_edge(self):
        return self._x_edge

    @property
    def y_edge(self):
        return self._y_edge

    @property
    def z_edge(self):
        return self._z_edge


class Ellipsoid(Solid):
    """
    """

    def __init__(self, x_diameter, y_diameter, z_diameter, **kwargs):
        """
        """

        self._x_diameter = x_diameter
        self._y_diameter = y_diameter
        self._z_diameter = z_diameter

        rx = x_diameter / 2
        ry = y_diameter / 2
        rz = z_diameter / 2

        def sdf(x, y, z):
            vx = x / rx
            vy = y / ry
            vz = z / rz
            ux = vx / rx
            uy = vy / ry
            uz = vz / rz
            vMag = _math.sqrt(vx * vx + vy * vy + vz * vz)
            uMag = _math.sqrt(ux * ux + uy * uy + uz * uz)
            return vMag * (vMag - 1) / uMag

        super().__init__(sdf=sdf, **kwargs)

    @property
    def x_diameter(self):
        return self._x_diameter

    @property
    def y_diameter(self):
        return self._y_diameter

    @property
    def z_diameter(self):
        return self._z_diameter


def intersection(*solids):
    def sdf(x, y, z):
        return max(obj.sdf(x, y, z) for obj in solids)

    return Solid(sdf=sdf, underlying=solids)


def union(*solids):
    def sdf(x, y, z):
        return min(obj.sdf(x, y, z) for obj in solids)

    return Solid(sdf=sdf, underlying=solids)


def difference(obj1, obj2):
    def sdf(x, y, z):
        return max(obj1.sdf(x, y, z), -obj2.sdf(x, y, z))

    return Solid(sdf=sdf, underlying=[obj1, obj2])


def translate(obj, dx=0.0, dy=0.0, dz=0.0):
    raise NotImplementedError()


def rotate(obj):
    raise NotImplementedError()


def mirror(obj, plane=None, axis=None, center=None):
    raise NotImplementedError()
