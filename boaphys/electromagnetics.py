from . import units as _units


class MagneticField:
    @staticmethod
    def dipole_bending_field(particle, r : _units.Quantity, relativistic=True) -> _units.Quantity:
        mass = particle.total_mass if relativistic else particle.rest_mass
        return mass * particle.velocity / (particle.charge * r)
    
    @staticmethod
    def dipole_bending_radius(particle, B : _units.Quantity, relativistic=True) -> _units.Quantity:
        mass = particle.total_mass if relativistic else particle.rest_mass
        return mass * particle.velocity / (particle.charge * B)
        

__all__ = ["MagneticField"]