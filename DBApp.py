import mysql.connector

group_number= "15" #FILL IN YOUR GROUP NUMBER

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_2_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_2_project_group_"+group_number
)

mycursor = mydb.cursor()

product = input('Product: ')
mycursor.execute(f'SELECT Title_of_product FROM Product')
myresult = mycursor.fetchall()
prods = [x[0] for x in myresult]
while product not in prods:
  print(f'Product {product} does not exist')
  product = input("Please give another product: ")

mycursor.execute(f'SELECT Discount FROM Product WHERE Title_of_product="{product}"')
myresult = mycursor.fetchall()

print(f'Current discount: {myresult[0][0]}')
answer = input('Change discount (Yes/No)? ')
if answer=='Yes':
    new_disc=float(input('New discount (in percentage without %): '))
    mycursor.execute(f'UPDATE Product SET discount={new_disc} WHERE Title_of_product="{product}"')
    mydb.commit()

    mycursor.execute(f'SELECT Discount FROM Product WHERE Title_of_product="{product}"')
    myresult = mycursor.fetchall()
    print(f'Discount changed to {myresult[0][0]} %')

else: 
    print('Discount not changed.')

mydb.close()