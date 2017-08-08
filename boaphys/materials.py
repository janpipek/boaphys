from . import units as _units
from . import constants as _constants


class Material:
    def __init__(self, Z, A, density, I=None):
        self.Z = Z
        self.A = A
        self.density = density
        self.I = I

    @property
    def electron_density(self):
        return (_constants.N_A * self.Z * self.density / (self.A * _units.g / _units.mol)).to(1 / _units.cm**3)


WATER = Material(8, 18, 1 * _units.g / _units.cm ** 3, I=12.621 * _units.eV)
