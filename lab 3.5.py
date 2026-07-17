import pandas as pd

def main():
    employee = {
        "Department": ["HR", "IT", "Finance", "Marketing", "IT"],
        "Employee Name": ["Alice", "Bob", "Charlie", "David", "Emma"],
        "Salary": [35000, 50000, 45000, 40000, 55000]
    }


    df = pd.DataFrame(employee)


    print("Employee Details:")
    print(df)


    avg_salary = df.groupby("Department")["Salary"].mean()

    print("\nAverage Salary of Employees in Each Department:")
    print(avg_salary)





if __name__ == "__main__":
    main()
