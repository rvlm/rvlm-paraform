
class Solid(object):

    def __init__(self, *, pf, underlying=None):
        """
        """

        if underlying is None:
            underlying = []

        self._pf = pf
        self._underlying   = underlying

    @property
    def pf(self):
        return self._pf

    @property
    def underlying(self):
        return self._underlying

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


class Cuboid(Solid):
    """
    """

    def __init__(self, x_edge, y_edge, z_edge, **kwargs):
        """
        """

        self._x_edge = x_edge
        self._y_edge = y_edge
        self._z_edge = z_edge

        def pf(x, y, z):
            hx = x_edge / 2
            hy = y_edge / 2
            hz = z_edge / 2
            return (-hx <= x <= hx and
                    -hy <= y <= hy and
                    -hz <= z <= hz)

        super().__init__(pf=pf, **kwargs)

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

        def pf(x, y, z):
            ax = x_diameter / 2
            ay = y_diameter / 2
            az = z_diameter / 2
            return (x/ax)**2 + (y/ay)**2 + (z/az)**2 <= 1

        super().__init__(pf=pf, **kwargs)

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
    def pf(x, y, z):
        return all(map(lambda obj: obj.pf(x, y, z), solids))

    return Solid(pf=pf, underlying=solids)


def union(*solids):
    def pf(x, y, z):
        return any(map(lambda obj: obj.pf(x, y, z), solids))

    return Solid(pf=pf, underlying=solids)


def xunion(obj1, obj2):
    def f(pf1, pf2):
        return lambda x, y, z: pf1(x, y, z) ^ pf2(x, y, z)

    return Solid(pf=f(obj1.pf, obj2.pf), underlying=[obj1, obj2])


def difference(obj1, obj2):
    def transform(pf1, pf2):
        return lambda x, y, z: pf1(x, y, z) and not pf2(x, y, z)

    return Solid(pf=transform(obj1.pf, obj2.pf),
                 underlying=[obj1, obj2])


def translate(obj, dx=0.0, dy=0.0, dz=0.0):
    raise NotImplementedError()


def rotate(obj):
    raise NotImplementedError()


def mirror(obj, plane=None, axis=None, center=None):
    raise NotImplementedError()
