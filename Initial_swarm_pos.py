import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import proj3d


def wave_formation (nbd, alpha, center, spacing ) : ####you can adjust the number of drones, the angle of the formation, the position of the first drone and the space between the drones
    nbr = (nbd-1)//2
    nbl = (nbd-1) - nbr
    x_dist, y_dist = spacing*abs(np.sin(alpha/2)) , spacing*abs(np.cos(alpha/2))
    left_side, right_side = np.zeros((nbl,3)) , np.zeros((nbr,3))
    for l in range (0,nbl) :
        left_side[l][0], left_side[l][1] , left_side[l][2]= center[0] - (l+1)*x_dist , center[1] -(l+1)*y_dist , center[2]
    for r in range (0,nbr) :
        right_side[r][0], right_side[r][1] , right_side[r][2]= center[0] + (r+1)*x_dist , center[1] - (r+1)*y_dist , center[2]
    inter_pos = np.vstack((np.array(center),left_side))
    pos = np.vstack((inter_pos,right_side))
    return pos


all_drones = wave_formation(101,30,[7,7,2],0.01)  # Give the all positions of each drone in the swarm

# Plotting the initial swarm formation

Xs,Ys,Zs = all_drones[:,0].tolist(), all_drones[:,1].tolist(), all_drones[:,2].tolist()

plt.figure(figsize=(7, 7))
axes = plt.axes(projection="3d")

axes.scatter(Xs, Ys, Zs)
plt.show()
