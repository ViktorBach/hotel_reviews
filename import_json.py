import json
import sqlite3

# load the data from JSON file
with open('guest_data.json', 'r') as f:
    guest_data = json.load(f)


conn = sqlite3('database.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Guest (
               GuestID INTEGER PRIMARY KEY,
               Firstname TEXT NOT NULL,
               Lastname TEXT NOT NULL,
               Email TEXT NOT NULL,
               Phone INTEGER,
               Review TEXT NOT NULL
)
''')

# inserting data from json into the guest table
for guest in guest_data:
    cursor.execute('''
INSERT INTO Guest (GuestID, Firstname, Lastname, Email, Phone, Review)
    VALUES (?, ?, ?, ?, ?, ?)
''', (
    guest["GuestID"],
    guest["Firstname"],
    guest["Lastname"],
    guest["Email"],
    guest["Phone"],
    guest["Review"]
))
    
# commit and close the connection
conn.commit()
conn.close()