import scipy.ndimage as ndi
import numpy as np
import utility
''' <GENETIC_ALGORITHMS> 

[1] Create Target Population
[2] Evaluate fitness of each individual
[3] Regenerate based on fitness and repeat

*2: Caveats of Step 2
  - Most fit individuals are selected as parents
  - Breed new individuals through crossover and 
    mutation.
  - Replace least fit with new generations. 

<GENETIC_ALGORITHMS> 
'''


def generate_population(individuals, m):
    seed_population = {}
    for i in range(individuals):
        seed_population[i] = np.array(np.random.random_integers(0, m, m*m)).reshape((m, m))
    return seed_population


def seed_genetic_pool(genes_per_individual, n_individuals):
    dimensions = [3, 3]
    initial_population = {}
    for i in range(n_individuals):
        individual = generate_population(genes_per_individual, dimensions[0])
        initial_population[i] = individual
    return initial_population


def breed(population, gene_pool, generations):
    chromosomes = {}
    layers = {}
    ii = 0
    for individual in population.values():
        genetics = gene_pool.values().pop(ii)
        ii += 1
        layer = np.zeros(individual.shape)
        chromo = []
        for gene in genetics.values():
            chroma = ndi.convolve(individual,gene)
            chromo.append(chroma)
            layer += chroma
        chromosomes[ii] = chromo
        layers['Blend_Layer '+str(ii)] = layer
    return chromosomes, layers


def main():
    gene_pool = seed_genetic_pool(16, 10)
    starting_population = generate_population(9, 120)
    chromosomes, layer = breed(starting_population, gene_pool, 5)
    utility.filter_preview(layer)


if __name__ == '__main__':
    main()
