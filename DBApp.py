import mysql.connector

group_number= "15" #FILL IN YOUR GROUP NUMBER
remote_connection = input('If accessing database with remote connection, write: "yes", else "no":\n')

if remote_connection == "yes":
  mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_2_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_2_hotels_group_"+group_number
)
else:
  mydb = mysql.connector.connect(
    host="groucho.it.uu.se",
    user="ht21_2_group_"+group_number,
    passwd="pwd_"+group_number,
    database="ht21_2_hotels_group_"+group_number
  )

mycursor = mydb.cursor()
name="\"Golden Nugget\""
mycursor.execute("SELECT EANHotelID, Name FROM Property WHERE Name = "+name)

myresult = mycursor.fetchall()
print("EANHotelID\t Name")
for x in myresult:
  print(str(x[0])+"\t"+x[1])

mydb.close()