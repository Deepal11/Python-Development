import mysql.connector

#connect to mysql database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="1234",
  database="db"
)

#create cursor
mycursor = mydb.cursor(buffered=True)

#create database
#mycursor.execute("CREATE DATABASE db")

#DROP table only if it exists
mycursor.execute("DROP TABLE IF EXISTS customers")

#CREATE table
mycursor.execute("CREATE TABLE customers (name VARCHAR(30), address VARCHAR(50))")

#ALTER table
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

#INSERT into table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)

#INSERT multiple rows
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql, val)

#COMMIT changes
mydb.commit()

#SELECT
mycursor.execute("SELECT * FROM customers")
for x in mycursor.fetchall():
    print(x)

print()
#SELECT columns
mycursor.execute("SELECT name, address FROM customers")
for x in mycursor.fetchall():
    print(x)

print()
#using fetchone()
mycursor.execute("SELECT * FROM customers")
result = mycursor.fetchone()
print(result)

print()
#WGERE clause

mycursor.execute("SELECT * FROM customers WHERE address ='Park Lane 38'")
for x in mycursor.fetchall():
    print(x)


print()
#filter rows using LIKE
mycursor.execute("SELECT * FROM customers WHERE address LIKE '%way%'")
for x in mycursor.fetchall():
    print(x)

print()
#sort in ascending order
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)
for x in mycursor.fetchall():
    print(x)

print()
#sort in descending order
mycursor.execute("SELECT * FROM customers ORDER BY name DESC")
for x in mycursor.fetchall():
    print(x)

print()
#DELETE record
mycursor.execute("DELETE FROM customers WHERE address = 'Mountain 21'")
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

print()
#UPDATE record
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ("Valley 345", "Canyon 123")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) updated")

print()
#LIMIT the number of records
mycursor.execute("SELECT * FROM customers LIMIT 5")
for x in mycursor.fetchall():
    print(x)

print()
#OFFSET (to start from another position)
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
for x in mycursor.fetchall():
    print(x)

#DROP table
mycursor.execute("DROP TABLE customers")

mycursor.close()
mydb.close()
