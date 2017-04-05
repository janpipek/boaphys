from . import (units, constants)


def escape_velocity(mass : units.Quantity, radius : units.Quantity) -> units.Quantity:
    import numpy as np
    return np.sqrt(2 * constants.G * mass / radius)
    
    
def hyperbolic_excess_speed(mass, radius, v0) -> units.Quantity:
    return np.sqrt(v0 ** 2 - escape_velocity(mass, radius) ** 2)