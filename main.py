import psycopg2

db = psycopg2.connect(
    database='jamaliddin`s',
    user='postgres',
    host='localhost', 
    password='252208'
)

cursor = db.cursor()

cursor.execute('''
    DROP TABLE IF EXISTS cars CASCADE;
    DROP TABLE IF EXISTS clients CASCADE;
    DROP TABLE IF EXISTS orders CASCADE; 
    DROP TABLE IF EXISTS employees CASCADE; 
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars(
        car_id SERIAL PRIMARY KEY,
        c_name VARCHAR(100) NOT NULL,
        c_model TEXT,
        c_date INTEGER,
        c_price NUMERIC(12, 2),
        c_is_sale BOOL DEFAULT TRUE
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS clients(
        client_id SERIAL PRIMARY KEY,
        c_name VARCHAR(50) NOT NULL,
        c_lastname VARCHAR(50),
        c_pnumber CHAR(13),
        c_address TEXT
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders(
        order_id SERIAL PRIMARY KEY,
        car_id INTEGER REFERENCES cars(car_id),
        client_id INTEGER REFERENCES clients(client_id),
        o_date DATE NOT NULL DEFAULT CURRENT_DATE,
        o_price NUMERIC(12, 2) DEFAULT 0
    );
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees(
        employee_id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL, 
        position VARCHAR(50) NOT NULL DEFAULT 'Ordinary Worker',
        salary NUMERIC(10, 2) 
    );
''')

cursor.execute('ALTER TABLE clients ADD COLUMN email VARCHAR(100);')
cursor.execute('ALTER TABLE clients RENAME COLUMN c_name TO name;')
cursor.execute('ALTER TABLE clients RENAME TO mijozlar;')

cursor.execute('''
    INSERT INTO cars (c_name, c_model, c_date, c_price, c_is_sale)
    VALUES 
        ('Toyota', 'Camry', 2020, 30000, TRUE),
        ('Honda', 'Civic', 2019, 25000, FALSE),
        ('BMW', 'X5', 2021, 60000, TRUE);
''')

cursor.execute('''
    INSERT INTO mijozlar (name, c_lastname, c_pnumber, c_address, email)
    VALUES 
        ('Ali', 'Valiyev', '+998901234567', 'Tashkent', 'ali@example.com'),
        ('Olim', 'Karimov', '+998907654321', 'Samarkand', 'olim@example.com');
''')

cursor.execute('''
    INSERT INTO orders (car_id, client_id, o_date, o_price)
    VALUES 
        (1, 1, '2023-01-10', 29000),
        (2, 2, '2023-02-15', 24500);
''')

cursor.execute('''
    INSERT INTO employees (name, position, salary)
    VALUES 
        ('Dilshod', 'Manager', 1200),
        ('Asad', 'Salesperson', 900),
        ('Shirin', 'Ordinary Worker', 800);
''')

cursor.execute("UPDATE employees SET name = 'Olim' WHERE employee_id = 1;")
cursor.execute("UPDATE employees SET name = 'Sardor' WHERE employee_id = 2;")

cursor.execute("DELETE FROM employees WHERE employee_id = 3;")

cursor.execute("SELECT * FROM employees;")
print("Xodimlar:", cursor.fetchall())

cursor.execute("SELECT * FROM cars;")
print("Cars:", cursor.fetchall())

cursor.execute("SELECT * FROM mijozlar;")
print("Mijozlar:", cursor.fetchall())
# cursor.execute("DROP TABLE IF EXISTS mijozlar;")


cursor.execute("SELECT * FROM orders;")
print("Orders:", cursor.fetchall())

db.commit()
cursor.close()
db.close()





































