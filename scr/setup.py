import numpy as np


class Sheet:
    def __init__(self, extentX: float, extentY: float, Nx: int, Ny: int):
        self.dx = extentX / Nx
        self.dy = extentY / Ny

        self.x = self.dx * (np.arange(Nx) - Nx // 2)
        self.y = self.dy * (np.arange(Ny) - Ny // 2)
        self.xx, self.yy = np.meshgrid(self.x, self.y)
        self.Nx = int(Nx)
        self.Ny = int(Ny)
        self.mask = np.zeros((self.Ny, self.Nx))

    def rectangular_slit(self, x0: float, y0: float, lx: float, ly: float):
        self.mask += np.select(
            [
                ((self.xx > (x0 - lx / 2)) & (self.xx < (x0 + lx / 2)))
                & ((self.yy > (y0 - ly / 2)) & (self.yy < (y0 + ly / 2))),
                True,
            ],
            [1, 0],
        )


class Screen:
    def __init__(
        self,
        extentX: float,
        extentY: float,
        Nx: int,
        Ny: int,
        Distance: float,
        wavelength: float,
    ):
        self.dx = Distance * wavelength / extentX
        self.dy = Distance * wavelength / extentY

        self.x = self.dx * (np.arange(Nx) - Nx // 2)
        self.y = self.dy * (np.arange(Ny) - Ny // 2)
        self.xx, self.yy = np.meshgrid(self.x, self.y)
        self.Nx = int(Nx)
        self.Ny = int(Ny)
        self.pupil = np.zeros((self.Ny, self.Nx))

    def construct_pupil(self, x0: float, y0: float, lx: float, ly: float):
        self.pupil += np.select(
            [
                ((self.xx > (x0 - lx / 2)) & (self.xx < (x0 + lx / 2)))
                & ((self.yy > (y0 - ly / 2)) & (self.yy < (y0 + ly / 2))),
                True,
            ],
            [1, 0],
        )
