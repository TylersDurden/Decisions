import matplotlib.pyplot as plt, scipy.ndimage as ndi
import time, imutils, numpy as np, sys


class akashic:
    state = [[]]
    internal_thresh = 0
    break_limit = 0
    cloud = {}

    def __init__(self, dims, k_limit, e_limit, N, debug):
        self.state = np.zeros(dims)
        self.internal_thresh = k_limit
        self.break_limit = e_limit
        self.cloud = self.initialize_cloud(N, debug)

    def initialize_cloud(self, N, verbose):
        pt_cloud = {}
        for pt in range(N):
            [x, y] = imutils.spawn_random_point(self.state)
            pt_cloud[pt] = [x,y]
        if verbose:
            print str(len(pt_cloud.keys())) + " Particle Point Cloud Created"
        return pt_cloud

    def draw_cloud(self, show):
        for pt in self.cloud.keys():
            [x, y] = self.cloud[pt]
            self.state[x, y] = 1
        if show:
            plt.imshow(self.state, 'gray')
            plt.show()

    @staticmethod
    def clustering(n_generations, initial_state, k_thresh, noisy, sensitivity):
        reel = []
        kernel = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
        for gen in range(n_generations):
            state = np.array(initial_state).flatten()
            ii = 0
            minima = np.array(initial_state).min()
            mean = np.array(initial_state).mean()
            for cell in ndi.convolve(initial_state, kernel).flatten():
                if cell >= k_thresh + mean :
                    state[ii] = 0
                if cell == 0:
                    state[ii] = 1
                ii += 1
            initial_state = state.reshape(np.array(initial_state).shape)
            reel.append(initial_state)
            if noisy and ii > 0 and gen % 10 == 0:
                initial_state += imutils.draw_centered_circle(initial_state,
                                                              np.array(initial_state).shape[0] / 4,
                                                              mean, False)
            if noisy and ii > 0 and gen % 10 == 0:
                initial_state -= sensitivity*np.random.random_integers(0, 1, 10000).reshape(100, 100)/2

        return reel, initial_state


def main():
    dims = [250, 250]
    if '-cluster' in sys.argv:
        t0 = time.time()
        seeds = np.random.random_integers(0, 2, 10000).reshape(100, 100)
        # # Update the seed state before modifying # #
        sense = int(input('Enter Sensitivity: '))
        ani, state = akashic.clustering(155, seeds, 4, True, sense)
        t1 = time.time() - t0
        print '[' + str(t1) + 's Elapsed]'
        # conv = ndi.laplace(state)
        if '-s' in sys.argv:
            file_name = str(input('Enter the name of rendered video:'))
            imutils.bw_render(ani, frame_rate=80, save=True, fileNameOut=file_name)
        else:
            imutils.bw_render(ani, frame_rate=80, save=False, fileNameOut='')

    if len(sys.argv) < 2:
        npts = 5500
        field = akashic(dims, 4, 12, npts, True)
        field.draw_cloud(False)
        pts_in_fov, fov = imutils.rectangle_accounting(field.state, 50, 1, True)
        print '['+str(100*float(pts_in_fov)/(len(fov.flatten())))+\
              "% of FOV Filled With Points]"
        print '['+str(100*float(pts_in_fov)/npts)+'% of points inside Field of View]'
        imutils.draw_rectangle(field.state, 60, 1, True)


if __name__ == '__main__':
    main()






