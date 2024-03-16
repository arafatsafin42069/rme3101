import numpy as np

# Define the grid size
grid_size = (5, 5)

# Define the rewards for each state
rewards = np.random.rand(*grid_size)  # Random rewards for each state

# Define the transition probabilities
# Example: 0.8 for moving in the intended direction, 0.1 for moving in each of the other directions
probabilities = {
    'up': 0.8,
    'down': 0.1,
    'left': 0.1,
    'right': 0.1
}

# Run the Value Iteration algorithm
optimal_values, optimal_policy = value_iteration(grid_size, rewards, probabilities)

print("Optimal Values:")
print(optimal_values)
print("Optimal Policy:")
print(optimal_policy)