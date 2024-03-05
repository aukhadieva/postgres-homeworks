CREATE TABLE employees
(
	employees_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20),
	notes text,
	city int UNIQUE REFERENCES orders(orders_id),
	employer_name int REFERENCES customers(customer_id)
);

CREATE TABLE customers
(
	customer_id int PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50)
);

CREATE TABLE orders
(
	orders_id int PRIMARY KEY,
	order_date varchar(10),
	ship_city varchar(30)
);

SELECT * FROM employees
