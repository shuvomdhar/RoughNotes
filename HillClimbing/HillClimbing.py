# Hill Climbing Algorithm
# Implement the Hill Climbing algorithm to solve an optimization problem, such as maximizing a function.

import random

# Define the function to maximize
def objective_function(x):
    return -x**2 + 5*x + 20

# Define the hill climbing algorithm
def hill_climbing(initial_x, step_size=0.1, max_iterations=1000):
    current_x = initial_x
    current_value = objective_function(current_x)

    for iteration in range(max_iterations):
        # Generate neighbors by adding/subtracting a step size
        neighbors = [current_x + step_size, current_x - step_size]

        # Evaluate the neighbors
        next_x = max(neighbors, key=objective_function)
        next_value = objective_function(next_x)

        # Check if the best neighbor improves the objective function
        if next_value > current_value:
            current_x, current_value = next_x, next_value
        else:
            # Local maximum found
            break

        print(f"Iteration {iteration + 1}: x = {current_x:.4f}, f(x) = {current_value:.4f}")

    return current_x, current_value

# Get user input for the initial point
initial_x = float(input("Enter an initial x value: "))

# Run the Hill Climbing algorithm
solution_x, solution_value = hill_climbing(initial_x)

# Output the result
print("\nFinal Solution:")
print(f"x = {solution_x:.4f}, f(x) = {solution_value:.4f}")
