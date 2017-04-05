from . import units


class MagneticField:
    @staticmethod
    def dipole_bending_field(particle, r : units.Quantity, relativistic=True) -> units.Quantity:
        mass = particle.total_mass if relativistic else particle.rest_mass
        return (mass * particle.velocity / (particle.charge * r)).to("tesla")
    
    @staticmethod
    def dipole_bending_radius(particle, B : units.Quantity, relativistic=True) -> units.Quantity:
        mass = particle.total_mass if relativistic else particle.rest_mass
        return (mass * particle.velocity / (particle.charge * B)).to("m")
        

__all__ = ["MagneticField"]