import numpy as np
import matplotlib.pyplot as plt

class Wave:
    def __init__(self,number_drones, head_position, angle, spacing, spacing_waves):
        self.head_position = head_position
        self.angle = angle
        self.spacing = spacing
        self.number_drones = number_drones
        self. spacing_waves = spacing_waves


class Ball:
    def __init__(self,number_drones, diameter, center, spacing):
            self.diameter = diameter
            self.center = center
            self. spacing = spacing
            self.number_drones = number_drones





def get_init_pos_wave (nbd, alpha, center, spacing) :
    nbr = (nbd - 1) // 2
    nbl = (nbd - 1) - nbr
    x_dist, y_dist = spacing * abs(np.sin(alpha / 2)), spacing * abs(np.cos(alpha / 2))
    left_side, right_side = np.zeros((nbl, 3)), np.zeros((nbr, 3))
    for l in range(0, nbl):
        left_side[l][0], left_side[l][1], left_side[l][2] = center[0] - (l + 1) * x_dist, center[1] - (l + 1) * y_dist, center[2]
    for r in range(0, nbr):
        right_side[r][0], right_side[r][1], right_side[r][2] = center[0] + (r + 1) * x_dist, center[1] - (r + 1) * y_dist, center[2]
    inter_pos = np.vstack((np.array(center), left_side))
    pos = np.vstack((inter_pos, right_side))
    return pos

def get_init_doublewave(nbd, alpha, center, spacing,spacing_waves) :
    new_head_pos = [0,0,0]
    new_head_pos [0], new_head_pos[1], new_head_pos[2] = center[0], center[1] - spacing_waves, center[2]
    first_wave = get_init_pos_wave(nbd//2, alpha, center, spacing)
    second_wave = get_init_pos_wave(nbd//2, alpha, new_head_pos, spacing)
    print(first_wave,second_wave)
    print(type(first_wave),len(first_wave))
    return np.vstack((first_wave,second_wave))



def get_ini_pos_ball(center, radius, spacing, num_surface_points, num_internal_points):
    surface_points = []
    phi = np.pi * (3. - np.sqrt(5.))
    for i in range(num_surface_points):           # creating the points at the surface of the ball
        y = 1 - (i / float(num_surface_points - 1)) * 2
        radius_at_height = np.sqrt(1 - y**2) * radius
        theta = phi * i
        x = np.cos(theta) * radius_at_height
        z = np.sin(theta) * radius_at_height
        point = center + np.array([x, y * radius, z])
        surface_points.append(point)

    internal_points = []
    num_internal_per_layer = int(radius / spacing)
    for i in range(num_internal_points):            # creating the points inside the ball
        layer = i % num_internal_per_layer
        height = layer * spacing + spacing / 2
        theta = np.random.uniform(0, 2*np.pi)
        phi = np.arccos(2*np.random.uniform(0, 1) - 1)
        x = center[0] + height * np.sin(phi) * np.cos(theta)
        y = center[1] + height * np.sin(phi) * np.sin(theta)
        z = center[2] + height * np.cos(phi)
        point = np.array([x, y, z])
        internal_points.append(point)

    return surface_points, internal_points



#
# def get_init_pos_front (number_drones, center, spacing) :
#     front_pos = np.zeros((number_drones,3))


###CREATING FEW BALL FORMATIONS###

small_ball = Ball(100,5,np.array([4,4,9]),1)
big_ball = Ball(1000,15,np.array([4,4,9]),2)

surface_points, intern_points = get_ini_pos_ball(big_ball.center,big_ball.diameter/2,big_ball.spacing,int(big_ball.number_drones*0.5),int(big_ball.number_drones*0.5))

swarm2 = [surface_points, intern_points]


x, y, z = [[point[0] for point in surface_points],[point[0] for point in intern_points]], [[point[1] for point in surface_points],[point[1] for point in intern_points]], [[point[2] for point in surface_points],[point[2] for point in intern_points]]


###CREATING FEW WAVE FORMATIONS###

little_wave = Wave (10,[3,3,5],40, 2,0.2)
big_narrow_wave = Wave (148,[4,4,12],30,0.05, 0.4)


swarm = get_init_doublewave(big_narrow_wave.number_drones,big_narrow_wave.angle,big_narrow_wave.head_position,big_narrow_wave.spacing,big_narrow_wave.spacing_waves)

# Plotting the initial swarm formation

Xs,Ys,Zs = swarm[:,0].tolist(), swarm[:,1].tolist(), swarm[:,2].tolist()

fig = plt.figure(figsize=(8, 8))
axes = plt.axes(projection="3d")

axes.scatter(Xs, Ys, Zs, color= 'red', label= 'Double Wave Formation', marker='^')
# axes.scatter(x, y, z, color= 'red', label= 'Ball Formation',marker='^')


axes.set_xlabel('x')
axes.set_ylabel('y')
axes.set_zlabel('altitude')
plt.title("Example of swarm's formation for 148 UAVs in a double wave formation")

#plt.title("Example of swarm's formation for 1000 UAVs in a ball formation")
plt.legend()
plt.show()
