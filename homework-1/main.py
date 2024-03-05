"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import random
import psycopg2
import os

from config import ROOT

PASSWORD = os.getenv('PSQL_PASSWORD')
CUSTOMERS = os.path.join(ROOT, 'homework-1', 'north_data', 'customers_data.csv')
EMPLOYEES = os.path.join(ROOT, 'homework-1', 'north_data', 'employees_data.csv')
ORDER_DATA = os.path.join(ROOT, 'homework-1', 'north_data', 'orders_data.csv')

with psycopg2.connect(database='north', user='postgres', password=PASSWORD) as connection:
    with connection.cursor() as cursor:

        with open(ORDER_DATA, newline='') as file:
            reader = csv.DictReader(file)

            counter_id = 0
            for row in reader:
                counter_id = counter_id + 1
                cursor.execute('INSERT INTO orders VALUES (%s, %s, %s)',
                               (counter_id, row['order_date'], row['ship_city']))

        with open(CUSTOMERS, newline='') as file:
            reader = csv.DictReader(file)

            counter_id = 0
            for row in reader:
                counter_id = counter_id + 1
                cursor.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                               (counter_id, row['company_name'], row['contact_name']))

        with open(EMPLOYEES, newline='') as file:
            reader = csv.DictReader(file)

            counter_id = 0
            counter_city = 0
            for row in reader:
                counter_id = counter_id + 1
                counter_city = counter_city + random.randint(1, 10)
                counter_employer_name = random.randint(1, 9)
                cursor.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                               (counter_id, row['first_name'], row['last_name'], row['notes'],
                                counter_city, counter_employer_name))


connection.close()
