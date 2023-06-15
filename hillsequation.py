import numpy as np
import matplotlib.pyplot as plt

def hill_muscle(length, velocity, max_force, damping):
    # Parameters
    optimal_length = 1.0  # Optimal length of the muscle
    force_length_factor = 0.5  # Force-length factor
    force_velocity_factor = 0.1  # Force-velocity factor

    # Force-length relationship
    force_length = (1 - force_length_factor * (length - optimal_length) ** 2) * max_force
    force_length = max(0, force_length)  # Ensure force is non-negative

    # Force-velocity relationship
    if velocity > 0:
        force_velocity = (1 - force_velocity_factor * (velocity / max_force)) * max_force
    else:
        force_velocity = (1 + force_velocity_factor * (velocity / max_force)) * max_force

    # Total force
    force = force_length * force_velocity - damping * velocity

    return force

# Simulation parameters
num_points = 100
lengths = np.linspace(0.5, 1.5, num_points)
velocities = np.linspace(-1, 1, num_points)

# Calculate forces for each length and velocity combination
forces = np.zeros((num_points, num_points))
for i, length in enumerate(lengths):
    for j, velocity in enumerate(velocities):
        forces[i, j] = hill_muscle(length, velocity, max_force=1.0, damping=0.1)

# Plotting
plt.figure(figsize=(12, 8))
plt.imshow(forces, extent=[min(velocities), max(velocities), min(lengths), max(lengths)],
           aspect='auto', origin='lower', cmap='coolwarm')
plt.colorbar(label='Force')
plt.xlabel('Velocity')
plt.ylabel('Length')
plt.title("Hill's Muscle Equation")
plt.show()
