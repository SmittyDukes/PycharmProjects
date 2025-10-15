import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Extended player stats
stats = pd.DataFrame({
    "points":   [30, 28, 25, 22, 27, 35, 18, 24],
    "assists":  [8, 6, 9, 4, 7, 10, 3, 5],
    "rebounds": [10, 9, 8, 7, 11, 12, 6, 8],
    "turnovers":[3, 2, 4, 5, 3, 6, 1, 3],
    "steals":   [2, 3, 1, 2, 4, 3, 2, 1],
    "blocks":   [1, 2, 1, 3, 2, 1, 2, 3],
    "fg_percent":[0.55, 0.48, 0.50, 0.44, 0.52, 0.60, 0.42, 0.46]
})

# 1️⃣ Compute correlation matrix
corr_matrix = stats.corr()

# 2️⃣ Plot heatmap
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", linewidths=0.5, square=True)
plt.title("Extended Player Stats Correlation Heatmap", fontsize=14)
plt.show()
corr_with_points = stats.corr()["points"].sort_values(ascending=False)
print(corr_with_points)
sns.barplot(
    x=corr_with_points.values,
    y=corr_with_points.index,
    hue=corr_with_points.index,   # use 'y' variable for color
    palette="coolwarm",
    legend=False
)
plt.title("Correlation Strength with Points")
plt.xlabel("Correlation Coefficient (r)")
plt.ylabel("Variable")
plt.show()

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
X = stats[["fg_percent"]]  # the input feature
y = stats["points"]         # the thing we want to predict
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

r2 = r2_score(y_test, y_pred)
print("R² Score:", round(r2, 2))
print("Coefficient (Slope):", model.coef_[0])
print("Intercept:", model.intercept_)

import seaborn as sns
import matplotlib.pyplot as plt

corr = df.corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', center=0)
plt.title("Player Stats Correlation Heatmap")
plt.show()