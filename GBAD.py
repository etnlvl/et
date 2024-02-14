import numpy as np
import heapq as hp

class GBAD:
    def __init__(self, position, drone_list, weapons_list):
        self.position = position
        self.drone_list = drone_list
        self.closest_drones = []
        self.weapons = weapons_list
        self.nw = len(weapons_list)

    def get_closest_drones(self, n):
        a = [np.linalg.norm(self.position- d.pos) for d in self.drone_list]
        n_dist =hp.nsmallest(n, a)
        indexes = [a.index(t) for t in n_dist]
        self.closest_drones = [self.drone_list[idx] for idx in indexes]
        return n_dist

    def create_weapons(self):
        pass


import Formations
import Weapons
# Drone formation
little_wave= Formations.Wave(100,5, np.array([4,4,9]),1)
little_wave.get_init_pos_wave(np.array([4,4,9]))
# N closest drones
n = 5
# Weapons
Gun1 = Weapons.Gun()
Gun2 = Weapons.Gun()
grenade = Weapons.Grenade()
Laser1 = Weapons.Laser()
Laser2 = Weapons.Laser()

# Test instead of small_ball.drone_list for further dist
# test_drones = [Drone(np.array([0,0,1]),0), Drone(np.array([1e4,1e4,1e4]),0), Drone(np.array([1e3,1e3,1e3]),0)]
gbase = GBAD(np.array([0,0,0]),little_wave.drone_list, [Gun1, Gun2, Laser1, Laser2]) # Init GBAD

# def __init__(self, pos, idx)

# Get probabilities of weapons
w_prob = [w.Pc for w in gbase.weapons]
# Create cost/probability matrix
cost = np.reshape(np.repeat(w_prob,n),(gbase.nw,n))
gbase.get_closest_drones(n)
in_range = []
for index, w in enumerate(gbase.weapons):
    dist = gbase.get_closest_drones(n)  # Get closest drones
    cost[index] = cost[index]*[d < w.rc for d in dist]
    cost[index]= cost[index] * np.repeat([w.ammunition > 0],n)
import MIP_Assinment

test = MIP_Assinment(cost)
test.optimize()







