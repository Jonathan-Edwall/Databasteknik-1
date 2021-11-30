import mysql.connector

group_number= "15" #FILL IN YOUR GROUP NUMBER
remote_connection = input('If accessing database with remote connection, write: "yes", else "no":\n')

if remote_connection == "yes":
  mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_2_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_2_project_group_"+group_number
)
else:
  mydb = mysql.connector.connect(
    host="groucho.it.uu.se",
    user="ht21_2_group_"+group_number,
    passwd="pwd_"+group_number,
    database="ht21_2_project_group_"+group_number
  )


mycursor = mydb.cursor()

department = input('Department: ')
mycursor.execute(f"SELECT Title_of_department FROM Department WHERE Parent_dep="{department}"')
myresult = mycursor.fetchall()
if len(mycursor.fetchall()) < 1:
    mycursor.execute(f'' SELECT Title_of_product, Retail_price_without_tax*(1+Tax/100)*(1-Discount/100) FROM Product WHERE Product.Title_of_department={department}'")
    myresult = mycursor.fetchall()
    print(f'Title_of_department \t Retail price (w. discount)')
    for x in myresult:
        print(f"x[0] \t x[1]")
else:
    print('Child departments')
    for x in myresult:
        print(F"x[0]")

mydb.close()




if (SQLCODE == 0):
  if len(mycursor.fetchall()) < 1:
    mycursor.execute(f'' SELECT Title_of_product, Retail_price_without_tax*(1+Tax/100)*(1-Discount/100) FROM Product WHERE Product.Title_of_department={department}'')
    myresult = mycursor.fetchall()
    print(f'Title_of_department \t Retail price (w. discount)')
    for x in myresult:
        print(f"x[0] \t x[1]")
  else:
      print('Child departments')
      for x in myresult:
          print(F"x[0]")
else:
  print(f' error')