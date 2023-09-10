Python 3.11.2 (v3.11.2:878ead1ac1, Feb  7 2023, 10:02:41) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
import numpy as np
import math
D_center = 110  
alpha = math.radians(1.5) 
theta = math.radians(120)  
width = 4 * 1852 
d_min = 2 * D_center * math.tan(theta/2) * 0.10 
d_max = 2 * D_center * math.tan(theta/2) * 0.20 
population_size = 100
num_generations = 200
elite_size = int(0.1 * population_size)
num_crossover_points = 1
def fitness(chromosome):
    coverage = 0
    last_line = 0
    for line in chromosome:
        D = D_center - abs(line - width/2) * math.tan(alpha)
        coverage_width = 2 * D * math.tan(theta/2)
        overlap = coverage_width - (line - last_line)
        if overlap < d_min or overlap > d_max:
...             return 0 
...         coverage += coverage_width
...         last_line = line
...     if last_line + coverage_width < width:
...         return 0
...     return coverage
... def crossover(parent1, parent2):
...     point = np.random.randint(1, len(parent1))
...     child1, child2 = parent1.copy(), parent2.copy()
...     child1[point:], child2[point:] = parent2[point:], parent1[point:]
...     return child1, child2
... def adaptive_mutation(chromosome, fitness_value, fitness_values):
...     if fitness_value < np.mean(fitness_values):
...         mutation_rate = 0.3 
...     else:
...         mutation_rate = 0.1 
... 
...     if np.random.rand() < mutation_rate:
...         mutation_point = np.random.randint(len(chromosome))
...         chromosome[mutation_point] += np.random.uniform(-d_min/10, d_min/10)
... def enhanced_genetic_algorithm():
...     population = np.random.uniform(low=d_min, high=d_max, size=(population_size, int(width/d_min)))
...     for generation in range(num_generations):
...         fitness_values = [fitness(chromo) for chromo in population]
...         elite_indices = np.argsort(fitness_values)[-elite_size:]
...         new_population = [population[i] for i in elite_indices]
...         while len(new_population) < population_size:
...             parents = np.argsort(fitness_values)[-2:]
...             child1, child2 = crossover(population[parents[0]], population[parents[1]])
...             new_population.extend([child1, child2])
...             for chromo in new_population[-2:]:
...                 adaptive_mutation(chromo, fitness(chromo), fitness_values)
...         population = np.array(new_population)
...     return population[np.argmax([fitness(chromo) for chromo in population])]
... best_solution = enhanced_genetic_algorithm()
