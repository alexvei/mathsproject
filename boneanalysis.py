import numpy as np
from scipy.linalg import solve
import matplotlib.pyplot as plt

# Define mesh properties
length = 1.0  # Length of the bone
num_elements = 10  # Number of elements
element_length = length / num_elements

# Create node coordinates
nodes = np.linspace(0, length, num_elements + 1)

# Create connectivity array
elements = np.column_stack([np.arange(num_elements), np.arange(1, num_elements + 1)])

# Assign material properties
elastic_modulus = 10e6  # Elastic modulus of the bone material
poisson_ratio = 0.3  # Poisson's ratio of the bone material
density = 1.0  # Density of the bone material

# Apply boundary conditions
fixed_nodes = [0]  # Fix the first node
load_values = [1000.0, 5000.0, 10000.0]  # Applied load values

# Initialize arrays for displacements
displacements = np.zeros((num_elements + 1, len(load_values)))

# Loop over different loads
for load_idx, applied_load in enumerate(load_values):

    # Define global force vector
    force = np.zeros(len(nodes))
    force[-1] = applied_load

    # Assemble the global stiffness matrix and load vector
    num_nodes = len(nodes)
    stiffness_matrix = np.zeros((num_nodes, num_nodes))

    for element in elements:
        node_i, node_j = element
        x_i, x_j = nodes[node_i], nodes[node_j]
        element_length = x_j - x_i

        # Compute element stiffness matrix
        k = (elastic_modulus * element_length) / (1 - poisson_ratio ** 2)
        k /= np.array([[1, -poisson_ratio], [-poisson_ratio, 1]])

        # Assemble element stiffness matrix into global stiffness matrix
        stiffness_matrix[node_i:node_j + 1, node_i:node_j + 1] += k

    # Apply boundary conditions to the global stiffness matrix and load vector
    for fixed_node in fixed_nodes:
        stiffness_matrix[fixed_node, :] = 0.0
        stiffness_matrix[fixed_node, fixed_node] = 1.0
        force[fixed_node] = 0.0

    # Solve the system of equations
    displacements[:, load_idx] = solve(stiffness_matrix, force)

# Visualize the deformed bone for different loads in a single plot
plt.figure()
plt.plot(nodes, np.zeros_like(nodes), 'k--', label='Initial')

for load_idx, applied_load in enumerate(load_values):
    plt.plot(nodes, displacements[:, load_idx], label=f'Load: {applied_load}')

plt.xlabel('Position')
plt.ylabel('Displacement')
plt.legend()
plt.title('Deformation of the Bone for Different Loads')
plt.show()
