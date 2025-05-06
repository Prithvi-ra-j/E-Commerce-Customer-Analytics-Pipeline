import pyodbc
conn = pyodbc.connect("DSN=ecommerce_dsn")
cursor = conn.cursor()
cursor.execute("SELECT * FROM customer_data LIMIT 5")
for row in cursor.fetchall():
    print(row)
conn.close()