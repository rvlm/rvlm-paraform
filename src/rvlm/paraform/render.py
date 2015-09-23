import numpy as _np


def render_to_bool_array(obj, ranges, nums):
    linspaces = []
    for (a, b), n in zip(ranges, nums):
        linspaces.append(_np.linspace(a, b, num=n))

    [xs, ys, zs] = _np.meshgrid(*linspaces)

    vpf = _np.vectorize(obj.pf)
    return vpf(xs, ys, zs)


# TODO: Find proper way to do it
def tpl(*xs):
    return tuple(xs)


def head(xs):
    return xs[0]


def tail(xs):
    return xs[1:]


def iterate_range(rng, num):
    """

    :param start:
    :param stop:
    :param num:
    :return:

        >>> list(iterate_range((0, 1), num=5))
        [0.0, 0.25, 0.5, 0.75, 1.0]
        >>> list(iterate_range((1, 0), num=5))
        [1.0, 0.75, 0.5, 0.25, 0.0]
        >>> list(iterate_range((0, 0), num=5))
        [0.0, 0.0, 0.0, 0.0, 0.0]
    """
    a, b = rng
    delta = (b - a) / (num - 1)
    for i in range(num):
        yield a + delta*i


def iterate_ranges(ranges, nums):
    """

    :param ranges:
    :param nums:
    :return:

        >>> from pprint import pprint
        >>> pprint(list(iterate_ranges([(0, 1), (0, 1)], [2, 5])))
        [(0.0, 0.0),
         (0.0, 0.25),
         (0.0, 0.5),
         (0.0, 0.75),
         (0.0, 1.0),
         (1.0, 0.0),
         (1.0, 0.25),
         (1.0, 0.5),
         (1.0, 0.75),
         (1.0, 1.0)]


    """
    if len(ranges) <= 0:
        return None
    elif len(ranges) == 1:
        yield from iterate_range(ranges[0], nums[0])
    else:
        (a, b), *tail_ranges = ranges
        num,    *tail_nums   = nums

        for x in iterate_range((a, b), num):
            for rest in iterate_ranges(tail_ranges, tail_nums):
                yield (x,) + (rest,)


# TODO: Ad-hoc
def iterate_ranges3(ranges, nums):
    for x in iterate_range(ranges[0], nums[0]):
        for y in iterate_range(ranges[1], nums[1]):
            for z in iterate_range(ranges[2], nums[2]):
                yield (x, y, z)


def render_to_points_array(obj, ranges, nums):
    """

    :param obj:
    :param ranges:
    :param nums:
    :return:

    """

    pf = obj.pf
    for coords in iterate_ranges3(ranges, nums):
        if pf(*coords):
            yield coords
