import matplotlib.pyplot as plt, matplotlib.animation as animation
import numpy as np, scipy.ndimage as ndi
import os, sys, utility

SHARP = [[0,0,0],
         [0,2,0],
         [0,0,0]]

BLUR = [[2,2,2],
        [2,2,2],
        [2,2,2]]


class osmosis:

    cell_world = [[]]
    dims = []

    def __init__(self, dimension, center_radius, contrasts):
        self.dims = dimension
        self.cell_world = self.initialize(center_radius, contrasts)
        self.edges = 100*ndi.gaussian_laplace(utility.draw_centered_circle(np.zeros(self.dims),
                                                                           center_radius,
                                                                           False), 1)

    def initialize(self, center_radius, contrasts):
        dr_noise = contrasts[0]
        val_circ = contrasts[1]
        state = val_circ*utility.draw_centered_circle(np.zeros(self.dims),center_radius,False)
        state += np.random.random_integers(0, dr_noise, self.dims[0]*self.dims[1]).reshape((self.dims))
        return state

    def show_states(self):
        f, ax = plt.subplots(1, 2)
        ax[0].imshow(self.cell_world, 'gray')
        ax[0].set_title('Cell World')
        ax[1].imshow(100*self.edges, 'gray')
        ax[1].set_title('Edges')
        plt.show()

    def internal_phase(self, n_steps):
        cycles = []
        for i in range(n_steps):
            ii = 0
            next_state = np.zeros(self.dims).flatten()
            edges = self.edges.flatten()
            for cell in self.cell_world.flatten():
                if edges[ii] >= 0:
                    continue
                # # /** Use Automata like rules to convect INSIDE circle **/ # #
                # else:

                ii += 1
            cycles.append(next_state.reshape(self.dims))
        return cycles


life = osmosis([250, 250], 100, [3, 5])
life.show_states()
test = life.internal_phase(1).pop()

plt.imshow(test, 'gray')
plt.show()