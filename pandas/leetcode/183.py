import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # 找出没有下过订单的客户
    result = customers[~customers['id'].isin(orders['customerId'])]
    return result[['name']].rename(columns={'name':'Customers'})