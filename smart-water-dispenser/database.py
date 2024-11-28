import mysql.connector
import time

# Database connection details
mydb = mysql.connector.connect(
  host="13.50.241.8:3306",
  username="root",
  password="password",
  database="smart_water_dispencer"
)

mycursor = mydb.cursor()

def insert_data(distance, water_flow):
  sql = "INSERT INTO sensor_data (distance, water_flow) VALUES (%s, %s)"
  val = (distance, water_flow)
  mycursor.execute(sql, val)
  mydb.commit()

# ... (rest of your Python code)

# Assuming you have a distance and water_flow value:
distance = 20.5
water_flow = 1

insert_data(distance, water_flow)

mycursor.close()
mydb.close()
