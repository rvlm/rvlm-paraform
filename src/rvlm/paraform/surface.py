"""
Two parametric surfaces
=======================

"""
import rvlm.paraform.utils as _utils


class Surface(object):
    """
    """

    def __init__(self, sf, u_range, v_range):
        """
        """
        self._u_range = u_range
        self._v_range = v_range
        self._sf      = sf

    @property
    def sf(self):
        return self._sf

    @property
    def u_range(self):
        return self._u_range

    @property
    def v_range(self):
        return self._v_range

    def translate(self, **kwargs):
        return translate(self, **kwargs)


class Plane(Surface):
    """
    """

    def __init__(self, point, u_vect, v_vect):
        """
        """
        assert _utils.is_vector_3d(point)
        assert _utils.is_vector_3d(u_vect)
        assert _utils.is_vector_3d(v_vect)

        # Calculate normal vector and do not even care about the case
        # when u_vect is parallel to v_vect.
        normal_vect = _utils.cross_product(u_vect, v_vect)
        normal_vect = _utils.unit_vector(normal_vect)

        self._point  = point
        self._u_vect = u_vect
        self._v_vect = v_vect
        self._normal_vect = normal_vect

        x0, y0, z0 = point
        ux, uy, uz = u_vect
        vx, vy, vz = v_vect

        def sf(u, v):
            return [x0 + ux*u + vx*v, y0 + uy*u + vy*v, z0 + uz*u + vz*v]

        super().__init__(sf=sf, u_range=[0, 1], v_range=[0, 1])

    @property
    def point(self):
        return self._point

    @property
    def u_vect(self):
        return self._u_vect

    @property
    def v_vect(self):
        return self._v_vect

    @property
    def normal_vect(self):
        return self._normal_vect

    XY = None
    XZ = None
    YZ = None


# Due to Python's limitations we must initialize these variable from outside
# of the class. That's not so black as it looks.
Plane.XY = Plane([0, 0, 0], [1, 0, 0], [0, 1, 0])
Plane.XZ = Plane([0, 0, 0], [1, 0, 0], [0, 0, 1])
Plane.YZ = Plane([0, 0, 0], [0, 1, 0], [0, 0, 1])


def translate(surf, dx=0.0, dy=0.0, dz=0.0):
    """
    Creates a translated copy of a surface. Result is a surface just like the
    original, but shifted by `(dx, dy, dz)` vector.

    :type  surf: Surface
    :param surf: Surface object to create a translated copy for.

    :type  dx, dy, dz: float
    :param dx, dy, dz: Coordinates shift along each axis. These coordinate
        components form a translation vector. Note that these parameters
        default values allows you to specify only non-zero components.

    Examples
    --------

        >>> [x0, y0, z0] = Plane.XY.sf(0, 0)
        >>> h = 1.0
        >>> planes = [Plane.XY.translate(dz=i*h) for i in range(5)]
        >>> for surf in planes:
        ...     [x, y, z] = surf.sf(0, 0)
        ...     print([x - x0, y - y0, z - z0])
        ...
        [0.0, 0.0, 0.0]
        [0.0, 0.0, 1.0]
        [0.0, 0.0, 2.0]
        [0.0, 0.0, 3.0]
        [0.0, 0.0, 4.0]

        In the example above we have demonstrated that plane object has really
        been shifted, because :math:`sf(0, 0)` returns the same relative point
        of an object. You may change `sf`'s arguments and see that the output
        remains the same.

        TODO: Add image.

    """
    assert _utils.is_number(dx)
    assert _utils.is_number(dy)
    assert _utils.is_number(dz)

    def transform(sf):
        def transformed_sf(u, v):
            x, y, z = sf(u, v)
            return x+dx, y+dy, z+dz

        return transformed_sf

    return Surface(sf=transform(surf.sf),
                   u_range=surf.u_range,
                   v_range=surf.v_range)


def apply_vector_field(surf, **kwargs):
    """
    Shifts surface by a vector field.

    :type surf: Surface
    """

    if len(kwargs) != 1:
        raise ValueError()

    (argspec, f), *_ = kwargs.items()
    f = _utils.expand_function(f, argspec)

    def transform(sf):
        return lambda u, v: f(*sf(u, v))

    return Surface(sf=transform(surf.sf),
                   u_range=surf.u_range,
                   v_range=surf.v_range)
