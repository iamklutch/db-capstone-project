import mysql.connector as connector

connection = connector.connect(user='admin', password='admin')

cursor = connection.cursor()

cursor.execute('USE little_lemon_db')

join_query = """
SELECT 
	Bookings.BookingID,
	Bookings.TableNumebr, 
	Bookings.CustomerID,
	Orders.Cost,
FROM Bookings
LEFT JOIN Orders ON Bookings.BookingID = Orders.BookingID
WHERE Orders.Cost >60
"""

cursor.execute(join_query)
results = cursor.fetchall()

print(cursor.column_names)
print(results)
