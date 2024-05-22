"""
This module contains functions for interacting with the database.
"""

import psycopg2

#connect to chinook database
connection = psycopg2.connect(database = "chinook")

#build a cursor object of the connection
cursor = connection.cursor()

#fetch the results (multiple)
results = cursor.fetchall()

#close the connection
connection.close()

#print the results
for result in results:
    print(result)
