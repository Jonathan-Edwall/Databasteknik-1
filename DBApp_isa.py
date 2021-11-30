import mysql.connector

group_number="15" #FILL IN YOUR GROUP NUMBER

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_2_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_2_project_group_"+group_number
)

mycursor = mydb.cursor()

department = input('Department: ')
mycursor.execute(f'SELECT Title_of_department FROM Department')
myresult = mycursor.fetchall()
deps = [x[0] for x in myresult]
print(deps)
while department not in deps:
  print(f'Department {department} does not exist')
  department = input("Please give another department: ")


mycursor.execute(f'SELECT Title_of_department FROM Department WHERE Parent_dep="{department}"')
myresult = mycursor.fetchall()
if len(myresult) < 1:
    mycursor.execute(f'SELECT Title_of_product, Retail_price_without_tax*(1+Tax/100)*(1-Discount/100) FROM Product WHERE Product.Title_of_department="{department}"')
    myresult = mycursor.fetchall()
    print(f'Title_of_department \t Retail price (w. discount)')
    for x in myresult:
        print(f"{x[0]} \t {x[1]}")
else:
    print('Child departments')
    for x in myresult:
        print(f"{x[0]}")

mydb.close()
