from boaphys.radiation import bethe_formula
from boaphys.particles import Particle
from boaphys import units, constants
from boaphys.materials import WATER

def show_bragg_peak(ekin=187 * 12 * units.MeV):
    """Shows a theoretical Bragg peak for carbon ions calculated from Bethe formula."""
    CarbonIon = Particle("carbon", rest_mass=12 * constants.u, z = 6)
    ion = CarbonIon(ekin)
    n = WATER.electron_density

    import matplotlib.pyplot as plt

    ion = CarbonIon(ekin)

    step = 0.1 * units.mm

    xs = []
    edep = []
    x = 0.0

    while ion.kinetic_energy > 0:
        dE_dx = bethe_formula(n=WATER.electron_density, z=ion.particle.z, beta=ion.beta, I=WATER.I).to(units.keV / units.um)
        dE = step * dE_dx
        x = x + step
        new_ekin = ion.kinetic_energy + dE
        ion.kinetic_energy = new_ekin
        xs.append(x.value)
        edep.append(-dE.value)

    xs.append((x + step).value)
    edep.append(0)

    fig, ax = plt.subplots()
    ax.plot(xs, edep)
    ax.set_xlabel("depth [mm]")
    ax.set_ylabel("dE/dx [MeV/mm]")
    ax.set_title("Bragg peak for carbon ion in water (theoretical)")
    plt.show()


if __name__ == "__main__":
    show_bragg_peak()
