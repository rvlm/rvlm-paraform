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

    # This ugly function is here due to PyCharm bug, preventing it from
    # understanding numpy array's equality comparison.
    # https://youtrack.jetbrains.com/issue/PY-17350
    def eq(array1: numpy.ndarray, array2: numpy.ndarray) -> bool:
        # noinspection PyUnresolvedReferences
        return (array1 == array2).all()

    cube = pfs.Cuboid(2.0, 2.0, 2.0)
    ball = pfs.Ellipsoid(2.4, 2.4, 2.4)

    # Check mathematical properties.
    assert eq(render(cube | cube), render(cube))
    assert eq(render(cube & cube), render(cube))
    assert not render(cube ^ cube).any()

    # Compare to saved renders.
    assert eq(render(cube & ball), load("cube_and_ball.npz"))
    assert eq(render(cube | ball), load("cube_or_ball.npz"))
    assert eq(render(cube ^ ball), load("cube_xor_ball.npz"))
    assert eq(render(cube - ball), load("cube_minus_ball.npz"))
    assert eq(render(ball - cube), load("ball_minus_cube.npz"))


if __name__ == "__main__":
    test_solid_boolean_operations()
