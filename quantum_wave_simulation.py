import numpy as np
import matplotlib.pyplot as plt

# Constants (natural units: ħ = 1, m = 1)
hbar = 1.0
m = 1.0

# Spatial grid
Nx = 1000
x_min, x_max = -50, 50
x = np.linspace(x_min, x_max, Nx)
dx = x[1] - x[0]

# Time parameters
dt = 0.01
Nt = 500

# Initial Gaussian wave packet
x0 = -10.0      # initial position
k0 = 2.0        # momentum
sigma = 1.0     # width

psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)  # normalize

# Potential (free particle = 0)
V = np.zeros(Nx)

# Laplacian operator (finite difference)
def laplacian(psi):
    return (np.roll(psi, -1) - 2 * psi + np.roll(psi, 1)) / dx**2

# Time evolution using Crank-Nicolson-like step
def evolve(psi):
    return psi + (-1j * hbar / (2 * m)) * laplacian(psi) * dt - 1j * V * psi * dt

# Simulation
for t in range(Nt):
    psi = evolve(psi)

    # Normalize to avoid drift
    psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)

    # Plot every 50 steps
    if t % 50 == 0:
        plt.plot(x, np.abs(psi)**2, label=f"t={t*dt:.2f}")

# Plot results
plt.title("Quantum Wave Packet Evolution")
plt.xlabel("Position")
plt.ylabel("Probability Density")
plt.legend()
plt.show()
