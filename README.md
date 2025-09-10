# N-Body-Simulation
Simulation of the interaction between N bodies under gravity using the leapfrog integration algorithm in Python. The bodies are initialised with random positions and velocities which can either be all set to zero or randomised. Masses are initialised in such a way that they are equal across all bodies and sum to 20. NBody.py runs the simulation and plots the trajectories of each body in the system over the simulation time.  

To produce the simulation, frames are generated for each timestep and saved as images. The resulting sequence of images are combined into a single animated GIF using either a Linux terminal or an external GIF maker. GIFcode.py contains code for this and should be used immediately after the simulation is run, inplace of the plotting section. 

The GIF attached is for a simulation with N = 100, tEnd = 5 and random_velocities = True
