from . import units as _units


_MeVc2 = _units.MeV / _units.c ** 2
_e = _units.e


class Particle:
    _defaults = {
        "charge": 0 * _e
    }
    
    def __init__(self, name : str, **kwargs):
        self.properties = Particle._defaults.copy()
        self.properties.update(kwargs)
        
    @property
    def rest_mass(self) -> _units.Quantity:
        return self.properties["rest_mass"]
        
    @property
    def rest_energy(self) -> _units.Quantity:
        return self.rest_mass * _units.c ** 2
        
    def __call__(self, *args, **kwargs) -> "DynamicParticle":
        return DynamicParticle(self, *args, **kwargs)
    
    @property
    def charge(self) -> _units.Quantity:
        return self.properties["charge"]
                
        
class DynamicParticle:
    def __init__(self, particle : Particle, ekin):
        self.particle = particle
        self.kinetic_energy = ekin
        
    def __getattr__(self, name):
        return getattr(self.particle, name)
        
    @property
    def total_energy(self) -> _units.Quantity:
        return self.particle.rest_energy + self.kinetic_energy
        
    @property
    def total_mass(self) -> _units.Quantity:
        return self.total_energy / _units.c ** 2
        
    @property
    def gamma(self) -> float:
        return float(self.total_energy / self.particle.rest_energy)
        
    @property
    def beta(self) -> float:
        import numpy as np
        return float(np.sqrt(1 - 1 / self.gamma ** 2))
        
    @property
    def velocity(self) -> _units.Quantity:
        return self.beta * _units.c        
        
        
Proton = Particle("proton",
                  rest_mass=938.2720813 * _MeVc2,
                  charge=1 * _e
                  )

Neutron = Particle("neutron",
                  rest_mass=938.2720813 * _MeVc2,
                  charge=1 * _e
                  )

Photon = Particle("photon", rest_mass=0 * _MeVc2)

Electron = Particle("electron",
                    rest_mass=0.5109989461 * _MeVc2,
                    charge=-1 * _e
                    )

Positron = Particle("positron",
                    rest_mass=0.5109989461 * _MeVc2,
                    charge=1 * _e
                    )



    
    
    