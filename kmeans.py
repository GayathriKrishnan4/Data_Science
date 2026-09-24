from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load dataset
data = load_iris()
X = data.data[:, :2]

# Create K-Means model
model = KMeans(n_clusters=3, random_state=42, n_init=10)
model.fit(X)

# Cluster labels
labels = model.labels_

print("Cluster labels:")
print(labels)

print("\nCluster centers:")
print(model.cluster_centers_)

# Plot clusters
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis')
plt.scatter(
    model.cluster_centers_[:, 0],
    model.cluster_centers_[:, 1],
    color='red',
    marker='X',
    s=200
)

plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")
plt.title("K-Means Clustering")
plt.show()
