import matplotlib.pyplot as plt
import numpy as np

# Define the velocity gradients
du_dy = np.linspace(0, 1.5, 100)

# Define the viscosities for each fluid type
mu_ideal = 0
mu_real = 0.1 + 0.1 * du_dy
mu_newtonian = 1.26
mu_non_newtonian = 1 + 0.5 * du_dy ** 0.5
mu_incompressible = 1.5
d = np.linspace(0.6, 1.5, 100)
mu_compressible = 1.2 + 1.2*d


# Calculate the shear stress for each fluid type and velocity gradient
shear_stress_ideal = mu_ideal * du_dy
shear_stress_newtonian = mu_newtonian * du_dy
shear_stress_non_newtonian = mu_non_newtonian * du_dy
shear_stress_real = mu_real * du_dy
shear_stress_incompressible = mu_incompressible * du_dy
shear_stress_compressible = mu_compressible * du_dy

# Plot the shear stress vs velocity gradient for each fluid type
plt.plot(du_dy, shear_stress_ideal, label='Ideal Fluid')
plt.plot(du_dy, shear_stress_newtonian, label='Newtonian Fluid')
plt.plot(du_dy, shear_stress_non_newtonian, label='Non-Newtonian Fluid')
plt.plot(du_dy, shear_stress_real, label='Real Fluid')
plt.plot(du_dy, shear_stress_incompressible, label='Incompressible Fluid')
plt.plot(du_dy, shear_stress_compressible, label='Compressible Fluid')

# Add labels, title and legend
plt.xlabel('Velocity Gradient')
plt.ylabel('Shear Stress')
plt.title('Shear Stress vs Velocity Gradient for Different Fluids')
plt.legend()

# Set the y-axis limit
plt.ylim(0, 2)

# Show the plot
plt.show()
