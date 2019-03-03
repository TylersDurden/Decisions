#!/usr/bin/env python
import sys, imutils, akasha
import numpy as np


class AutomataEngine:
    dimensions = []
    energy_levels = []
    energy_states = {}
    base_state_data = dict
    generations = 0

    def __init__(self, dims, states, state_data, time_scale):
        self.dimensions = dims
        self.energy_states = state_data
        self.energy_levels = states
        self.generations = time_scale
        self.base_state_data = self.measure_base_energy_levels(50)

    def measure_base_energy_levels(self, pad):
        base_levels = {}
        ii = 1
        for energy_eigenstate in self.energy_states.values():
            level_data = {}
            level_data['level'] = energy_eigenstate
            level_data['pad'] = pad
            level_data['n_pts'] = imutils.rectangle_accounting(energy_eigenstate, pad, 1, False)
            level_data['val'] = 1
            base_levels[ii] = level_data
            ii += 1
        return base_levels


def arg_parse(args, key):
    parser = 0
    ii = 0
    for element in args:
        if element == key:
          parser = ii + 1
        ii += 1
    return parser


def check_for_dims():
    dims = [250, 250]
    if '-d' in sys.argv:
        try:
            d = sys.argv[arg_parse(sys.argv, '-d')]
            dims = [int(d), int(d)]
        except IndexError:
            exit(0)
    return dims


def create_energy_levels(dimensions, default_energy_states, verbose):
    # Define the Energy Levels to use for simulation
    energy_eigenstates = {}
    energy_states = []
    filled_state = dimensions[0] * dimensions[1]
    for level in np.linspace(0, filled_state, default_energy_states):
        energy_states.append(int(level))
    energy_states.pop(0)
    ii = 0
    # Create a random seed state of ground state
    for energy_level in energy_states:
        ak = akasha.akashic(dimensions, default_energy_states, len(energy_states), energy_level,
                                                verbose)
        ak.draw_cloud(False)
        energy_eigenstates[ii] = np.array(ak.state)
        ii += 1
    return energy_states, energy_eigenstates


class StateMachine:

    state = [[]]
    lifespan = 0
    engine = AutomataEngine

    def __init__(self, state_space, timespan, mode):
        self.engine = state_space
        self.lifespan = timespan
        rules = {'Heater': self.heat_cycle}
        if mode in rules.keys():
            rules[mode]()

    def heat_cycle(self):
        ground = np.array(self.engine.energy_states[0])
        npts_in_center = self.engine.base_state_data['n_pts']

def main():
    # Dimensions of universe
    # N Energy Levels to use
    # Define a timescale to use for generative simulation
    # Begin Simulation
    #   - Create random seeds
    verbosity = False
    dimensions = check_for_dims()
    default_energy_states = 16
    default_time_scale = 100
    energy_states, energy_eigenstates = create_energy_levels(dimensions,default_energy_states, verbosity)

    # Create the probablilistic autoamta engine
    pae = AutomataEngine(dimensions,energy_states, energy_eigenstates,default_time_scale)
    asm = StateMachine(pae, default_time_scale, mode='Heater')


if __name__ == '__main__':
    main()
