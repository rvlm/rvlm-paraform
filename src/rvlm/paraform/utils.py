import rvlm.paraform.autogen as _autogen


def expand_function(f, argspec):
    """
    Expands function `f` to take exactly three arguments and return exactly
    three results. Original `f` may take any non-empty subset of (x, y, z)
    arguments in any order, and return from one to three results. The exact
    parameter layout of `f` is prescribed by `argspec` argument, which is just
    a plain string, formatted like "<RESULTS>_<ARGUMENTS>". For example, if
    `argspec` equals to "xz_yx", it means that `x, z = f(y, x)`. All possible
    values for RESULTS/ARGUMENTS are: "x", "y", "z", "xy", "xz", "yz", "yz",
    "zx", "zy", "xyz", "xzy", "yxz", "yzx", "zxy", and "zyx", total 15. Thus,
    the overall number of possible `argspec` variants is 225.

    This function internally implemented through Python code generation in
    order to support every possible variant of `argspec`.
    """
    return _autogen.expand_function_autogen(f, argspec)
