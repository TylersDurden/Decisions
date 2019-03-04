import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utility


def create_egg(show, state_size, egg_radius,n_particles):
    r = int(egg_radius*0.6)
    circle = utility.draw_centered_circle(np.zeros((state_size, state_size)),r, False)
    # text = utility.draw_text('EGG', utility.create_font_mappings(), False)
    # cx = state_size / 2
    # circle[0:40, cx:text.shape[1] + cx] += text[0:40, :]
    state, cloud = utility.create_point_cloud(250, egg_radius, n_particles, False)
    egg = circle - state
    if show:
        plt.imshow(egg, 'gray')
        plt.show()
    return egg


def simulation(egg, egg_size, steps):
    f1 = [[1, 1, 1],  # Min ~1/2
          [1, 0, 1],  # Max = 8
          [1, 1, 1]]  # Edges ~ 3-4
    f2 = [[1, 1, 0, 0, 1, 1],  # Min = 2
          [1, 1, 0, 0, 1, 1],  # Max = 16
          [0, 0, 0, 0, 0, 0],  # Edges ~ 2-4
          [0, 0, 0, 0, 0, 0],
          [1, 1, 0, 0, 1, 1],
          [1, 1, 0, 0, 1, 1]]

    simulation = []
    for step in range(steps):
        e = egg.flatten()
        contact = ndi.convolve(egg, f1)
        reach = ndi.convolve(egg, f2).flatten()

        cavg = np.array(contact.flatten()).mean()
        ravg = np.array(reach).mean()

        ii = 0
        for cell in contact.flatten():
            if cell == 8 and reach[ii] > ravg:
                 e[ii] = 0
            if cell == 8 and reach[ii] < ravg:
                 e[ii] = 0
            # if cell == cavg and reach[ii] < 4:
            #     e[ii] = 1
            if cell >= 3 and cell == ravg:
                e[ii] = 1
            # if cell == ravg and cell <= 3 and e[ii] == 1:
            #     e[ii] = 0
            if e[ii] == 1 and cell == cavg and cell == ravg:
                e[ii] = 0
            # if e[ii] == 0 and cell == cavg and cell == ravg:
            #     e[ii] = 1
            if reach[ii] == 16 and cell == 8:
                e[ii] = 1
            if e[ii] == 0 and reach[ii] == 4 and cell == 3:
                e[ii] = 0
            ii += 1
        egg = np.array(e).reshape(egg.shape)
        simulation.append(egg)
        err, cloud = utility.create_point_cloud(egg.shape[0], egg_size, 10, False)
        egg += err
    return simulation


def main():
    state_size = 250
    egg_size = 124
    n_particles = 300
    egg = create_egg(False, state_size, egg_size, n_particles)

    # RUN SIMULATION LOOP
    steps = 100
    film = simulation(egg, egg_size, steps)
    utility.bw_render(film, 125, False, '')


if __name__ == '__main__':
    main()
