import numpy as np


class Perceptron:
    directions = {}
    world = [[]]
    pos = []
    percept = {}
    action = {}

    def __init__(self, state, position, stimulus):
        self.world = state
        self.pos = position
        self.percept = stimulus
        self.initialize_directions()

    def initialize_directions(self):
        self.directions = {1: [self.pos[0] - 1, self.pos[1] - 1],
                           2: [self.pos[0], self.pos[1] - 1],
                           3: [self.pos[0] + 1, self.pos[1] - 1],
                           4: [self.pos[0] - 1, self.pos[1]],
                           5: [self.pos],
                           6: [self.pos[0] + 1, self.pos[1]],
                           7: [self.pos[0] - 1, self.pos[1] + 1],
                           8: [self.pos[0], self.pos[1] + 1],
                           9: [self.pos[0] + 1, self.pos[1] + 1]}


class StepsEngine:

    Fuel = 0
    burst_limit = 0
    starting_pt = []
    decision_tree = {}
    steps = []

    def __init__(self, N, depth, start):
        self.Fuel = N
        self.burst_limit = depth
        self.starting_pt = start
        self.decision_tree, self.steps = self.Ignition()

    def Ignition(self):
        random_walk = []
        raw_steps = np.random.randint(0, 9, self.Fuel)
        step_tree = {}
        i = 0
        for step in raw_steps:
            possible_steps = []
            cycle = np.random.randint(0, 9, self.burst_limit).flatten()
            for spark in cycle:
                possible_steps.append(spark)
            random_walk.append(step)
            step_tree[i] = possible_steps
            i += 1
        return step_tree, random_walk
