import matplotlib.pyplot as plt
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



def seed_genetic_pool(genes_per_individual, n_individuals):
    dimensions = [3, 3]
    initial_population = {}
    for i in range(n_individuals):
        individual = generate_seed_population(genes_per_individual, dimensions)
        initial_population[i] = individual
    return initial_population


seed_population = seed_genetic_pool(16, 100)