DROP TABLE IF EXISTS cars CASCADE;
DROP TABLE IF EXISTS clients CASCADE;
DROP TABLE IF EXISTS orders; 
DROP TABLE IF EXISTS employees;



CREATE TABLE IF NOT EXISTS cars(
    car_id SERIAL PRIMARY KEY,
    c_name VARCHAR(100) NOT NULL,
    c_model TEXT,
    c_date INTEGER,
    c_price NUMERIC(12, 2),
    c_is_sale BOOL DEFAULT TRUE
);

CREATE TABLE IF NOT EXISTS clients(
	client_id SERIAL PRIMARY KEY,
    c_name VARCHAR(50) NOT NULL,
    c_lastname VARCHAR(50),
    c_pnumber CHAR(13),
    c_address TEXT
);

CREATE TABLE IF NOT EXISTS orders(
    order_id SERIAL PRIMARY KEY,
    car_id INTEGER REFERENCES cars(car_id),
    client_id INTEGER REFERENCES clients(client_id),
    o_date DATE NOT NULL DEFAULT CURRENT_DATE,
    o_price NUMERIC(12, 2) DEFAULT 0
);

CREATE TABLE IF NOT EXISTS employees(
    employee_id SERIAL PRIMARY KEY,
	name VARCHAR(50) NOT NULL, 
    position VARCHAR(50) NOT NULL DEFAULT 'Ordinary Worker',
	salary NUMERIC(10, 2) 
);

ALTER TABLE clients ADD COLUMN email VARCHAR(100);
ALTER TABLE clients RENAME COLUMN c_name TO name;
ALTER TABLE clients RENAME TO mijozlar;

