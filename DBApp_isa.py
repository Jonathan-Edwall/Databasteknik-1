import mysql.connector

group_number="15" #FILL IN YOUR GROUP NUMBER

mydb = mysql.connector.connect(
  host="127.0.0.1",
  user="ht21_2_group_"+group_number,
  passwd="pwd_"+group_number,
  database="ht21_2_hotels_group_"+group_number
)

mycursor = mydb.cursor()

department = input('Department: ')
mycursor.execute("SELECT Title_of_department FROM Department WHERE Parent_dep={department}")
myresult = mycursor.fetchall()
if len(mycursor.fetchall()) < 1:
    mycursor.execute("SELECT Title_of_product, Retail_price_without_tax*(1+Tax/100)*(1-Discount/100) FROM Product WHERE Product.Title_of_department={department}")
    myresult = mycursor.fetchall()
    print(f'Title_of_department \t Retail price (w. discount)')
    for x in myresult:
        print(f"x[0] \t x[1]")
else:
    print('Child departments')
    for x in myresult:
        print(F"x[0]")

mydb.close()

###############################################
#import mysql.connector

#group_number="15" #FILL IN YOUR GROUP NUMBER

#mydb = mysql.connector.connect(
  #host="127.0.0.1",
  #user="ht21_2_group_"+group_number,
  #passwd="pwd_"+group_number,
  #database="ht21_2_hotels_group_"+group_number
#)

#mycursor = mydb.cursor()

#product = input('Product: ')
#mycursor.execute("SELECT Discount FROM Product WHERE Title_of_product={product}")
#myresult = mycursor.fetchone()

#print(f'Current discount: {myresult[0]}')
#answer = input('Change discount (Yes/No)? ')
#if answer=='Yes':
    #new_disc=float(input('New discount (in percentage without %): '))
    #mycursor.execute("UPDATE Product SET discount={new_disc} WHERE Title_of_product={product}")
    #mydb.commit()

    #mycursor.execute("SELECT Discount FROM Product WHERE Title_of_product={product}")
    #myresult = mycursor.fetchone()
    #print('Discount changed to' + str(myresult[0]) + '%')

#else: 
    #print('Discount not changed.')

#mydb.close()