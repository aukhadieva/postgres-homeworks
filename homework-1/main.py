"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import random
import psycopg2

from config import PASSWORD, ORDER_DATA, CUSTOMERS, EMPLOYEES


def open_file(file_name: str) -> list:
    """
    Открывает csv файл на чтение, возвращает список словарей.
    """
    with open(file_name, newline='') as file:
        reader = csv.DictReader(file)
        row_list = []
        for row in reader:
            row_list.append(row)
        return row_list


def execute_connection(row_list: list) -> None:
    """
    Подключается к базе данных PostgreSQL.
    Создает курсор для переменной connection.
    Выполняет запрос к базе данных и добавляет данные из списка в таблицы.
    """
    with psycopg2.connect(database='north', user='postgres', password=PASSWORD) as connection:
        with connection.cursor() as cursor:

            try:
                counter_id = 0
                for item in row_list:
                    counter_id += 1
                    cursor.execute('INSERT INTO orders VALUES (%s, %s, %s)',
                                   (counter_id, item['order_date'], item['ship_city']))
            except KeyError:
                pass

            try:
                counter_id = 0
                for item in row_list:
                    counter_id += 1
                    cursor.execute('INSERT INTO customers VALUES (%s, %s, %s)',
                                   (counter_id, item['company_name'], item['contact_name']))
            except KeyError:
                pass

            try:
                counter_id = 0
                counter_city = 0
                for row in row_list:
                    counter_id += 1
                    counter_city = counter_city + random.randint(1, 10)
                    counter_employer_name = random.randint(1, 9)
                    cursor.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)',
                                   (counter_id, row['first_name'], row['last_name'], row['notes'],
                                    counter_city, counter_employer_name))
            except KeyError:
                pass

    connection.close()



if __name__ == '__main__':
    orders_data = open_file(ORDER_DATA)
    customers_data = open_file(CUSTOMERS)
    employees_data = open_file(EMPLOYEES)
    filled_orders = execute_connection(orders_data)
    filled_customers = execute_connection(customers_data)
    filled_employees = execute_connection(employees_data)
