import pandas as pd
dict1={"Name":["anu","reena","veena"],
       "age":[23,26,25],
       "city":["KTM","EKM","IDK"]
       }
df=pd.DataFrame(dict1)
df.to_csv("students.csv",index=False)
df=pd.read_csv("students.csv")
print("First row:")
print(df.head(1))
print("last row:")
print(df.tail(1))