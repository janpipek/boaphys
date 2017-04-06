from . import (units, constants)
from multipledispatch import dispatch


def escape_velocity(mass : units.Quantity, radius : units.Quantity) -> units.Quantity:
    import numpy as np
    return np.sqrt(2 * constants.G * mass / radius).to("km/s")
    
    
def hyperbolic_excess_speed(mass, radius, v0) -> units.Quantity:
    return np.sqrt(v0 ** 2 - escape_velocity(mass, radius) ** 2).to("km/s")
    
    
class SpaceBody:
    def __init__(self, radius, mass):
        self.mass = mass
        self.radius = radius
        
    @property
    def escape_velocity(self):
        return escape_velocity(self.mass, self.radius)
        
    @property
    def surface_gravity(self):
        return (constants.G * self.mass / self.radius ** 2).to("m/s**2")
        
        
class Star(SpaceBody):
    def __init__(self, name, radius=None, mass=None, distance=None):
        super(Star, self).__init__(radius, mass)
        self.name = name
        self.distance = distance

        
class Planet(SpaceBody):
    def __init__(self, name, radius, mass):
        super(Planet, self).__init__(radius, mass)
        self.name = name


Sun = Star("Sun",
           mass=1.98855e30 * units.kg,
           radius=695700 * units.km,
           distance=1 * units.AU)

    
Earth = Planet("Earth",
               mass=5.97237e24 * units.kg,
               radius=6378.1 * units.km
               )

@dispatch(units.Quantity)
def schwarzchild_radius(mass : units.Quantity) -> units.Quantity:
    """Radius of a sphere of the same mass with escape velocity equivalent to speed of light."""
    return (2 * constants.G * mass / (constants.c ** 2)).to("km")
    
@dispatch(SpaceBody)
def schwarzchild_radius(o : SpaceBody) -> units.Quantity:
    return schwarzchild_radius(o.mass)   
    
    

    

stars = {
    "Betelgeuse": Star("Betelgeuse", distance=642.5 * units.lightyear)
}
