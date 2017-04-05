from . import units as _units
from .particles import DynamicParticle
from multipledispatch import dispatch

# Some units
c = _units.c
keV = _units["keV"]
MeV = _units["MeV"]
GeV = _units["GeV"]


@dispatch(_units.Quantity)        
def beta(value : _units.Quantity) -> float:
    return float(value / _units.c)


@dispatch(DynamicParticle)
def beta(particle : DynamicParticle) -> float:
    return particle.beta
    

def gamma(arg) -> float:
    import numpy as np
    1 / np.sqrt(1 - beta(value) ** 2)