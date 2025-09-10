import numpy as np
import matplotlib.pyplot as plt

def initialize_bodies(N, random_velocities=False): # Function to initialise the positions and velocities of N bodies, given false random velocities
    
    positions = np.random.uniform(-5, 5, (N, 3))# Random positions assuming the moving space is 5 x 5 box
    
    
    masses = np.full(N, 20.0 / N) # Ensuring all the masses are equal and sum to 20
    
    if random_velocities:
        
        velocities = np.random.uniform(-1, 1, (N, 3)) # Some random initial velocities 
        
        velocities -= np.mean(velocities, axis=0) # Adjusting the velocities to set center-of-mass velocity to zero ensuring the system is in the centre of mass. 

    else:
        
        velocities = np.zeros((N, 3)) # Set all the velocities to zero in the velocity matrix 
    
    return positions, velocities, masses


def calculate_accelerations(positions, masses, softening_length): # Function to compute accelerations for each body
    N = len(positions)
    accelerations = np.zeros_like(positions) # Creating acceleration array with same shape and data type as the position array
    
    for i in range(N):
        for j in range(i+1, N):
            
            r_ij = positions[j] - positions[i] # The r vector from body i to body j
           
            dist = np.sqrt(np.sum(r_ij**2) + softening_length**2) # The distance between body i and body j
            # Softening length is there to prevent any singularities in the acceleration equation below
            
            force = masses[i] * masses[j] / dist**2 # Force magnitude assuming G = 1
           
            acceleration = force * r_ij / dist # Acceleration calculation
            
            accelerations[i] += acceleration / masses[i] # Acceleration for body i 
            accelerations[j] -= acceleration / masses[j] # Acceleration for body j 
    
    return accelerations


def leapfrog_integration(positions, velocities, masses, dt, softening_length, Nt): # Function to implement the leapfrog algorithm
    
    positions_history = np.zeros((Nt, len(positions), 3)) # Array to store the positions at each time step for plotting later
    
    for t in range(Nt):
        
        positions_history[t] = positions # Storing the current positions
        
        accelerations = calculate_accelerations(positions, masses, softening_length)
        velocities += 0.5 * dt * accelerations # (1/2) Kick: Update velocities by half a timestep
        
        positions += dt * velocities # Drift: Update positions using current velocities
       
        accelerations = calculate_accelerations(positions, masses, softening_length)
        velocities += 0.5 * dt * accelerations  # (1/2) Kick: Update velocities by another half timestep
    
    return positions_history

''' Simulation Stage where N, the number of bodies, timestep and simulation can be altered. In this case N = 100, dt = 0.01 and tEnd = 5. Additionally random_velocities can be set to True or False'''

N = 100  # 100 bodies
dt = 0.01  # Time step
tEnd = 5.0  # Total simulation time
Nt = int(np.ceil(tEnd / dt))  # Number of timesteps
softening_length = 0.1  # Softening length for gravitational force calculation

positions, velocities, masses = initialize_bodies(N, random_velocities=False) # Initialising the bodies with zero velocities

positions_history = leapfrog_integration(positions, velocities, masses, dt, softening_length, Nt) # Running the simulation

''' Plotting the trajectories of the bodies'''

plt.figure(figsize=(8, 8)) # Square plotting space
for i in range(N):
    plt.plot(positions_history[:, i, 0], positions_history[:, i, 1], label=f'Body {i+1}')# Plot the 2D trajectories of the bodies

plt.title('N-Body Simulation')
plt.xlabel('x / m')
plt.ylabel('y / m')
plt.xlim(-5, 5)  
plt.ylim(-5, 5) # Limits which can be adjusted based on expected positions
plt.grid(True)
plt.show()
