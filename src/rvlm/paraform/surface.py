
class Surface(object):

    def __init__(self, sf):
        self.urange = None
        self.vrange = None
        self.sf = sf

    def scale(self, **kwargs):
        return scale(self, **kwargs)

    def shift(self, **kwargs):
        return shift(self, **kwargs)


class Plane(Surface):

    def __init__(self, normal):



        pass


Oxy = Surface(sf=lambda u, v: (u, v, 0))

Oxz = Surface(sf=lambda u, v: (u, 0, v))

Oyz = Surface(sf=lambda u, v: (0, u, v))


def ribbonX(ymin=None, ymax=None, zmin=None, zmax=None):
    pass


def scale(obj, f_x=None, f_y=None, f_z=None):
    pass


def shift(surf, f_xy=None, f_xz=None, f_yz=None):
    """

        zx_xzy

        shift(surf, x_vector=f)
        shift(surf, x_y=f)
        shift(surf, x_z=f)
        shift(surf, x_yz=f)
        shift(surf, x_zy=f)
        shift(surf, x_xyz=f) ......

        shift(surf, y_p=f)
        shift(surf, y_x=f)
        shift(surf, y_z=f)
        shift(surf, y_xz=f)
        shift(surf, y_zx=f)

        shift(surf, z_p=f)
        shift(surf, z_x=f)
        shift(surf, z_y=f)
        shift(surf, z_xy=f)
        shift(surf, z_yz=f)

        shift(surf, p_x=f)
        shift(surf, p_y=f)
        shift(surf, p_z=f)
        shift(surf, p_xy=f)
        shift(surf, p_yx=f)
        shift(surf, p_xz=f)
        shift(surf, p_zx=f)
        shift(surf, p_yz=f)
        shift(surf, p_zy=f)
        shift(surf, p_p=f)

    :param surf:
    :param f_xy:
    :param f_xz:
    :param f_yz:
    :return:
    """

    if f_xy and not (f_xz or f_yz):
        def f(sf):
            def new_sf(u, v):
                (x, y, z) = sf(u, v)
                return (x, y, z + f_xy(x, y))

            return new_sf

        return Surface(sf=f(surf.sf))

    if f_xz and not (f_xy or f_yz):
        def f(sf):
            def new_sf(u, v):
                (x, y, z) = sf(u, v)
                return (x, y + f_xz(x, z), z)

            return new_sf

        return Surface(sf=f(surf.sf))

    if f_yz and not (f_xy or f_xz):
        def f(sf):
            def new_sf(u, v):
                (x, y, z) = sf(u, v)
                return (x + f_yz(y, z), y, z)

            return new_sf

        return Surface(sf=f(surf.sf))

    raise ValueError()

