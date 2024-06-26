import pandas as pd

# Solution:
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    for index in employees.index:
        employees.loc[index, 'salary'] *= 2
    return employees

# Example:
employees = {
  "Name": ["John", "Steven", "Bob"],
  "salary": [5000, 4000, 4500]
}

# Modify another column:
data = pd.DataFrame(employees)

print(modifySalaryColumn(data))
def modifyNameColumn(data):
    for index in data.index:
        data.loc[index, 'Name'] = "Director " + data.loc[index, 'Name']
    return data

print(modifyNameColumn(data))
