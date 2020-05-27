import pyodbc

# Connect to driver
conn = pyodbc.connect('DRIVER=Devart ODBC Driver for MySQL;User ID=root; \
                      Password=1234;Data Source=localhost;Database=db')

# Create cursor
cur = conn.cursor()

# SELECT
cur.execute('SELECT * from customers')
for x in cur.fetchall():
    print(x)

# INSERT
query = "INSERT INTO customers (name, address) VALUES (?, ?)"
val = ("Michelle", "Blue Village")
cur.execute(query, val)
conn.commit()

print()
# UPDATE
cur.execute("UPDATE customers SET address = 'Valley 345' WHERE address = 'Mountain 21'")
conn.commit()
print(cur.rowcount, "record(s) updated")

print()
# DELETE
cur.execute("DELETE FROM customers WHERE address = 'Apple st 652'")
conn.commit()
print(cur.rowcount, "record(s) deleted")

# Close cursor and connection
cur.close()
conn.close()
