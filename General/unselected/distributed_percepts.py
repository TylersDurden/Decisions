import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import networkx as nx
import numpy as np
import utility
import sys


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

    def minimize_connectivity(self):
        # Go through all connections
        # And Eliminate all but 1, leaving
        # The one that connects furthest pt
        if self.n_connections == 1:
            return True
        else:
            x = self.position[1]
            y = self.position[0]
            radii = {}
            maxima = 0
            for p in self.connections.keys():
                pt = self.connections[p]
                r = np.sqrt((x-pt[1])*(x-pt[1]) + (y-pt[0])*(y-pt[0]))
                if r > maxima:
                    maxima = r
                radii[str(maxima)] = pt
            print "Keeping connection \033[1m"+self.__repr__()+"->("+\
                  str(radii[str(maxima)][1])+','+str(radii[str(maxima)][1])+')\t '+\
                  str(maxima)+'\033[0m'
            return radii[str(maxima)]

    def __repr__(self):
        me = ''
        me += str(self.position[1])+","+str(self.position[0])
        return me


class Swarm:

    swarm = [[]]
    cloud_data = {}
    conx_distrib = {}
    FireFlies = list()

    def __init__(self, w_size, c_radius, n_perc):
        self.swarm, self.cloud_data = Swarm.initialize(w_size, c_radius, n_perc)
        # determine the distribution of connectivity in the cluster
        self.conx_distrib, self.FireFlies = self.check_interconnect_distribution()
        # Show the swarm, and plot of connectivity
        self.show()

    def show(self):
        # Use K to see the 'reach' of each firefly
        k = np.ones((4,4))
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
        flies = []
        # Count the distribution of connections in firefly swarm
        neighbors = {}
        x_domain = np.arange(0, 10, 1)
        for x in x_domain:
            neighbors[x] = 0
        # Create a swarm of FireFlies, counting each's connections
        for point in self.cloud_data.keys():
            try:
                ff = FireFly(self.swarm, self.cloud_data, point, 4)
                flies.append(ff)
                neighbors[ff.n_connections] += 1
            except IndexError:
                pass
        return neighbors, flies

    @staticmethod
    def initialize(w_size, c_radius, n_percepts):
        # Create a Point Cloud based on Parameters defined above
        swarm, cloud_data = utility.create_point_cloud(w_size, c_radius, n_percepts, False)
        print str(len(cloud_data.keys())) + " Points in Cloud"
        return swarm, cloud_data

    def minimize_connectivity(self, is_animated):
        evolution = []
        '''
        We want to minimize the connectivity to 1 
        connection within threshold (reach) such
        that network remains wholly connected 
        (no particle has 0 connections, ideally).
        '''
        correctly_configured = self.conx_distrib[1]
        print str(correctly_configured) + " Particles Currently have 1 Connection "
        target = 1
        correct = {'done': [], 'open': []}
        for particle in self.FireFlies:
            if particle.n_connections == target:
                correct['done'].append(particle)
            else:
                correct['open'].append(particle)
                particle.minimize_connectivity()


def main():
    # Input Parameters
    world_size = 258
    cloud_radius = 104
    n_percepts = 500

    ''' Initialize a SWARM '''
    s = Swarm(world_size, cloud_radius, n_percepts)

    if '-minimize' in sys.argv:
        # Minimize swarm connectivity to lowest non-zero number
        print "\033[1m\033[34m\t\t** Minimizing Swarm Connectivity **\033[0m"
        s.minimize_connectivity(is_animated=True)
        s.check_interconnect_distribution()
        s.show()

    if '-optimize' in sys.argv:
        # Maximize swarm connectivity to lowest non-zero number
        print "\033[1m\033[35m\t\t** Optimizing Swarm Connectivity **\033[0m"
        s.optimize_swarm(is_animated=True)
        print s.FireFlies.pop().connections

if __name__ == '__main__':
    main()

