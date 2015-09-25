import rvlm.paraform.utils as _utils


class Surface(object):

    def __init__(self, sf):
        self.urange = None
        self.vrange = None
        self.sf = sf

    def scale(self, **kwargs):
        return scale(self, **kwargs)

    def shift(self, **kwargs):
        return shift(self, **kwargs)


def shift(surf, **kwargs):
    """
    """
    if len(kwargs) != 1:
        raise ValueError()

    (argspec, f), *_ = kwargs.items()
    f = _utils.expand_function(f, argspec)

    def transform(sf):
        return lambda u, v: f(*sf(u, v))

    return Surface(sf=transform(surf.sf))
