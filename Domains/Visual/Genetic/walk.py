import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import utility
import time


def create_random_walk(n_steps):
    Directions = {1: 'up left',
                  2: 'up',
                  3: 'up right',
                  4: 'left',
                  5: 'self',
                  6: 'right',
                  7: 'down left',
                  8: 'down',
                  9: 'down right'}
    choice_pool = np.random.randint(1, 10, n_steps)
    random_walk = list()
    for step in choice_pool:
        random_walk.append(Directions[step])
    return random_walk


def draw_random_walk_basic(start, random_steps, world, erase, show):
    t0 = time.time()
    f = plt.figure()
    walk = list()
    path = list()
    state = world
    state[start[0], start[1]] = 1
    for step in random_steps:
        Directions = {'up left': [start[0]-1, start[1]-1],
                      'up': [start[0]-1 ,start[1]],
                      'up right': [start[0]-1, start[1]+1],
                      'left': [start[0], start[1]-1],
                      'self': start,
                      'right': [start[0], start[1]+1],
                      'down left': [start[0]+1, start[1]-1],
                      'down': [start[0]+1, start[1]],
                      'down right': [start[0]+1, start[1]+1]}
        if erase:
            state[start[0], start[1]] = 0
        path.append(start)
        try:
            start = Directions[step]
            state[start[0], start[1]] = 1
            walk.append([plt.imshow(state, 'gray')])
        except IndexError:
            continue
    dt = time.time()-t0
    print '\033[1mSimulation Finished \033[91m['+str(dt)+'s]\033[0m'
    if show:
        print '\033[1m\033[32mRendering '+str(len(walk))+' Frames\033[0m'
        a = animation.ArtistAnimation(f, walk, interval=20, blit=True, repeat_delay=900)
        plt.show()
        f.clear()
    return walk, path


'''
def evaluate_walk(path, goal):
    score = 0
    start = path[0]
    stop = path[len(path)-1]
    target_x = goal[0]
    target_y = goal[1]
    travel = []
    tracking = []
    good_steps = []
    i = 0
    for step in path:
        dx = step[0]-start[0]
        dy = step[1]-start[1]
        if i>0:
            travel.append([dx-goal[0], dy-goal[1]])
            r = [(step[0]-goal[0]),(step[1]-goal[1])]
            rad = np.sqrt(r[0]*r[0]+r[1]*r[1])
            tracking.append(rad)
        i += 1
    for s in np.diff(tracking):
        if s<=0:
            good_steps.append(True)
    print "Walk started at " + str(start) + " and ended at " + str(stop)
    correct_direction,steps = count_correct_steps(path, good_steps)
    score = 0.5*(float(len(good_steps)))/(len(path)) +\
            0.3*(np.array(tracking).mean()/np.array(tracking).max())
    score *= 100
    return score, correct_direction
'''


def count_correct_steps(path, good_steps):
    correct = []
    streak = 0
    ii = 0
    for step in good_steps:
        if step:
            streak += 1
            correct.append(path[ii])
        else:
            correct = []
            streak = 0
        ii += 1
    print "Longest correct sequence of steps: " + str(streak)
    return streak, correct


def main():
    show = False
    n_steps = 350
    dimensions = [100, 100]
    simple_map = utility.draw_centered_box(np.zeros(dimensions), 80, -1, False)
    start_pt = [15, 15]
    endpoint = [55,55]

    # Illustrate end point
    simple_map[endpoint[0]-3:endpoint[0]+3,endpoint[1]-3:endpoint[1]+3] = 1
    random_start = utility.spawn_random_point(np.zeros(dimensions))

    # Predetermine walk, and draw it
    random_walk = create_random_walk(n_steps)
    animated_walk, pathway = draw_random_walk_basic(start_pt, random_walk, simple_map, False, show)

    # Evaluate it on certain parameters
    score, best_path= evaluate_walk(pathway, endpoint)
    print "WALK SCORE: " + str(score)


if __name__ == '__main__':
    main()
