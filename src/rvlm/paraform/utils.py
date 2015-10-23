"""
Miscellaneous helper functions
==============================

"""
import math as _math
import rvlm.paraform.autogen as _autogen


def cross_product(a, b):
    """
    """
    return [a[1]*b[2] - a[2]*b[0],
            a[2]*b[0] - a[0]*b[2],
            a[0]*b[1] - a[1]*b[0]]


def unit_vector(a):
    """
    """
    [ax, ay, az] = a
    norm = _math.sqrt(ax*ax + ay*ay + az*az)
    return [ax/norm, ay/norm, az/norm]


# Arguments checks for assertions


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
