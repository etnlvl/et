import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def generate_points(center, radius, spacing, num_surface_points, num_internal_points):
    surface_points = []
    phi = np.pi * (3. - np.sqrt(5.))  # Golden angle in radians

    for i in range(num_surface_points):
        y = 1 - (i / float(num_surface_points - 1)) * 2  # y goes from 1 to -1
        radius_at_height = np.sqrt(1 - y**2) * radius
        theta = phi * i  # Angle around the y-axis
        x = np.cos(theta) * radius_at_height
        z = np.sin(theta) * radius_at_height
        point = center + np.array([x, y * radius, z])
        surface_points.append(point)

    internal_points = []
    num_internal_per_layer = int(radius / spacing)  # Number of internal points per layer
    for i in range(num_internal_points):
        layer = i % num_internal_per_layer
        height = layer * spacing + spacing / 2  # Adding spacing/2 to ensure points are within the sphere
        theta = np.random.uniform(0, 2*np.pi)
        phi = np.arccos(2*np.random.uniform(0, 1) - 1)
        x = center[0] + height * np.sin(phi) * np.cos(theta)
        y = center[1] + height * np.sin(phi) * np.sin(theta)
        z = center[2] + height * np.cos(phi)
        point = np.array([x, y, z])
        internal_points.append(point)

    return surface_points, internal_points

# Exemple d'utilisation
center = np.array([0, 0, 0])  # Centre de la boule
diameter = 10  # Diamètre de la boule
spacing = 1  # Espacement entre les points
radius = diameter / 2
num_surface_points = 1000  # Nombre de points sur la surface
num_internal_points = 500  # Nombre de points à l'intérieur

surface_points, internal_points = generate_points(center, radius, spacing, num_surface_points, num_internal_points)

# Tracer les points dans l'espace
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Extraire les coordonnées x, y et z des points
xs_surface = [point[0] for point in surface_points]
ys_surface = [point[1] for point in surface_points]
zs_surface = [point[2] for point in surface_points]

xs_internal = [point[0] for point in internal_points]
ys_internal = [point[1] for point in internal_points]
zs_internal = [point[2] for point in internal_points]

# Tracer les points
ax.scatter(xs_surface, ys_surface, zs_surface, color='blue', label='Surface points')
ax.scatter(xs_internal, ys_internal, zs_internal, color='red', label='Internal points')

# Définir les étiquettes des axes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Afficher la légende
plt.legend()

plt.show()
