from boaphys.particles import Proton
from boaphys import units
from boaphys.electromagnetics import MagneticField
import numpy as np


radius = 2.57 * units.m

print("E\tB_nonrel\tB_rel")
for energy in range(5, 100, 5):
    proton = Proton(energy * units.MeV)
    B_rel = float(MagneticField.dipole_bending_field(proton, radius) / units.tesla)
    velocity_nonrel = np.sqrt(2 * proton.kinetic_energy / proton.rest_mass)
    B_nonrel = float(proton.rest_mass * velocity_nonrel / (proton.charge * radius) / units.tesla)
    print("{0}\t{1:.8f}\t{2:.8f}".format(energy, B_nonrel, B_rel))
    