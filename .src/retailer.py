def retailer_tasks():
    print("----------------------------------------------------------------------------------------------\n\n----------------------------------------------------------------------------------------------\n")
    f=open("retailer.txt","r")
    import mysql.connector
    from tabulate import tabulate
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    mycursor=mydb.cursor()
    
    print(f.read())
            
    print("") 
    ch1=int(input("What changes are you planning to make : "))
            
    while ch1 in [1,2,3,4,5,6,7,8]:
        if ch1==1:
            f=open("update.txt","r")                                                                                    #update
            print(f.read())
                    
            ch=int(input("What do you want to update : "))
            while ch in [1,2,3,4]:
                if ch==1:
                    itemcode=input("Enter item code: ")
                    print("")
                    newprice=input("Re-enter price: ")
                    print("")
                    mycursor.execute("update menu set price='%s' where itemcode='%s'"%(newprice,itemcode))
                          
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    print('')
                    print("******************************  PRICE UPDATED  ********************************")
                    print("")   
                    mydb.commit()
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    break
                elif ch==2:
                    
                    itemcode=input("Enter item code: ")
                    print("")
                    newcategory=input("Re-enter category: ")
                    print("")
                    mycursor.execute("update menu set category='%s' where itemcode='%s'"%(newcategory,itemcode))
                          
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    print('')
                    print("****************************  CATEGORY UPDATED  ******************************")
                    print("")   
                    mydb.commit()
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    break
                elif ch==3:
                    itemcode=input("Enter item code: ")
                    print("")
                    newitemname=input("Re-enter item name: ")
                    print("")
                    mycursor.execute("update menu set item='%s' where itemcode='%s'"%(newitemname,itemcode))
                          
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    print('')
                    print("*******************************  ITEM UPDATED  *********************************")
                    print("")   
                    mydb.commit()
                    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    break
                elif ch==4:
                    itemcode=input("Enter item code: ")
                    print("")
                    newitemcode=input("Re-enter item code: ")
                    print("")
                    mycursor.execute("update menu set itemcode='%s' where itemcode='%s'"%(newitemcode,itemcode))
                          
                    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    print('')
                    print("*****************************  ITEMCODE UPDATED  *******************************")
                    print("")   
                    mydb.commit()
                    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                    break
                else:
                    break
            break
        elif ch1==3:                                                                                                 #itemdeletion
            
            itemcode=input("Enter item code to be deleted: ")
            print("")
            mycursor.execute("delete from menu where itemcode='%s'"%(itemcode))
      
                        
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            print('')
            print("*******************************  ITEMCODE DELETED ********************************")
            
            print("")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            mydb.commit()
            break

        elif ch1==2:
            print("Enter item details to be inserted: ")                                                                 #iteminsertion
            print("")
            print("*******************************************************************************\n")
            itemcode=input("Enter item code: ")
            category=input("Enter category: ")
            name=input("Enter itemname: ")
            price=input("Enter price: ")
            mycursor.execute("insert into menu values ('%s','%s','%s','%s')"%(itemcode,category,name,price))
                       
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            print('')
            print("******************************** ITEM INSERTED *******************************")
            print("")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            mydb.commit()
            break
        elif ch1==4:                                                                                                    #display customer records
            
            print("")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            print('')
            print("************************ DISPLAYING CUSTOMER RECORDS *****************************")
            print("")
            print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
            
            import csv
            with open ("Crecord.csv", "r") as k:
                
                    csv_w=csv.reader(k)
                    for i in csv_w:
                        
                            print(i)
            break


        
        elif ch1==5:                                                                                       #sending emails
            import csv
            listrecord=[]
            
            
            while True:
                print("Whom you want to send the mail: ")
                print("1. Customer")
                print("2. Co-worker")
                print('3. Exit\n\n')
                
                ch=int(input())
                if ch==1:
                    with open("Crecord.csv","r") as k:                                                     # to customer
                        csv_w=csv.reader(k)
                        for i in csv_w:
                            if csv_w.line_num==1:
                                continue
                            print(i)
                            listrecord.append(i)
                        print('''---------------------------------------------------------------------------------------------------------------
\n Email to be sent to:

1. ALL THE CUSTOMERS
2. TO A FINITE NUMBER OF CUSTOMERS

---------------------------------------------------------------------------------------------------------------

''')
                        ch2=int(input())
                        if ch2==1:
                            sub=input("Enter subject: ")
                            print("")
                            str=input("Enter the message to be sent: ")
                            print("")
                            for j in listrecord:
                                
                                
                                email=j[5]
                                rmail(email,sub,str)
                        else:
                            sub=input("Enter subject: ")
                            print("")
                            str=input("Enter the message to be sent: ")
                            print("")
                            l_id=[]
                            while True:
                                c_id=input("Enter CUSTOMER ID of the recipient: ")
                                l_id.append(c_id)
                                choice=input("Do you want to enter more CUSTOMER ID's:(y/n): ")
                                if choice in 'nN':                                    
                                    for i in l_id:
                                        for j in listrecord:
                                            if j[0]==i:
                                                email=j[5]
                                                rmail(email,sub,str)
                                                break
                                if choice in 'yY':
                                    continue
                                break
                                
                        
                                                                                                                   # to employee
                elif ch==2:
                     with open("Erecord.csv","r") as k:
                        csv_w=csv.reader(k)
                        for i in csv_w:
                            if csv_w.line_num==1:
                                continue
                            print(i)
                            listrecord.append(i)
                        print('''---------------------------------------------------------------------------------------------------------------\n
Email to be sent to:

1. ALL THE EMPLOYEES
2. TO A FINITE NUMBER OF EMPLOYEES

---------------------------------------------------------------------------------------------------------------

''')
                        ch2=int(input())
                        if ch2==1:
                            sub=input("Enter subject: ")
                            print("")
                            str1=input("Enter the message to be sent: ")
                            print("")
                            for j in listrecord:
                                if j[5] !="NA":
                                    
                                    email=j[5]
                                    rmail(email,sub,str1)
                        else:
                            sub=input("Enter subject: ")
                            print("")
                            str=input("Enter the message to be sent: ")
                            print("")
                            l_id=[]
                            while True:
                                c_id=input("Enter EMPLOYEE ID of the recipient: ")
                                l_id.append(c_id)
                                
                                choice=input("Do you want to enter more EMPLOYEE ID's:(y/n): ")
            
                                if choice in 'nN':
                                    for i in l_id:
                                        if i not in "naNA":
                                            for j in listrecord:
                                                if j[0]==i:
                                                    email=j[5]
                                                    rmail(email,sub,str)
                                                    break
                                            
                                if choice in 'yY':
                                    continue
                                break   
                                            
                                
                else:
                    break
            break
                
                    
        elif ch1==6:                                                               #UPDATING EMP RECORDS
            import csv
            import random
            from easygui import passwordbox
            agree=input("Are you the HEAD EMPLOYEE:(y/n) ")
            if agree in "Yy":
                password=passwordbox("Enter password: ")
                if password=="rvtp001":
                    while True:
                        print('\n--------------------------------------------------------------------------------------------------------\n')
                        print("1. ADD RECORDS TO EMPLOYEE FILE")
                        print("2. DELETE RECORDS FROM EMPLOYEE FILE")
                        print("3. UPDATE EXISTING RECORDS")
                        print("4. EXIT")
                        print('\n--------------------------------------------------------------------------------------------------------\n')

                        ch1=int(input("Enter your choice: "))
                        print("")
                        print("")
                        if ch1==4:
                            break
                        elif ch1==1:
                            while True:
                                with open ("Erecord.csv","a") as f:
                                    csvw=csv.writer(f)
                                    empname=input("Enter new employee's name: ")
                                    empadd=input("Enter new employee's address: ")
                                    empph=input("Enter new employee's phone number: ")
                                    empage=input("Enter new employee's age: ")
                                    empmail=input("Enter new employee's email address: ")
                                    empsal=input("Enter new employee's salary: ")
                                    emprec=[random.randrange(1000,9000),empname,empadd,empph,empage,empmail,empsal]
                                    csvw.writerow(emprec)
                                    print("")
                                    print("")
                                    choice=input("Do you want to add more records:(y/n): ")
                                
                                    if choice in 'nN':
                                            
                                        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                                        print('')
                                        print("******************************* RECORD ENTERED ************************************")
                                        print("")
                                        print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                                    break
                        elif ch1==2:
                            listrec=[]
                            with open ("Erecord.csv","r") as f:
                                csvr=csv.reader(f)
                                for i in csvr:
                                    listrec.append(i)
                                    print(i)
                                    
                            while True:
                                delrec= input("Enter Employee ID of the record you want to delete:")
                                for i in listrec:
                                    for j in i:
                                        if j==delrec:
                                            listrec.remove(i)
                                with open("Erecord.csv","w") as f:
                                    csvw=csv.writer(f)
                                    for j in listrec:
                                        csvw.writerow(j)
                                choice=input("Do you want to delete anymore records:(y/n) ")
                                if choice in 'nN':
                                    
                                    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                                    print('')
                                    print("******************************* RECORD DELETED ************************************")
                                    print("")
                                    print(":::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n")
                                    break

                                
                        elif ch1==3:
                            while True:
                                print('\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n')
                                print("1. UPDATE ADDRESS")
                                print("2. UPDATE PHONE NUMBER")
                                print("3. SALARY")
                                print("4. EXIT")
                                print('\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||n')
                                ch2=int(input("Enter your choice: "))
                                listrec=[]
                                if ch2 in[1,2,3]:
                                    with open ("Erecord.csv","r") as f:
                                        csvr=csv.reader(f)
                                        for i in csvr:
                                            listrec.append(i)
                                            print(i)
                                if ch2==1:
                                    while True:
                                        empid= input("Enter Employee ID of the record you want to change the address for:")
                                        newadd=input("Enter new address: ")
                                        for i in range (len(listrec)):
                                            if listrec[i][0]==empid:
                                                listrec[i][2]=newadd
                                            
                                        with open("Erecord.csv","w") as f:
                                            csvw=csv.writer(f)
                                            for i in listrec:
                                                csvw.writerow(i)
                                        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
                                        print("**********************  CHANGE IMPLEMENTED  **********************************\n")
                                        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
                                        choice=input("Do you want to update address for anymore records:(y/n) ")
                                        if choice in 'nN':
                                            break

                                elif ch2==2:
                                    while True:
                                        empid= input("Enter Employee ID of the record you want to change the phone number for:")
                                        newph=input("Enter new phone number: ")
                                        for i in listrec:
                                            if i[0]==empid:
                                                i[3]=newph
                                            
                                        with open("Erecord.csv","w") as f:
                                            csvw=csv.writer(f)
                                            for i in listrec:
                                                csvw.writerow(i)
                                        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
                                        print("**********************  CHANGE IMPLEMENTED  **********************************\n")
                                        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
                                        choice=input("Do you want to update phone number for anymore records:(y/n) ")
                                        if choice in 'nN':
                                            break
                                elif ch2==3:
                                    while True:
                                        empid= input("Enter Employee ID of the record you want to change the salary for:")
                                        inc=int(input("Enter the increament in salary: "))
                                        for i in listrec:
                                            if i[0]==empid:
                                                i[6]=int(i[6])+inc
                                    
                                            
                                        with open("Erecord.csv","w") as f:
                                            csvw=csv.writer(f)
                                            for i in listrec:
                                                csvw.writerow(i)

                                        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
                                        print("**********************  CHANGE IMPLEMENTED  **********************************\n")
                                        print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
                                        choice=input("Do you want to update salary for anymore records:(y/n) ")
                                        if choice in 'nN':
                                            break
                                elif  ch2==4:
                                    break
                            break
                
                else:
                    print("!!!!!!!!   INVALID PASSWORD   !!!!!!")
            else:
                print("\n---------------------------------------------------------------------------------------------\nSORRY! YOU DON'T HAVE ACCESS TO THIS FACILITY\n")
                print("---------------------------------------------------------------------------------------------\n")
                                    
                                  
            break
            
        elif ch1==8:
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
            print("**********************************  EXITING  *************************************\n")
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
            break
        elif ch1==7:
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n\n')
            print("**********************************  DISPLAYING GRAPH  *************************************\n")
            print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
            import graph
            graph.graph()
            break
                
                
                

        else:
            
           print("NOT A VALID CHOICE!!!!")
       




           

def rmail(mail,sub,msgfromretailer):
    import smtplib
    import csv

    subject = sub
    msg = msgfromretailer
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login("steaminmugscs@gmail.com", "rvtp324612")
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail("steaminmugscs@gmail.com",mail, message)
    server.quit()
    print("\n::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("\n\n")
    print("***************************  EMAIL SENT!  **********************************")
    print("")
    print("")
    print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::")
    print("")
    print("")




                   
                  


        
