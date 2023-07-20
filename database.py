import sqlite3

def table_exists(conn, table_name):
    result = conn.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
    return bool(result.fetchone())

def create_tables(conn):
    if not table_exists(conn, 'users'):
        conn.execute('''CREATE TABLE users 
                        (userId INTEGER PRIMARY KEY, 
                        password TEXT,
                        email TEXT,
                        firstName TEXT,
                        lastName TEXT,
                        address1 TEXT,
                        address2 TEXT,
                        zipcode TEXT,
                        city TEXT,
                        state TEXT,
                        country TEXT, 
                        phone TEXT
                        )''')
        print("Table 'users' created.")

    if not table_exists(conn, 'products'):
        conn.execute('''CREATE TABLE products
                        (productId INTEGER PRIMARY KEY,
                        name TEXT,
                        price REAL,
                        description TEXT,
                        image TEXT,
                        stock INTEGER,
                        categoryId INTEGER,
                        FOREIGN KEY(categoryId) REFERENCES categories(categoryId)
                        )''')
        print("Table 'products' created.")

    if not table_exists(conn, 'kart'):
        conn.execute('''CREATE TABLE kart
                        (userId INTEGER,
                        productId INTEGER,
                        FOREIGN KEY(userId) REFERENCES users(userId),
                        FOREIGN KEY(productId) REFERENCES products(productId)
                        )''')
        print("Table 'kart' created.")

    if not table_exists(conn, 'categories'):
        conn.execute('''CREATE TABLE categories
                        (categoryId INTEGER PRIMARY KEY,
                        name TEXT
                        )''')
        print("Table 'categories' created.")

if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    create_tables(conn)
    conn.close()
