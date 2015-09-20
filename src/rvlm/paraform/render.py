import rvlm.paraform.paraform as _pf
import numpy as _np


def render_to_bool_array(obj, start, stop, nums):
    linspaces = []
    for a, b, n in zip(start, stop, nums):
        linspaces.append(_np.linspace(a, b, num=n))

    [xs, ys, zs] = _np.meshgrid(*linspaces)

    vpf = _np.vectorize(obj.pf)
    return vpf(xs, ys, zs)
