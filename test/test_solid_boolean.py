import os
import numpy
import rvlm.paraform.solid as pfs


def test_solid_boolean_operations():

    def render(obj) -> numpy.ndarray:
        grid = numpy.meshgrid(numpy.linspace(-2, 2, 50),
                              numpy.linspace(-2, 2, 50),
                              numpy.linspace(-2, 2, 50))

        vpf = numpy.vectorize(obj.pf)
        return vpf(*grid)

    def load(name) -> numpy.ndarray:
        real_name = os.path.join(os.path.dirname(__file__), "renders", name)
        with numpy.load(real_name) as f:
            return f['arr_0']

    cube = pfs.Cuboid(2.0, 2.0, 2.0)
    ball = pfs.Ellipsoid(2.4, 2.4, 2.4)

    # Check mathematical properties.
    assert numpy.all(render(cube | cube) == render(cube))
    assert numpy.all(render(cube & cube) == render(cube))
    assert numpy.any(render(cube ^ cube)) == False

    # Compare to saved renders.
    assert numpy.all(render(cube & ball) == load("cube_and_ball.npz"))
    assert numpy.all(render(cube | ball) == load("cube_or_ball.npz"))
    assert numpy.all(render(cube ^ ball) == load("cube_xor_ball.npz"))
    assert numpy.all(render(cube - ball) == load("cube_minus_ball.npz"))
    assert numpy.all(render(ball - cube) == load("ball_minus_cube.npz"))


if __name__ == "__main__":
    test_solid_boolean_operations()
