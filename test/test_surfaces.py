import rvlm.paraform.surface as sf
import rvlm.paraform.render  as pr
import numpy


def save_surface(fn, surf):
    points = []
    for u in pr.iterate_range((0, 1), 100):
        for v in pr.iterate_range((0, 1), 100):
            points.append(surf.sf(u, v))

    numpy.savetxt(fn, numpy.array(points))


def test_surfaces():

    surf = sf.Oxy.shift(f_xy=lambda x, y: (x-y)**2)
    save_surface("test_surf.txt", surf)


test_surfaces()