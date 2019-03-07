import matplotlib.pyplot as plt
import numpy as np
import utility
import time


def spawn_random_walk(position, n_steps):
    choice_pool = np.random.randint(1, 10, n_steps)
    random_walk = list()
    for step in choice_pool:
        directions = {1: [position[0]-1, position[1]-1],
                      2: [position[0]-1, position[1]],
                      3: [position[0]-1, position[1]+1],
                      4: [position[0], position[1]-1],
                      5: position,
                      6: [position[0], position[1]+1],
                      7: [position[0]+1, position[1]-1],
                      8: [position[0]+1, position[1]],
                      9: [position[0]+1, position[0]+1]}
        random_walk.append(directions[step])
        position = directions[step]
    return random_walk


def track_walk(start, goal, steps):
    displacement = []
    from_goal = []
    good_steps = []
    best_segments = {}
    streak = 0
    ii = 0
    for step in steps:
        r = [(step[0] - goal[0]), (step[1] - goal[1])]
        g = np.sqrt(r[0] * r[0] + r[1] * r[1])
        r = np.sqrt((step[0]-start[0])*(step[0]-start[0]) + (step[1]-start[1])*(step[1]-start[1]))
        from_goal.append(g)
        displacement.append(r)
    dG = np.diff(np.array(from_goal)[1:])
    dR = np.diff(np.array(displacement)[1:])
    for disp in dG:
        if disp <=0:
            streak += 1
            good_steps.append(steps[ii])
        elif dR[ii] >0:
            good_steps.append(steps[ii])
        else:
            best_segments[len(good_steps)] = good_steps
            good_steps = []
            streak = 0
        ii += 1
    return displacement, from_goal, good_steps, best_segments, dG, dR


def draw_walk(initial_state, start, target, walk):
    state = initial_state
    state[start[0],start[1]] = 1
    state[target[0]:target[0]+5, target[1]:target[1]+5] = -1
    for step in walk:
        state[step[0], step[1]] = 1
    return state


def main():
    T0 = time.time()
    # SINGLE WALK

    state = np.zeros((250, 250))
    # world = utility.draw_centered_box(state,100,2,False)
    start = [60, 50]
    target = [120, 74]

    random_walk = spawn_random_walk(start, 250)
    dR, dG, good_steps, best_steps, ddG, ddR = track_walk(start, goal=target, steps=random_walk)
    final_state = draw_walk(state, start, target, random_walk)

    # f, ax = plt.subplots(1, 2)
    # ax[0].imshow(final_state, 'gray')
    # ax[1].plot(dG)
    # ax[1].plot(dR)
    # ax[1].plot(np.array(dG)-np.array(dR))
    # plt.show()

    # TODO:
    '''
    ** Fitness Function 
    ** Evaluate, Parents
    ** Children, Mutation/Crossover 
    ** Simulation Loop
    '''

    DT = time.time()-T0
    print "FINISHED ["+str(DT)+'s Elapsed]'

if __name__ == '__main__':
    main()

