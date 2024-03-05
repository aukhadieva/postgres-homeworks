import os
ROOT = os.path.dirname(__file__)

PASSWORD = os.getenv('PSQL_PASSWORD')
CUSTOMERS = os.path.join(ROOT, 'homework-1', 'north_data', 'customers_data.csv')
EMPLOYEES = os.path.join(ROOT, 'homework-1', 'north_data', 'employees_data.csv')
ORDER_DATA = os.path.join(ROOT, 'homework-1', 'north_data', 'orders_data.csv')
