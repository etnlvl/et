import numpy as np
import matplotlib.pyplot as plt

class Wave:
    def __init__(self,number_drones, head_position, angle, spacing ):
        self.head_position = head_position
        self.angle = angle
        self.spacing = spacing
        self.number_drones = number_drones
        self.drone_list = []

    def get_init_pos_wave(self, head_position=None):
        if head_position is None:
            pass
        else:
            self.head_position = head_position
        nbr = (self.number_drones - 1) // 2
        nbl = (self.number_drones - 1) - nbr
        x_dist, y_dist = self.spacing * abs(np.sin(self.angle / 2)), self.spacing * abs(np.cos(self.angle / 2))
        left_side, right_side = np.zeros((nbl, 3)), np.zeros((nbr, 3))
        for l in range(0, nbl):
            left_side[l][0], left_side[l][1], left_side[l][2] = self.head_position[0] - (l + 1) * x_dist, self.head_position[1] - (
                        l + 1) * y_dist, self.head_position[2]
            point1 = left_side[l]
            drl = Drone(point1, l)
            self.drone_list.append(drl)
        for r in range(0, nbr):
            right_side[r][0], right_side[r][1], right_side[r][2] = self.head_position[0] + (r + 1) * x_dist, self.head_position[1] - (
                        r + 1) * y_dist, self.head_position[2]
            point2 = right_side[r]
            drr = Drone(point2, r)
            self.drone_list.append(drr)
        inter_pos = np.vstack((np.array(self.head_position), left_side))
        pos = np.vstack((inter_pos, right_side))
        print("The initial positions of each UAV in the swarm are ", pos)

        return pos

    def get_init_double_wave(self):
        first_wave = self.get_init_pos_wave()
        new_head_pos = [0, 0, 0]
        spacing_waves = self.spacing/3
        new_head_pos[0], new_head_pos[1], new_head_pos[2] = self.head_position[0], self.head_position[1] - spacing_waves, self.head_position[2]
        second_wave = self.get_init_pos_wave(head_position=new_head_pos)
        print(first_wave, second_wave)
        print(type(first_wave), len(first_wave))
        return np.vstack((first_wave, second_wave))

class Ball:
    def __init__(self,number_drones, diameter, center, spacing):
            self.diameter = diameter
            self.center = center
            self. spacing = spacing
            self.number_drones = number_drones
            self.drone_list = []

    def get_ini_pos_ball(self):
        surface_points = []
        phi = np.pi * (3. - np.sqrt(5.))
        for i in range(int(self.number_drones*0.5)):           # creating the points at the surface of the ball
            y = 1 - (i / float(self.number_drones*0.5 - 1)) * 2
            radius_at_height = np.sqrt(1 - y**2) * self.diameter/2
            theta = phi * i
            x = np.cos(theta) * radius_at_height
            z = np.sin(theta) * radius_at_height
            point = self.center + np.array([x, y * self.diameter/2, z])
            dr = Drone(point, i)
            self.drone_list.append(dr)
            surface_points.append(point)


        internal_points = []
        num_internal_per_layer = int(self.diameter/2 / self.spacing)
        for i in range(int(self.number_drones*0.5)):            # creating the points inside the ball
            layer = i % num_internal_per_layer
            height = layer * self.spacing + self.spacing / 2
            theta = np.random.uniform(0, 2*np.pi)
            phi = np.arccos(2*np.random.uniform(0, 1) - 1)
            x = self.center[0] + height * np.sin(phi) * np.cos(theta)
            y = self.center[1] + height * np.sin(phi) * np.sin(theta)
            z = self.center[2] + height * np.cos(phi)
            point = np.array([x, y, z])
            internal_points.append(point)

        return surface_points, internal_points

class Front:
    def __init__(self, number_drones, center, spacing, front_dir) :
        self.number_drones= number_drones
        self.center = center
        self.spacing = spacing
        self.front_dir = front_dir
        self.drone_list = []


    def get_init_pos_front(self):
        nbl= self.number_drones//2
        nbr = self.number_drones - 1 -nbl
        pos = []
        if self.front_dir[0] == 1 : # front goes to x direction
            for r in range (0, nbr) :
                e = np.array([self.center[0], self.center[1] + self.spacing, self.center[2]])
                pos.append(e)
                drone = Drone (e, r)
                self.drone_list.append(drone)
            for l in range (0,nbl) :
                k = np.array([self.center[0], self.center[1] - self.spacing , self.center[2] ])
                pos.append(k)
                drone = Drone(k, l)
                self.drone_list.append(drone)


        else :                     # front goes to y direction
            for r in range (0, nbr) :
                e = np.array([self.center[0] + self.spacing, self.center[1], self.center[2]])
                pos.append(e)
                drone = Drone(e, r)
                self.drone_list.append(Drone)
            for l in range (0,nbl) :
                k = np.array([self.center[0] - self.spacing, self.center[1], self.center[2] ])
                pos.append(k)
                drone= Drone (k,l)
                self.drone_list.append(Drone)



class Drone:
    def __init__(self, pos, idx):
        self.active = 1
        self.pos = pos
        self.distance = np.sqrt(self.pos[0]**2+ self.pos[1]**2 +self.pos[2]**2)
        self.index = idx
        self.threat_val = 1
        self.path = []



small_ball= Ball(100,5, np.array([4,4,9]),1)
big_ball = Ball(1000, 100, np.array([4,4,9]), 20)


surface_points, intern_points = small_ball.get_ini_pos_ball()

double_wave = Wave(189, np.array([2,2,10]),30, 2)
wave_points = double_wave.get_init_pos_wave()

front_config = Front(50 , np.array([5,5,4]),1, [1,0,0])

front_wave = front_config.get_init_pos_front()

#
# Xs,Ys,Zs = wave_points[:,0].tolist(), wave_points[:,1].tolist(), wave_points[:,2].tolist()
#
# fig = plt.figure(figsize=(6, 6))
# axes = plt.axes(projection="3d")
# axes.scatter(Xs, Ys, Zs, color= 'red', label= 'Double Wave Formation', marker='^')
# axes.set_xlabel('x')
# axes.set_ylabel('y')
# axes.set_zlabel('altitude')
# plt.title(f"Example of swarm's formation for {double_wave.number_drones} UAVs as a wave")
# plt.show()