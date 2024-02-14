import numpy as np
import matplotlib.pyplot as plt

def next_pos(init_pos, velocity, time_step,nb_d):
    new_pos = []
    for i in range(0,nb_d):
        new_pos.append(init_pos[i] + velocity[i] * time_step)
    return np.reshape(new_pos,(nb_d,3))
# For building the initial position of the swarm accord
#def build_init_swarm_pos(nb_d, geometry_desired, ) :


init_pos1 = np.array([[16,6,8],[16.5,6.5,8],[15.5,5.5,8]])


test_position = next_pos(init_pos1, np.array([0.1,-0.1,-0.2]), 1,2) # Testing if working


def build_all_positions (first_pos, Nb_it, velocity , time_step,nb_d) :
    all_positions = []
    all_positions.append(first_pos)
    for i in range (1,Nb_it) :
        all_positions.append(next_pos(all_positions[i-1],velocity, time_step,nb_d))
    return all_positions

# Test of build_all_positions
swarm_positions = build_all_positions (init_pos1, 10,  np.array([2,2,-1]), 0.5 , 3)

# print(swarm_positions)

Xs,Ys,Zs = [],[],[]

for array in swarm_positions:
    col1, col2, col3 = array[:,0].tolist() , array[:,1].tolist(), array[:,2].tolist()
    Xs.extend(col1)
    Ys.extend(col2)
    Zs.extend(col3)

print(Xs, Ys, Zs)
fig = plt.figure()
ax = plt.axes(projection='3d')

ax.plot3D(Xs, Ys, Zs)

ax.set_title('Swarm trajectory')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Altitude')

plt.show()
