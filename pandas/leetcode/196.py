import pandas as pd

def delete_duplicate_emails(person: pd.DataFrame) -> None:
    min_id = person.groupby('email')['id'].transform('min')
    person.drop(person[person['id'] != min_id].index, inplace=True)
    return