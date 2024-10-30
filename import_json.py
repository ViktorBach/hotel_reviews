import json
import sqlite3

# Connect to SQLite (creates the database file if it doesn't exist)
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS Review')

# Create the Guest table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Review (
    ReviewID INTEGER PRIMARY KEY AUTOINCREMENT,
    GuestID INT,
    Rating INT NOT NULL,
    Comment TEXT,
    Date DATE
)
''')

# Read the CSV file and insert data into the table
with open('json_db.json', 'r') as file:
    json_data = json.load(file)

    # Insert data from CSV into the Guest table
    for row in json_data:
        cursor.execute('''
        INSERT INTO Review (GuestID, Rating, Comment, Date)
        VALUES (?, ?, ?, ?)
        ''', (
            row["GuestID"],
            row["Rating"],
            row["Comment"],
            row["Date"]
        ))

# Commit and close the connection
conn.commit()
conn.close()

print("Data successfully imported to SQLite database :)")
