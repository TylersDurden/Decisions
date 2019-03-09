from matplotlib.animation import FFMpegWriter
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import utility
import sys

def predatory_chase(path, opts):
    start = opts['start']
    tracker = []
    chase = []
    follow = []
    captured = False
    for step in path:
        dx = step[0]-start[0]
        dy = step[1]-start[1]
        r = np.sqrt(dx**2 + dy**2)
        tracker.append(r)
        if np.abs(dx) > np.abs(dy):
            if dx < 0:
                start = [start[0]-1, start[1]]
            if dx > 0:
                start = [start[0]+1, start[1]]
        if abs(dx) < abs(dy):
            if dy > 0:
                start = [start[0], start[1]+1]
            if dy < 0:
                start = [start[0], start[1]-1]
        chase.append(start)
        follow.append(step)
        if r == 0:
            captured = True
            break

    return chase, follow, captured


def draw_chase(prey_path, pred_path, shape, save, ani):
    f = plt.figure()
    state = np.zeros(shape)
    chase = []
    if len(pred_path) != len(prey_path):
        print "Chase sequence sizes don't match!!"
        print "Prey: " + str(len(prey_path))
        print "Pred: " + str(len(pred_path))
        exit(0)
    else:
        for step in range(len(prey_path)):
            prey = prey_path[step]
            pred = pred_path[step]
            state[prey[0]-2:prey[0]+2, prey[1]-2:prey[1]+2] = -1
            state[pred[0]-2:pred[0]+2, pred[1]-2:pred[1]+2] = 1
            chase.append([plt.imshow(state, 'gray')])
            state[prey[0]-2:prey[0]+2, prey[1]-2:prey[1]+2] = 0
            state[pred[0]-2:pred[0]+2, pred[1]-2:pred[1]+2] = 0
    a = animation.ArtistAnimation(f,chase,interval=50,blit=True,repeat_delay=900)
    if save:
        w = animation.FFMpegWriter(fps=ani['fps'],bitrate=1800)
        a.save(ani['name'], writer=w)
    plt.show()
    return chase


def main():
    if '-demo' in sys.argv:
        prey_seed, gene_sequence = utility.spawn_random_walk([100, 100], 270)
        pred_steps, prey_moves, caught = predatory_chase(prey_seed, {'start': [200, 200]})
        if caught:
            print 'Captured!'
        draw_chase(prey_moves, pred_steps, [250, 250], False, {'fps': 50, 'name': 'basic_chase.mp4'})


if __name__ == '__main__':
    main()
