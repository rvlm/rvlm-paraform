
class Solid(object):

    def __init__(self, pf, underlying=None):
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
