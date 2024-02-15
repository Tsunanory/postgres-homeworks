CREATE TABLE customers_data(
	customer_id VARCHAR(6) PRIMARY KEY,
	company_name VARCHAR(60) NOT NULL,
	contact_name VARCHAR(40) NOT NULL
);

CREATE TABLE employees_data(
	employee_id SMALLINT PRIMARY KEY,
	first_name VARCHAR(15) NOT NULL,
	last_name VARCHAR(15) NOT NULL,
	title VARCHAR(50) NOT NULL,
	birth_date DATE NOT NULL,
	notes TEXT NOT NULL
);

CREATE TABLE orders_data(
	order_id SMALLINT PRIMARY KEY,
	customer_id VARCHAR(5) REFERENCES customers_data(customer_id),
	employees_id SMALLINT REFERENCES employees_data(employee_id),
	order_date DATE NOT NULL,
	ship_city VARCHAR(30)
);
