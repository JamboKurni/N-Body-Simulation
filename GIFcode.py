import numpy as np
import matplotlib.pyplot as plt

''' Code to produce GIF of simulation'''

Snap = 10 # Snapshot taken every 10th step
fig, ax = plt.subplots()
for frame in range(Nt):

    # Clear the axes to prepare for the next frame
    if frame %Snap == 0: # every Snapth step, take a snapshot (Snap is an integer)
        ax.clear()
    # Plot the updated positions of the particles
        pos = positions_history[frame]
        ax.scatter(pos[:, 0], pos[:, 1], s=10, color='blue')
        ax.set_aspect('equal', 'box')
        ax.set(xlim=(-5, 5), ylim=(-5, 5))
        ax.set_title(f'Frame {frame}') # Display the frame number
        # Save the current frame as a .png file with a unique name
        plt.savefig(f'N_Body_Simulation_1B_{frame:03d}.png', dpi=240) # As an example