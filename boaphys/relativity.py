from . import units, constants
from .particles import DynamicParticle
from multipledispatch import dispatch


@dispatch(units.Quantity)        
def beta(value : units.Quantity) -> float:
    return float(value / constants.c)


@dispatch(DynamicParticle)
def beta(particle : DynamicParticle) -> float:
    return particle.beta
    

def gamma(arg) -> float:
    import numpy as np
    1 / np.sqrt(1 - beta(value) ** 2)