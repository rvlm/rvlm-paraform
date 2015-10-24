"""
Parametric curves (tracks)
==========================

In this library context, *one-parametric curve* (or *track*) is one-dimensional
entity, defined by it's *track function*:

.. math::

   \\DeclareMathOperator{\\tf}{tf}
   \\vec{r} = \\tf(s), \\quad s_1 \\le s \\le s_2

where :math:`s` is a freely varying curve parameter. Track function produces a
set of :math:`\\vec{r}` vectors, which describe the curve location in space.
Note that, unlike pure math, parameter varying range is two-sides limited,
infinite curve are not allowed, so it worth nothing having unlimited parameter
range.

Curve rendering is always an approximation. The :math:`[s_1; s_2]` ranges is
divided into a number of segments by evenly spaced :math:`s_i` points. For each
:math:`s_i` its corresponding vector :math:`\\vec{r}_i` is calculated:

.. math:: \\vec{r}_i = \\tf(s_i).

Thus the curve is treated as a number of line segments
:math:`[\\vec{r}_i, \\vec{r}_{i+1}]`, located in a tridimentional space. When
the curve is requested to be paint on a display of rendered into a computational
lattice all operations a really performed on its line segments. So, it's really
important to choose an appropriate step for :math:`s_i` points: having too
distant points would produce an image of poor quality, having to close points
would significantly increase time to display or render. Note that the nature of
:math:`\\tf(s)` function itself is the first factor to take into consideration
when estimating that step value.

"""
import rvlm.paraform.utils as _utils


class Track(object):
    """
    Represents track of arbitrary shape in the most generic form as described
    above. This class is immutable, so it allow no further modification once
    created.
    """

    def __init__(self, tf, s_range, underlying=None):
        """
        It requires only track function :math:`\\tf(s)` and :math:`[s_1; s_2]`
        range to be passed as arguments.

        :type tf: (float) -> (float, float, float)
        :parameter tf:
            Track function :math:`\\tf(s)` as Python callable object. It may
            be, for example, lambda expression or class instance with
            `__call__` method overridden. This way or another, it must allow
            calling with single floating point parameter, returning a tuple of
            three Cartesian coordinates :math:`(x, y, z)`, which represent
            :math:`\\vec{r}` vector value.

        :type s_range: (float, float) | list[float]
        :parameter s_range:
            Track function parameter range as :math:`[s_1, s_2]` pair of
            numbers. This pair can be passed as a tuple or as a list, depending
            on user preference.

        :type underlying: list[Track] | tuple
        :param underlying:
            List of tracks this track is based on. Currently this list is just
            stored as class property to make object tree inspection possible.
            Normally this property should never be accessed from within of the
            class itself, because all parameters needed for :math:`\\tf`
            function computation are usually referred as direct closures.
        """

        assert callable(tf)
        assert _utils.is_vector_2d(s_range)

        if underlying in None:
            underlying = []

        self._tf         = tf
        self._s_range    = tuple(s_range)
        self._underlying = underlying

    @property
    def tf(self):
        """
        Gets track function :math:`\\tf(s)` which was passed to constructor at
        the object creation. This property is read only.

        :rtype: callable
        """
        return self._tf

    @property
    def s_range(self):
        """
        Gets range of allowed values for track function parameters. This range
        is always a tuple even if a list was originally passed as constructor
        parameter. This property is immutable and read only.

        :rtype: (float, float)
        """
        return self._s_range

    @property
    def underlying(self):
        """
        """
        return self._underlying


class Axis(Track):
    """
    """

    def __init__(self, point, direction):
        """
        """

        assert _utils.is_vector_3d(point)
        assert _utils.is_vector_3d(direction)

        x0, y0, z0 = point
        ax, ay, az = direction

        def tf(s):
            return x0 + ax * s, y0 + ay * s, z0 + az * s

        self._point     = point
        self._direction = direction

        super().__init__(tf=tf, s_range=[0, 1])

    @property
    def point(self):
        return self._point

    @property
    def direction(self):
        return self._direction
