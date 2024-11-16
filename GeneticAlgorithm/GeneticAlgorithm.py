# Genetic Algorithm for Optimization
# Write a Python program to solve an optimization problem using Genetic Algorithms.

import random

# Define the objective function to maximize
def objective_function(x):
    return -x**2 + 5*x + 20

# Generate an initial population
def generate_population(size, x_min, x_max):
    return [random.uniform(x_min, x_max) for _ in range(size)]

# Select individuals for mating pool (Tournament Selection)
def selection(population, fitnesses, num_parents):
    selected_parents = []
    for _ in range(num_parents):
        # Tournament of two randomly chosen individuals
        i, j = random.sample(range(len(population)), 2)
        if fitnesses[i] > fitnesses[j]:
            selected_parents.append(population[i])
        else:
            selected_parents.append(population[j])
    return selected_parents

# Perform crossover (single-point crossover)
def crossover(parent1, parent2):
    # Averaging two parents to create offspring
    return (parent1 + parent2) / 2

# Perform mutation
def mutate(individual, mutation_rate, x_min, x_max):
    if random.random() < mutation_rate:
        return individual + random.uniform(-1, 1)  # Small mutation step
    return individual

# Genetic Algorithm
def genetic_algorithm(pop_size, generations, x_min, x_max, mutation_rate):
    # Initialize population
    population = generate_population(pop_size, x_min, x_max)

    for generation in range(generations):
        # Evaluate fitness of each individual
        fitnesses = [objective_function(x) for x in population]

        # Select the best individuals to be parents
        parents = selection(population, fitnesses, pop_size // 2)

        # Generate the next generation
        next_generation = []
        while len(next_generation) < pop_size:
            parent1, parent2 = random.sample(parents, 2)
            offspring = crossover(parent1, parent2)
            offspring = mutate(offspring, mutation_rate, x_min, x_max)
            next_generation.append(offspring)

        # Update the population with the next generation
        population = next_generation

        # Print the best solution in the current generation
        best_individual = max(population, key=objective_function)
        best_fitness = objective_function(best_individual)
        print(f"Generation {generation + 1}: x = {best_individual:.4f}, f(x) = {best_fitness:.4f}")

    # Return the best solution found
    best_individual = max(population, key=objective_function)
    return best_individual, objective_function(best_individual)

# Parameters for the Genetic Algorithm
population_size = int(input("Enter population size: "))
num_generations = int(input("Enter number of generations: "))
x_min = float(input("Enter minimum x value: "))
x_max = float(input("Enter maximum x value: "))
mutation_rate = float(input("Enter mutation rate (0-1): "))

# Run the Genetic Algorithm
solution_x, solution_value = genetic_algorithm(population_size, num_generations, x_min, x_max, mutation_rate)

# Output the result
print("\nBest solution found:")
print(f"x = {solution_x:.4f}, f(x) = {solution_value:.4f}")
