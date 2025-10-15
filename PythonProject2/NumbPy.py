import numpy as np
points = [25, 30, 28]
np_points = np.array(points)

print(np_points)
print(type(np_points))

# Each operation applies to every element
print(np_points + 5)      # add 5 to every game
print(np_points * 2)      # double every value
print(np_points / 2)      # divide every value

print("Total:", np_points.sum())
print("Average:", np_points.mean())
print("Highest:", np_points.max())
print("Lowest:", np_points.min())
print("Standard deviation:", np_points.std())

team = np.array([
    [25, 30, 28],   # Player 1 scores
    [20, 22, 18]    # Player 2 scores
])

print("Shape:", team.shape)   # (rows, columns)
print("Player 1 average:", team[0].mean())
print("Team average:", team.mean())

lebron = np.array([30, 28, 25])
ad = np.array([22, 18, 20])

print("Dot product:", np.dot(lebron, ad))

lebron = np.array([30, 7, 8])
ad = np.array([22, 3, 10])

print(np.dot(lebron, ad))

A = np.array([1, 2, 3])
B = np.array([4, 5, 6])
print(np.dot(A, B))

points = np.array([30, 28, 25, 22, 27, 35])
print(np.mean(points))
print(np.median(points))
print(np.min(points) - np.max(points))
print(np.var(points))
print(np.std(points))

import numpy as np
player_A = np.array([70, 68, 72, 69, 71, 70, 69, 72, 70, 71])

# Player B - streaky
player_B = np.array([55, 80, 65, 75, 60, 85, 50, 90, 70, 55])

# Calculate variance and standard deviation for both
var_A = np.var(player_A)
std_A = np.std(player_A)

var_B = np.var(player_B)
std_B = np.std(player_B)

print("Player A Variance:", var_A)
print("Player A Std Dev:", std_A)
print("Player B Variance:", var_B)
print("Player B Std Dev:", std_B)

data = np.array([5, 7, 8, 6, 9])
var = np.var(data)
std = np.std(data)

print(f"Variance: {var:.2f}")
print(f"Std Dev: {std:.2f}")

points = [24, 28, 25, 23, 30]

print(np.mean(points))
print(np.median(points))
print(np.max(points) - np.min(points))
var = np.var(points)
std = np.std(points)
print(var)
print(std)

import matplotlib.pyplot as plt

# Settings
# Settings
p_make = 0.7
num_trials = 1000
shot_sizes = [10, 100, 1000]  # small, medium, large samples

plt.figure(figsize=(15, 5))

for i, shots_per_trial in enumerate(shot_sizes, 1):
    empirical_probs = []

    for _ in range(num_trials):
        shots = np.random.choice([1, 0], size=shots_per_trial, p=[p_make, 1 - p_make])
        empirical_probs.append(np.mean(shots))

    plt.subplot(1, 3, i)
    plt.hist(empirical_probs, bins=25, color='skyblue', edgecolor='black', alpha=0.8)
    plt.axvline(p_make, color='red', linestyle='--', linewidth=2, label='True P = 0.7')
    plt.title(f'{shots_per_trial} Shots per Trial', fontsize=12, fontweight='bold')
    plt.xlabel('Empirical Probability')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

# 1️⃣ Data (you could imagine this came from a NumPy array or CSV)
games = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
player_a = [25, 30, 22, 28, 35, 27, 29, 26, 31, 33]
player_b = [18, 20, 24, 26, 28, 22, 25, 30, 29, 27]

# 2️⃣ Create the chart
plt.figure(figsize=(10, 6))
plt.plot(games, player_a, color='orange', marker='o', linewidth=2, label='Player A')
plt.plot(games, player_b, color='blue', marker='s', linewidth=2, label='Player B')
# 3️⃣ Add labels, title, and legend
plt.title("Player Scoring Trend (Last 10 Games)", fontsize=14, fontweight='bold')
plt.xlabel("Game Number", fontsize=12)
plt.ylabel("Points Scored", fontsize=12)
plt.legend()

# 4️⃣ Add a grid and custom axis limits for style
plt.grid(True, alpha=0.3)
plt.ylim(15, 40)

# 5️⃣ Display it
plt.show()

assists = [3, 5, 7, 9, 11]
points = [15, 20, 28, 30, 35]

plt.scatter(assists, points, color="red")
plt.title("Assists vs Points")
plt.xlabel("Assists")
plt.ylabel("Points")
plt.grid(True, alpha=0.3)

plt.show()


scores = [20, 22, 25, 30, 35, 36, 38, 40, 42, 45]
plt.boxplot(scores)
plt.title("Score Spread")
plt.ylabel("Points")
plt.show()


import numpy as np

minutes = np.array([30, 45, 60, 75, 90])
makes   = np.array([4, 6, 8, 10, 12])

r = np.corrcoef(minutes, makes)[0, 1]
print("Correlation:", round(r, 2))
