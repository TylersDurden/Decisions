import matplotlib.pyplot as plt
import numpy as np, time


class Markov:
    DEPTH = 0

    MODEL = {}   # Like a histogram for predicting future steps over time
    base_case_places = {}

    def __init__(self, n_steps, options):
        self.DEPTH = n_steps
        self.base_case_places = options
        self.initialize_probabilities()

    def initialize_probabilities(self):
        self.MODEL = self.find_step_distribution()
        n_possible_routes = pow(8, self.DEPTH)/1e8
        print '['+str(n_possible_routes) + " Billion Possible Routes for " + \
              str(self.DEPTH) + ' step path]'

    def find_step_distribution(self):
        distribution = {'up left':0,'up':0,'up right':0,
                        'left':0,'none':0,'right':0,
                        'down left':0,'down':0,'down right':0}
        N = int(1e6)
        total = N*self.DEPTH
        t0 = time.time()
        for i in range(N):
            walk, directions = generate_random_walk(self.DEPTH)
            for step in walk:
                distribution[step] += float(1)/total
        print str(total/1e6) + " Million Total Steps Counted [" + str(time.time() - t0) + 's]'
        return distribution


def generate_random_walk(n_steps):
    seed = np.random.randint(1, 10, n_steps)
    walk = []
    directions = {1: 'up left', 2: 'up', 3: 'up right',
                  4: 'left', 5: 'none', 6: 'right',
                  7: 'down left', 8: 'down', 9: 'down right'}
    for step in seed:
        walk.append(directions[step])
    return walk, directions


def main():
    walk, options = generate_random_walk(10)
    marky_mark = Markov(10, options)


if __name__ == '__main__':
    main()
