# KNN Classification in Python

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. Load dataset
iris = load_iris()
X = iris.data
y = iris.target

# 2. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# 4. Create KNN classifier
k = 5
knn = KNeighborsClassifier(n_neighbors=k)

# 5. Train the model
knn.fit(X_train, y_train)

# 6. Make predictions
y_pred = knn.predict(X_test)

# 7. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)

print("Accuracy:", accuracy)
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# 8. Predict a new sample
new_sample = [[5.1, 3.5, 1.4, 0.2]]
new_sample = scaler.transform(new_sample)

prediction = knn.predict(new_sample)

print("Predicted class:", iris.target_names[prediction[0]])