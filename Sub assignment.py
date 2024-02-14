import Formations
import Weapons

drone = Formations.wave_points


class Sub_assignment:
    def __init__(self, naw, dt):
        self.naw = naw      # number of available weapons
        self.dt = dt      # distance to target

    def closest_drones (self, all_positions) :
        five_closest_drones = []
        for dist in range (5) :
            dist_min , index  = min(all_positions.dist), self.all_positions(idx)
            five_closest_drones.append(dist_min)
            del drone[index].pos




