#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

# Constants (natural units: ħ = 1, m = 1)
hbar = 1.0
m = 1.0

# Spatial grid
Nx = 800
x_min, x_max = -50, 50
x = np.linspace(x_min, x_max, Nx)
dx = x[1] - x[0]

# Time parameters
dt = 0.01
Nt = 2000

# Initial Gaussian wave packet
x0 = -10.0
k0 = 2.0
sigma = 1.0

psi = np.exp(-(x - x0)**2 / (2 * sigma**2)) * np.exp(1j * k0 * x)
psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)

# Potential (free particle)
V = np.zeros(Nx)

# Laplacian (finite difference)
def laplacian(psi):
    return (np.roll(psi, -1) - 2 * psi + np.roll(psi, 1)) / dx**2

# Time evolution
def evolve(psi):
    return psi + (-1j * hbar / (2 * m)) * laplacian(psi) * dt - 1j * V * psi * dt

# Setup plot
plt.ion()
fig, ax = plt.subplots()
line, = ax.plot(x, np.abs(psi)**2)

ax.set_xlim(x_min, x_max)
ax.set_ylim(0, 1)
ax.set_title("Quantum Wave Packet Evolution")
ax.set_xlabel("Position")
ax.set_ylabel("Probability Density")

# Simulation loop
for t in range(Nt):
    psi = evolve(psi)

    # Normalize
    psi /= np.sqrt(np.sum(np.abs(psi)**2) * dx)

    # Update plot every few steps
    if t % 5 == 0:
        line.set_ydata(np.abs(psi)**2)
        ax.set_title(f"Time = {t*dt:.2f}")
        plt.pause(0.001)

# Keep window open at the end
plt.ioff()
plt.show()
