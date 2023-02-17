import numpy as np
import matplotlib.pyplot as plt

# Define the variables
viscosity = 0.0027  # dynamic viscosity of blood in Pa s
length = 0.15  # length of vessel in m
pressure = 40*133.332  # pressure difference across vessel in Pa

# Define the radius range
num_points = 1000
radius_min = 0.002  # minimum vessel radius in m
radius_max = 0.003  # maximum vessel radius in m
radius = np.linspace(radius_min, radius_max, num_points)

# Calculate the flow rates for each radius
flow_rate = (((np.pi * radius ** 4) / (8 * viscosity)) * ((pressure) / (length)))*60000
print(flow_rate[0])

# Plot the data
plt.plot(radius, flow_rate)

# Add axis labels and a title
plt.title("Blood Flow Rate vs Vessel Radius")
plt.xlabel("Vessel Radius (m)")
plt.ylabel("Flow Rate (L/min)")

# Show the plot
plt.show()
