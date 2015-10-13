import rvlm.paraform.solid as _pf


class Box(_pf.Solid):

    def __init__(self, wx, wy, wz):

        def pf(x, y, z):
            lwx = self.wx / 2.0
            lwy = self.wy / 2.0
            lwz = self.wz / 2.0
            return abs(x) <= lwx and abs(y) <= lwy and abs(z) <= lwz

        self.wx = wx
        self.wy = wy
        self.wz = wz
        self.pf = pf


class Ball(_pf.Solid):

    def __init__(self, d):

        def pf(x, y, z):
            lr2 = (self.d/2.0)**2
            return x*x + y*y + z*z <= lr2

        self.d  = d
        self.pf = pf


class Cylinder(_pf.Solid):

    def __init__(self, r, h):

        def pf(x, y, z):
            lr2 = self.r**2
            lh  = self.h / 2.0
            return x*x + y*y <= lr2 and abs(z) <= lh

        self.r  = r
        self.h  = h
        self.pf = pf


def cube(edge):
    return Box(edge, edge, edge)


def box(wx, wy, wz):
    pass


def loft(a, b, r_x=None, r_y=None, r_z=None):
    pass
