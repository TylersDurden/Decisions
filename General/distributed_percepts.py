import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import networkx as nx
import numpy as np
import utility


class FireFly:
    position = []
    world = []
    connections = {}
    n_connections = 0

    def __init__(self, swarm_matrix, point_cloud, my_index, reach):
        self.position = point_cloud[point_cloud.keys().pop(my_index)]
        self.world = swarm_matrix
        self.find_neighbors(point_cloud, reach)

    def find_neighbors(self, cloud, threshold):
        x_pos = self.position[1]
        y_pos = self.position[0]
        cnxs = 0
        for p in cloud.keys():
            pt = cloud[p]
            xp = pt[1]
            yp = pt[0]
            if str(self.position) != str(pt):
                dx = ((xp-x_pos)*(xp-x_pos))
                dy = ((yp-y_pos)*(yp-y_pos))
                r = np.sqrt((dx+dy))
                if r <= threshold:
                    self.connections[cnxs] = pt
                    cnxs += 1
        self.n_connections = cnxs


class Swarm:

    swarm = [[]]
    cloud_data = {}
    conx_distrib = {}

    def __init__(self, w_size, c_radius, n_perc):
        self.swarm, self.cloud_data = self.initialize(w_size, c_radius, n_perc)
        # determine the distribution of connectivity in the cluster
        self.conx_distrib = self.check_interconnect_distribution()
        # Show the swarm, and plot of connectivity
        self.show()

    def show(self):
        # Show swarm connectivity distribution
        f, ax = plt.subplots(1, 2)
        ax[0].bar(self.conx_distrib.keys(), self.conx_distrib.values())
        ax[0].set_title('Swarm Image')
        ax[1].imshow(self.swarm, 'gray')
        ax[0].set_title('N Connections Per FireFly [' + str(len(self.cloud_data.keys())) + ' total points in cloud]')
        ax[0].set_ylabel('N Particles')
        ax[0].set_xlabel('N Connections')
        plt.show()

    def check_interconnect_distribution(self):
        # Count the distribution of connections in firefly swarm
        neighbors = {}
        x_domain = np.arange(0, 10, 1)
        for x in x_domain:
            neighbors[x] = 0
        # Create a swarm of FireFlies, counting each's connections
        for point in self.cloud_data.keys():
            try:
                ff = FireFly(self.swarm, self.cloud_data, point, 4)
                neighbors[ff.n_connections] += 1
            except IndexError:
                pass
        return neighbors


    def initialize(self, w_size, c_radius, n_percepts):
        # Create a Point Cloud based on Parameters defined above
        swarm, cloud_data = utility.create_point_cloud(w_size, c_radius, n_percepts, False)
        print str(len(cloud_data.keys())) + " Points in Cloud"
        return swarm, cloud_data


def main():
    # Input Parameters
    world_size = 258
    cloud_radius = 124
    n_percepts = 450

    Swarm(world_size, cloud_radius, n_percepts)


if __name__ == '__main__':
    main()

