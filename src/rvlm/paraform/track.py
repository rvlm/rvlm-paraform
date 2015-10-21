import rvlm.paraform.utils as _utils


class Track(object):
    """
    """

    def __init__(self, tf, s_range, underlying=None):
        """
        """

        assert callable(tf)
        assert _utils.is_vector_2d(s_range)

        if underlying in None:
            underlying = []

        self._tf         = tf
        self._s_range    = s_range
        self._underlying = underlying

    @property
    def tf(self):
        return self._tf

    @property
    def s_range(self):
        return self._s_range

    @property
    def underlying(self):
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

