r"""
Helper functions
================

This document describes functions from RVLM Paraform project, which get
available after the following module import:

.. code-block:: python

    import rvlm.paraform.utils

Despite this module isn't for internal use only, it's recommended for library
user to rely on its content with extra caution, as some helper functions may
get eventually removed.

This module is a helper in nature, so it's not devoted to a narrow specific
topic. Instead, many topics comes here, each having it's own section in this
documentation.


Vector operations
-----------------

This section contains operations on vectors in tri-dimensional space. Supposing
that an orthonormal Cartesian coordinate system is present, each vector is
essentially an ordered triplet of real numbers:

 .. math::

    \vec{v} = (v_x, v_y, v_z).

In Python this triplet can be represented as tuple of list. The library allows
both of them to be passed as parameters, but the tuple form is preferred for
its immutability. All vectors the library calculates by itself and return to
user are always tuples.

.. autofunction:: cross_product
.. autofunction:: unit_vector

Parameter validation
--------------------

.. autofunction:: is_number
.. autofunction:: is_vector_2d
.. autofunction:: is_vector_3d

Miscellaneous
-------------

 .. autofunction:: expand_function

"""
import math as _math
import rvlm.paraform.autogen as _autogen


def cross_product(a, b):
    r"""
    Calculates a cross product (or vector product) of two vectors in
    tri-dimensional Cartesian coordinates.

    :type a: (float, float, float) | list[float]
    :parameter a:
        Vector :math:`\vec{a}` coordinates :math:`(a_x, a_y, a_z)` as tuple
        or list.

    :type b: (float, float, float) | list[float]
    :parameter b:
        Vector :math:`\vec{b}` coordinates :math:`(b_x, b_y, b_z)` as tuple
        or list.

    :rtype: (float, float, float)
    :returns:
        Vector product :math:`[\vec{a} \times \vec{b}]`, calculated using the
        following formula:

        .. math::

           [\vec{a} \times \vec{b}] = \left|
               \begin{array}{ccc}
                   \vec{i} & \vec{j} & \vec{k} \\
                   a_x & a_y & a_z \\
                   b_x & b_y & b_z
               \end{array}  \right|.
    """
    return (a[1]*b[2] - a[2]*b[0],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0])


def unit_vector(v):
    r"""
    Returns vector, codirectional to :math:`\vec{v}`, but length of 1.

    :type v: (float, float, float) | list[float]
    :parameter v:
        Vector :math:`\vec{v}` coordinates :math:`(v_x, v_y, v_z)` as tuple
        or list.

    :rtype: (float, float, float)
    :returns:
        Unit vector (or *orth* vector) :math:`\vec{e}_\vec{v}`, calculated as
        the following:

        .. math::

           \vec{e}_\vec{a} = \frac{1}{|\vec{v}|} \vec{v}, \quad
           |\vec{v}| = \sqrt{v_x^2 + v_y^2 + v_z^2}.

    .. seealso::

        https://en.wikipedia.org/wiki/Unit_vector
    """
    (vx, vy, vz) = v
    norm = _math.sqrt(vx*vx + vy*vy + vz*vz)
    return (vx/norm, vy/norm, vz/norm)


def is_number(x):
    """
    """
    return type(x) == float or type(x) == int


def is_vector_2d(v):
    """
    """
    return (v is not None
              and (type(v) == list or type(v) == tuple)
              and len(v) == 2
              and is_number(v[0])
              and is_number(v[1]))


def is_vector_3d(v):
    """
    """
    return (v is not None
              and (type(v) == list or type(v) == tuple)
              and len(v) == 3
              and is_number(v[0])
              and is_number(v[1])
              and is_number(v[2]))


def expand_function(f, argspec):
    """
    Expands function `f` to take exactly three arguments and return exactly
    three results. Original `f` may take any non-empty subset of (x, y, z)
    arguments in any order, and return from one to three results. The exact
    parameter layout of `f` is prescribed by `argspec` argument, which is just
    a plain string, formatted like "<RESULTS>_<ARGUMENTS>".

    For example, if `argspec` equals to "xz_yx", it means that `x, z = f(y, x)`
    or, more specifically:

    .. code-block:: python

        def expand_function(f, "xz_yx"):
            def result(x, y, z):
                x, z = f(y, z)
                return x, y, z

            return result

    All possible values for RESULTS (or ARGUMENTS) are: "x", "y", "z", "xy",
    "xz", "yz", "yz", "zx", "zy", "xyz", "xzy", "yxz", "yzx", "zxy", and "zyx",
    total 15. Thus, the overall number of possible `argspec` variants is 225.

    This function internally implemented through Python code generation in
    order to support every possible variant of `argspec`.
    """
    return _autogen.expand_function_autogen(f, argspec)
