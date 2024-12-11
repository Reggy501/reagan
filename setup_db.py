import sqlite3

# Connect to the database (it will create the file if it doesn't exist)
conn = sqlite3.connect('app.db')

# Create a cursor object
cursor = conn.cursor()

# Create the users table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    firstname TEXT NOT NULL,
    lastname TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    phone TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

# Commit changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully!")
