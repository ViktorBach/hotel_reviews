import sqlite3


# Configuring the mricoservice for database access (essentially making a a connection)
def db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    
    return connection