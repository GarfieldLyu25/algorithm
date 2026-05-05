import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    employee = employee.drop_duplicates(['salary'])
    if len(employee['salary']) < 2:
        return pd.DataFrame({'SecondHighestSalary':[None]})
    employee = employee.sort_values('salary', ascending = False)[['salary']]
    employee = employee.rename(columns={'salary':'SecondHighestSalary'})
    return employee.head(2).tail(1)