import pandas as pd
dict1={"Name":["anu","reena","veena"],
       "mark":[85,95,75]
       }
df=pd.DataFrame(dict1)
filtered_df=df[df["mark"]>80]
print(filtered_df)
sorted_df=df.sort_values(by=["mark"],ascending=False)
print("Students with mark greater than 80(descending order):")
print(sorted_df)