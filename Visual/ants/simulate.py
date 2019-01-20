import numpy as np, matplotlib.pyplot as plt, matplotlib.animation as animatio
import ant, time


def spawn_random_point(state):
    # Initialize a random position
    x = np.random.randint(0, state.shape[0], 1, dtype=int)
    y = np.random.randint(0, state.shape[1], 1, dtype=int)
    return [x, y]


class MotionPerceptPipeLine:
    start = []
    choices = []
    world = [[]]

    def __init__(self, N, state):
        t0 = time.time()
        start_point = spawn_random_point(state)
        crawl_space = ant.StepsEngine(N=N, depth=9, start=start_point)
        print "Completed computing " + str(N) + " random steps [" + str(time.time() - t0) + 's]'
        thoughts = crawl_space.decision_tree
        actions = crawl_space.steps


def main():
    steps = 100  # 100 Steps
    width = 500
    height = 500
    MotionPerceptPipeLine(steps,np.zeros((100, 100)))


if __name__ == '__main__':
    main()
