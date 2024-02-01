# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Drone:
    def __init__(self, position, velocity, threat_value):
        self.position = position
        self.velocity = velocity
        self.threat_value = threat_value

class Weapon:
    def __init__(self, ammunition, availability, optimal_range, destruction_time):
        self.ammunition = ammunition
        self.availability = availability
        self.optimal_range = optimal_range
        self.destruction_time = destruction_time

def update_position_approach(drone, approach_speed, gbad_position):
    # Update drone position with linear approach towards GBAD with a 45-degree slope
    direction_to_gbad = gbad_position - drone.position
    normalized_direction = direction_to_gbad / np.linalg.norm(direction_to_gbad)

    # Update position to maintain a 45-degree slope
    drone.position += approach_speed * normalized_direction
    drone.position[2] = gbad_position[2] + np.tan(np.pi / 4) * np.linalg.norm(drone.position[:2] - gbad_position[:2])

    drone.velocity = normalized_direction

def calculate_hit_probability(distance, sshp_matrix):
    # Find the SSHP value based on the distance
    for range_limit, sshp_value in sshp_matrix.items():
        if distance <= range_limit:
            return sshp_value
    # If the distance is greater than the maximum range, return the lowest SSHP value
    return list(sshp_matrix.values())[-1]

def plot_simulation(threat_matrix, gbad_position, background=True):
    fig = plt.figure(figsize=(10, 8))  # Set the figure size to (10, 8) inches
    ax = fig.add_subplot(111, projection='3d')

    # Plot GBAD position
    ax.scatter(gbad_position[0], gbad_position[1], gbad_position[2], label='GBAD', c='blue', s=200)

    if background:
        # Add a more realistic mountain shape
        mountain_x = np.linspace(-20, -10, 100)
        mountain_y = np.linspace(-15, -5, 100)
        mountain_X, mountain_Y = np.meshgrid(mountain_x, mountain_y)
        mountain_Z = np.exp(-0.05 * (mountain_X + 15)**2 - 0.05 * (mountain_Y + 10)**2) * 10
        ax.plot_surface(mountain_X, mountain_Y, mountain_Z, cmap='terrain', alpha=0.7)

    for drone in threat_matrix:
        ax.scatter(drone.position[0], drone.position[1], drone.position[2], label=f'Drone {drone.threat_value}')

    # Set fixed axes limits for consistent scale
    ax.set_xlim([-20, 20])
    ax.set_ylim([-20, 20])
    ax.set_zlim([0, 60])

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.legend()
    plt.show()

def simulate_attack(threat_matrix, weapons_matrix, sshp_matrix, gbad_position):
    approach_speed = 1.0  # Adjust as needed

    for time_step in range(20):  # Simulate 20 time steps
        print(f"Time Step: {time_step}")
        for i, drone in enumerate(threat_matrix):
            # Update drone position with a staggered approach
            update_position_approach(drone, approach_speed, gbad_position + np.array([0, 0, 10 + i * 5]))

            print(f"Drone {drone.threat_value} at Position {drone.position}")

            # Decide which weapon to use based on threat, availability, range, and hit probability
            for weapon in weapons_matrix:
                if (
                    weapon.availability > 0
                    and np.linalg.norm(drone.position - gbad_position) <= weapon.optimal_range
                ):
                    distance_to_drone = np.linalg.norm(drone.position - gbad_position)
                    hit_probability = calculate_hit_probability(
                        distance_to_drone, sshp_matrix
                    )

                    # Randomly determine if the weapon hits based on hit probability
                    if np.random.rand() < hit_probability:
                        print(
                            f"Hit! Using Weapon: Ammo={weapon.ammunition}, Range={weapon.optimal_range}, Destruction Time={weapon.destruction_time}, Hit Probability={hit_probability}"
                        )
                        weapon.availability -= 1
                    else:
                        print(
                            f"Miss! Using Weapon: Ammo={weapon.ammunition}, Range={weapon.optimal_range}, Destruction Time={weapon.destruction_time}, Hit Probability={hit_probability}"
                        )
                    break

        # Plot the current positions of drones and GBAD after each time step
        plot_simulation(threat_matrix, gbad_position)

# Create 8 drones with a staggered approach in a circular formation
drones = []
for i in range(8):
    angle = i * (2 * np.pi / 8)  # Evenly spaced angles
    position = np.array([15 * np.cos(angle), 15 * np.sin(angle), 50])
    velocity = np.array([-np.sin(angle), np.cos(angle), 0])  # Perpendicular to the position vector
    drones.append(Drone(position, velocity, i + 1))

# Create 4 different types of weapons
weapons = [
    Weapon(20, 1, 15, 3),  # Type 1
    Weapon(15, 1, 10, 2),  # Type 2
    Weapon(10, 1, 20, 4),  # Type 3
    Weapon(25, 1, 25, 5)   # Type 4
]

sshp_matrix = {10: 0.8, 15: 0.6, 20: 0.4, 25: 0.2}  # Example SSHP matrix

# GBAD system position in a plain
gbad_position = np.array([0, 0, 0])

# Simulate the attack with SSHP considerations
simulate_attack(drones, weapons, sshp_matrix, gbad_position)
