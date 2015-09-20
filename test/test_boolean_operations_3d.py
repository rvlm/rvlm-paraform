import os
import numpy as np
import rvlm.paraform.all as pf


def test_boolean_operations_3d():

    def render(obj):
        grid = np.meshgrid(np.linspace(-2, 2, 50),
                           np.linspace(-2, 2, 50),
                           np.linspace(-2, 2, 50))
        vpf = np.vectorize(obj.pf)
        return vpf(*grid)

    def load(name):
        real_name = os.path.join(os.path.dirname(__file__), "renders", name)
        with np.load(real_name) as f:
            return f['arr_0']

    cube = pf.cube(2.0)
    ball = pf.Ball(2.4)

    # Check mathematical properties.
    assert (render(cube | cube)        == render(cube)).all()
    assert (render(cube & cube)        == render(cube)).all()
    assert render(cube ^ cube).any()   == False

    # Compare to saved renders.
    assert (render(cube & ball) == load("cube_and_ball.npz")).all()
    assert (render(cube | ball) == load("cube_or_ball.npz")).all()
    assert (render(cube ^ ball) == load("cube_xor_ball.npz")).all()
    assert (render(cube - ball) == load("cube_minus_ball.npz")).all()
    assert (render(ball - cube) == load("ball_minus_cube.npz")).all()


test_boolean_operations_3d()