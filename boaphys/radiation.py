import numpy as np
from numbers import Number

from . import units as _units
from . import constants as _constants


def radiation_length(Z : Number, A : Number) -> _units.Quantity:
    """Radiation length (a.k.a. X_0)

    The distance over which electrons lose 1/e of their energy.

    See: https://en.wikipedia.org/wiki/Radiation_length

    Returns
    -------
    The length in g/cm^-2
    """

    import numpy as np
    return 1432.8 * A / (Z * (Z + 1) * (11.319 - np.log(Z))) * _units["g/cm^(-2)"]


def bethe_formula(n : _units.Quantity, z : Number, beta : Number, I: _units.Quantity) -> _units.Quantity:
    """Betha formula for energy loss of particle in medium.

    See: https://en.wikipedia.org/wiki/Bethe_formula

    Parameters
    ----------
    n : density of atoms in medium
    z : charge of the moving particle
    beta : speed of the particles (as fraction of c)
    I : mean ionizing potential of the medium

    Returns
    -------
    The energy loss in medium per unit length.

    """
    from numpy import pi, log
    # from constants import c, eps0, e
    from .particles import Electron
    m_e = Electron.rest_mass

    return -(
        4 * pi / Electron.rest_energy *
        (n * z ** 2) / (beta ** 2) *
        (_constants.e.si ** 2 / (4 * pi * _constants.eps0)) ** 2 *
        (log(2 * m_e * _constants.c ** 2 * beta ** 2 / (I * (1 - beta ** 2))) - beta ** 2)
    ).to(_units.MeV / _units.cm)
