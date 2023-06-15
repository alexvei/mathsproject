import numpy as np
import matplotlib.pyplot as plt
# Constants
Cm = 1.0  # Membrane capacitance (uF/cm^2)
ENa = 50.0  # Sodium ion reversal potential (mV)
EK = -77.0  # Potassium ion reversal potential (mV)
EL = -54.387  # Leakage ion reversal potential (mV)
gNa = 120.0  # Maximum sodium conductance (mS/cm^2)
gK = 36.0  # Maximum potassium conductance (mS/cm^2)
gL = 0.3  # Maximum leakage conductance (mS/cm^2)

# Simulation parameters
dt = 0.01  # Time step (ms)
t_end = 50.0  # Total simulation time (ms)
n_steps = int(t_end / dt)  # Number of simulation steps
# Initialize variables
Vm = np.zeros(n_steps)  # Membrane potential (mV)
m = np.zeros(n_steps)  # Sodium activation variable
h = np.zeros(n_steps)  # Sodium inactivation variable
n = np.zeros(n_steps)  # Potassium activation variable

# Set initial conditions
Vm[0] = -65.0  # Membrane potential at time 0 (mV)
m[0] = 0.05  # Initial m value
h[0] = 0.6  # Initial h value
n[0] = 0.32  # Initial n value
# Sodium channel activation variable (m) dynamics
def alpha_m(V):
    return 0.1 * (V + 40.0) / (1.0 - np.exp(-(V + 40.0) / 10.0))

def beta_m(V):
    return 4.0 * np.exp(-(V + 65.0) / 18.0)

def m_inf(V):
    return alpha_m(V) / (alpha_m(V) + beta_m(V))

def tau_m(V):
    return 1.0 / (alpha_m(V) + beta_m(V))

# Sodium channel inactivation variable (h) dynamics
def alpha_h(V):
    return 0.07 * np.exp(-(V + 65.0) / 20.0)

def beta_h(V):
    return 1.0 / (1.0 + np.exp(-(V + 35.0) / 10.0))

def h_inf(V):
    return alpha_h(V) / (alpha_h(V) + beta_h(V))

def tau_h(V):
    return 1.0 / (alpha_h(V) + beta_h(V))

# Potassium channel activation variable (n) dynamics
def alpha_n(V):
    return 0.01 * (V + 55.0) / (1.0 - np.exp(-(V + 55.0) / 10.0))

def beta_n(V):
    return 0.125 * np.exp(-(V + 65.0) / 80.0)

def n_inf(V):
    return alpha_n(V) / (alpha_n(V) + beta_n(V))

def tau_n(V):
    return 1.0 / (alpha_n(V) + beta_n(V))
# Simulate action potentials
for i in range(1, n_steps):
    V = Vm[i-1]
    m[i] = m_inf(V)
    h[i] = h_inf(V)
    n[i] = n_inf(V)

    # Apply ion channel blockers
    if i > int(n_steps / 2):
        gNa = 0.0  # Block sodium channels
        gK = 0.0  # Block potassium channels

    # Compute membrane currents
    INa = gNa * m[i] ** 3 * h[i] * (V - ENa)
    IK = gK * n[i] ** 4 * (V - EK)
    IL = gL * (V - EL)

    # Compute membrane potential change
    dVm = (-(INa + IK + IL) / Cm) * dt
    Vm[i] = Vm[i-1] + dVm
# Generate time vector
t = np.linspace(0, t_end, n_steps)

# Plot membrane potential
plt.plot(t, Vm)
plt.xlabel('Time (ms)')
plt.ylabel('Membrane Potential (mV)')
plt.title('Action Potential Generation with Ion Channel Blockers')
plt.grid(True)
plt.show()
# Generate time vector
t = np.linspace(0, t_end, n_steps)

# Plot sodium activation variable (m)
plt.plot(t, m, label='m')
plt.xlabel('Time (ms)')
plt.ylabel('Activation Variable')
plt.title('Sodium Activation Variable (m) over Time')
plt.legend()
plt.grid(True)
plt.show()

# Plot potassium activation variable (n)
plt.plot(t, n, label='n')
plt.xlabel('Time (ms)')
plt.ylabel('Activation Variable')
plt.title('Potassium Activation Variable (n) over Time')
plt.legend()
plt.grid(True)
plt.show()drive
