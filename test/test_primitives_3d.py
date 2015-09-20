from rvlm.labhelpers.extnumpy import filter_along_axis
from rvlm.labhelpers.tabular  import tabularmf
from rvlm.paraform.all        import *
from rvlm.paraform.render     import render_to_bool_array
from helpers                  import check_render
import numpy


def cube_minus_ball(edge, diameter):
    return cube(edge).minus(Ball(diameter))


def test_primitive_renders():
    assert check_render(
        cube_minus_ball(2.0, 2.4), "cube_minus_ball_2.0_2.4.npz")




[xs, ys, zs] = numpy.meshgrid(numpy.linspace(-2, 2), numpy.linspace(-2, 2), numpy.linspace(-2, 2))
#vpf = numpy.vectorize(mimi.pf)

#arr = vpf(xs, ys, zs)
table = tabularmf([xs, ys, zs])
pf = mimi.pf

table = numpy.array(list(filter(lambda t: pf(t[0], t[1], t[2]), table)))

numpy.savetxt("tst.txt", table)
# numpy.savez("test.npz", numpy.hstack())
