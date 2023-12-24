def createbilltable():                                                                                                       #creates table  bill in sql
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    mycursor=mydb.cursor()
    
    mycursor.execute("create table bill (Item_name char(40), Quantity int, Price int)")

    
    

def finalbill():                                                                                                             #adds item to the bill table
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    mycursor=mydb.cursor()
    
    itemid=input("Enter the ID of item you want to buy: ")
    qty=int(input("Enter quantity: "))
    mycursor.execute("select * from menu where itemcode='%s'"%(itemid))
        
        

    for i in mycursor:
        itemcode,category,item,price=i
        p=price
        print("__________________________________________________________________")
        print("Item name:      ", item)
               
        print("Price per item: ", price)
        print("")
        print("✔✔✔✔✔✔✔✔✔✔    Item added to your cart   ✔✔✔✔✔✔✔✔✔✔✔")
        print("▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨")
        s1="INSERT INTO bill VALUES (%s,%s,%s)"
        rate=qty*p           
        values=(item, qty, rate)
        mycursor.execute(s1,values)
        
        
    
        print("\nPlease answer the below question to confirm you are an human")
        day=input("Enter the day today:")
        val=(day,rate)
        s2="INSERT INTO crecord VALUES (%s,%s)"            
        mycursor.execute(s2,val)

        mydb.commit()
        

    
        


def generatebill():                                                                                                   #prints the bill and enters customer record in csv
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    
    print("")
    print("▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨▨")
    print("___________________________Generating Your BILL______________________________")
    print("")
    print("")
    
    print("-----------------------------------------------------------------------------")
    print("")

   
    print("-----------------------------------------------------------------------------")
    print("")
    print("                             YOUR   BILL                                     ")
    print("")
                    
    mycursor=mydb.cursor()
    mycursor.execute("Select * from bill")
    data=mycursor.fetchall()
    headers=["Item_name","Quantity","Price"]
    if data:
        print(tabulate(data,headers,tablefmt="fancy_grid"))
    else:
        print("An Error occured, Try later")
                   
        print("-----------------------------------------------------------------------------")
            
        print("-----------------------------------------------------------------------------")
        print("")
    mycursor.execute("select sum(price) from bill")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("")
    print("  Your Grand Total is:  $", end="")
    for i in mycursor:
        bill=i[0]
        print("  ",  bill)
        print("")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("")
        print("")
        print("")
        
        





        

def clearbill():                                                                                           #clears the bill table
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    mycursor=mydb.cursor()
    
    mycursor.execute("drop table bill")
    mydb.commit()


    

