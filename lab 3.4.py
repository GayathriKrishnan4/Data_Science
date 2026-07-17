import pandas as pd


data = {
    "Name": ["Alice", "Bob", None, "David"],
    "Age": [20, None, 19, 22],
    "Marks": [85, 90, None, 92]
}

df = pd.DataFrame(data)


print("DataFrame:")
print(df)


print("\nMissing Values:")
print(df.isnull())


print("\nNumber of Missing Values in Each Column:")
print(df.isnull().sum())
