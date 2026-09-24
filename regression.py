import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Dataset
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 8, 10])

# Create model
model = LinearRegression()
model.fit(X, y)

# Prediction
y_pred = model.predict(X)

print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Predicted values:", y_pred)

# Plot
plt.scatter(X, y, color="blue")
plt.plot(X, y_pred, color="red")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Linear Regression")
plt.savefig("regression_plot.png")