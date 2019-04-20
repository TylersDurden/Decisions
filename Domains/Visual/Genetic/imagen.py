import matplotlib.pyplot as plt
import scipy.ndimage as ndi
import numpy as np
import utility


def generate_random_squares(n_squares, N, fine, show):
    squares = []
    sqN = int(np.sqrt(N))
    for square in range(n_squares):
        if fine==0:
            squares.append(np.random.random_integers(0, 2, N).reshape((sqN, sqN)))
        else:
            genes = np.random.random_integers(0, 2, N) < fine
            squares.append(np.array(genes).reshape((sqN, sqN)))
    if show:
        utility.bw_render(squares, 1000, False, '')
    return squares


def create_gene_sequence(N, show, fine):
    # Generate an initial population of genetic blocks
    seed_genes = generate_random_squares(10, N, fine, show)

    sequence = np.random.random_integers(0, len(seed_genes) - 1, len(seed_genes))
    genome = seed_genes[0]
    for s in sequence:
        genome = np.concatenate((genome, seed_genes[s]), 0)
    if show:
        plt.imshow(genome, 'gray')
        plt.show()

    return genome, seed_genes, sequence


def splice_sequece_into_genome(sequence_data):
    n_sequences = len(sequence_data.keys())
    print 'Splicing ' + str(n_sequences) + ' Sequences Together'


class Imagination:
    image_library = {}

    def __init__(self, imat, title):
        self.image_library[title] = imat
        self.isolate()

    def isolate(self):
        count = 0
        mapping = {}
        for pixel in np.array(self.image_library.values().pop()).flatten():
            if pixel >0:
                count += 1
        print str(count) + " Pixels Found"


def main():

    k0 = [[0,0,1,1,0,0],
          [0,1,1,1,1,0],
          [1,1,1,1,1,1],
          [1,1,1,1,1,1],
          [0,1,1,1,1,0],
          [0,0,1,1,0,0]]

    k1 = [[]]

    # CREATE GOAL/Engine IMAGE
    goal = plt.imread('wfn.png')[200:400, 1200:1400, 0]
    plt.imshow(ndi.convolve(goal,k0,origin=0), 'gray')
    plt.show()
    ##

    goal_shape = goal.shape
    goal_pixel_count = goal_shape[0] * goal_shape[1]
    Imagination(goal, 'GOAL')
    print 'GoalState PixelCount: ' + str(goal_pixel_count)
    print 'GoalState Shape: ' + str(goal_shape)

    N = 49
    dna, seed, genetics = create_gene_sequence(N, True, fine=0)
    print dna.shape


if __name__ == '__main__':
    main()
