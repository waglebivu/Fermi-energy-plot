import numpy as np
import matplotlib.pyplot as plt

# Constants
k_B = 8.617333262145e-5  # Boltzmann constant in eV/K

# Given Fermi energy
E_f = 3.12  # in eV

# Temperatures
temperatures = [0, 50, 100, 150, 300]  # in Kelvin

# Energy range for the plot
energy_range = np.linspace(E_f - 2 * k_B * max(temperatures),
                           E_f + 2 * k_B * max(temperatures), 1000)


# Calculate Fermi-Dirac distribution function
def fermi_dirac_distribution(energy, temperature):
    if temperature == 0:
        # Avoid division by zero by returning a step function
        return np.heaviside(E_f - energy, 0.5)
    else:
        return 1 / (1 + np.exp((energy - E_f) / (k_B * temperature)))


# Plotting
plt.figure(figsize=(8, 6))

for T in temperatures:
    fermi_dist = fermi_dirac_distribution(energy_range, T)
    plt.plot(energy_range, fermi_dist, label=f'Temperature = {T}K')

# Setting labels and title
plt.xlabel('Energy (eV)')
plt.ylabel('Fermi-Dirac Distribution')
plt.title('Fermi Energy Plot for Na at Different Temperatures')
plt.legend()
plt.grid(True)
plt.show()
