import rvlm.paraform.solid as pfs
import numpy as np
import netCDF4 as ncd


def renderToArray(solid, xs, ys, zs):

    probeFunc = solid.probe
    def func(p):
        sd, mat = probeFunc(p)
        if sd >= 0.0:
            mat = pfs.Material()

        return np.array([mat.epsilon, mat.mu, mat.sigma, mat.sigmaH])

    grid = np.meshgrid(xs, ys, zs)
    grid = np.stack(grid, axis = -1)
    return np.apply_along_axis(func, -1, grid)


def saveToNetCDF(arr, fileName):
    dataset = ncd.Dataset(fileName, 'w')
    dataset.createDimension('Nx', arr.shape[0])
    dataset.createDimension('Ny', arr.shape[1])
    dataset.createDimension('Nz', arr.shape[2])

    dims = ('Nx', 'Ny', 'Nz')
    dataset.createVariable('epsilon', float, dims)
    dataset.createVariable('mu',      float, dims)
    dataset.createVariable('sigma',   float, dims)
    dataset.createVariable('sigmaH',  float, dims)
    dataset.variables['epsilon'][:, :, :] = arr[:, :, :, 0]
    dataset.variables['mu']     [:, :, :] = arr[:, :, :, 1]
    dataset.variables['sigma']  [:, :, :] = arr[:, :, :, 2]
    dataset.variables['sigmaH'] [:, :, :] = arr[:, :, :, 3]
    dataset.close()


if __name__ == '__main__':
    ball = pfs.Ellipsoid([0.10, 0.10, 0.10], material = pfs.Material(epsilon=1.5))
    arr = renderToArray(ball,
        np.linspace(-0.5, 0.5, 50),
        np.linspace(-0.5, 0.5, 50),
        np.linspace(-0.5, 0.5, 50))

    saveToNetCDF(arr, 'test_ball.nc')
