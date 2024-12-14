#Solving 1D Heat Equation

import matplotlib.pyplot as plt
import math

# Parameters
L = 1.0          # Length of the rod
T = 0.1          # Total time for simulation
nx = 50          # Number of spatial grid points
nt = 1000        # Number of time steps
alpha = 0.01     # Thermal diffusivity

dx = L / (nx - 1)    # Spatial step size
dt = T / nt          # Time step size

# Stability condition
r = alpha * dt / dx**2
if r > 0.5:
    raise ValueError("Stability condition violated: reduce dt or increase dx")

# Initialize spatial grid and temperature distribution
x = [i * dx for i in range(nx)]
u = [0.0] * nx  # Initial temperature is zero everywhere
u_new = [0.0] * nx

# Initial condition: u(x, 0) = sin(pi * x)
for i in range(nx):
    u[i] = math.sin(math.pi * x[i])

# Boundary conditions: u(0, t) = u(L, t) = 0
u[0] = u[-1] = 0

# Time-stepping loop
for n in range(nt):
    for i in range(1, nx - 1):
        u_new[i] = u[i] + r * (u[i+1] - 2*u[i] + u[i-1])
    u = u_new[:]  # Update solution (copy values)

# Plot the results
plt.figure(figsize=(8, 6))
plt.plot(x, u, label=f"Time = {T:.2f} s")
plt.title("Heat Equation Solution ")
plt.xlabel("Position (x)")
plt.ylabel("Temperature (u)")
plt.grid()
plt.legend()
plt.show()
