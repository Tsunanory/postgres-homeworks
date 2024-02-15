import psycopg2
import pandas as pd
import re

customers = pd.read_csv('north_data/customers_data.csv')
employees = pd.read_csv('north_data/employees_data.csv')
orders = pd.read_csv('north_data/orders_data.csv')

cdf = pd.DataFrame(customers)
edf = pd.DataFrame(employees)
odf = pd.DataFrame(orders)


conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='password'
)
try:
    with conn:
        with conn.cursor() as cur:

            for row in cdf.itertuples():
                cur.execute('''
                INSERT INTO customers_data (customer_id, company_name, contact_name)
                VALUES (%s, %s, %s)
                ''',
                            (row.customer_id,
                row.company_name,
                row.contact_name)
                )

            for row in edf.itertuples():
                cur.execute('''
                INSERT INTO employees_data (employee_id, 
                first_name, last_name, title, birth_date, notes)
                VALUES (%s, %s, %s, %s, %s, %s)
                ''',
                (row.employee_id, row.first_name, row.last_name,
                 row.title, row.birth_date, row.notes)
                )

            for row in odf.itertuples():
                cur.execute('''
                INSERT INTO orders_data (order_id, 
                customer_id, employees_id, order_date, ship_city)
                VALUES (%s, %s, %s, %s, %s)
                ''',
                (row.order_id, row.customer_id, row.employee_id,
                row.order_date, row.ship_city)
                )

finally:
    conn.close()

