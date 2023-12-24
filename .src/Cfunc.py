
def choose(num):
    num=str(num)                                                                                                         #displays choices in menu
    if num=='1':
        f1=open("COFFEENBEV.txt")
        print("                                                          ▶▶▶▶▶  COFFEE AND BEVERAGES  ◀◀◀◀◀")
        print(f1.read())
    elif num=='2':
        f1=open("NONCOFFEE.txt")
        print("                                                          ▶▶▶▶▶  NON COFFEE DRINKS  ◀◀◀◀◀")
        print(f1.read())
    elif num=='3':
        f1=open("PIZZA.txt")
        print("                                                               ▶▶▶▶▶  PIZZA   ◀◀◀◀◀")
        print(f1.read())
    elif num=='4':
        f1=open("SANDWICH.txt")
        print("                                                              ▶▶▶▶▶  SANDWICHES   ◀◀◀◀◀")
        print(f1.read())
    elif num=='5':
        f1=open("SOUPS.txt")
        print("                                                                ▶▶▶▶▶  SOUPS   ◀◀◀◀◀")
        print(f1.read())
    elif num=='6':
        f1=open("BURGER.txt")
        print("                                                                   ▶▶▶▶▶  BURGERS  ◀◀◀◀◀")
        print(f1.read())
    elif num=='7':
        f1=open("CHINESE.txt")
        print(f1.read())
    elif num=='8':
        f1=open("PASTRIES.txt")
        print("                                                                    ▶▶▶▶▶  PASTRIES  ◀◀◀◀◀")
        print(f1.read())
    elif num=='9':
        f1=open("KARNATAKA SPECIAL.txt")
        print("                                                               ▶▶▶▶▶  KARNATAKA SPECIAL   ◀◀◀◀◀")
        print(f1.read())
    else:
        service=eval(input("PLEASE RATE OUR SERVICE OUT OF 5: "))
        print("")
        print("---------------------------------    !!THANKYOU!!    -------------------------------------")
        print("")






 

def cdetails_n_mailon(cname):
    import random
                                                                                                                  #entering customer details         
                
    print("Please enter the following details")
    print("")
    print("")
                    
    add=input("Enter your address: ")
    print("")
    phone=int(input("Enter your phone no.: "))
    print("")
    age=int(input("Enter your age: "))
    print("")
    mail=input("Enter your e-mail address: ")
    print("")
    print("")
    print("")
    print("Choose a payment method")
    print("1.PayPal")
    print("2.GooglePay")
    print("3.Credit Card")
    print("4.MoonDelicacy Debit Card")
    payment_mode=int(input("Enter your choice: "))
    print("")
    print("------------------------------------------------------------------------------")
    print("")
    print("")
    import mysql.connector
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    mycursor=mydb.cursor()
    mycursor.execute("select sum(price) from bill")
    for i in mycursor:
        bill=i[0]
        with open("mailcontent.txt","w")as f2:
            f2.write("Hello, " )
            f2.write(cname+" your order from STEAMIN' MUGS worth $")
            f2.write(str(bill)+" has been accepted and will be delivered to you in "+str(random.randint(25,40))+" mins. \nHOPE YOU HAVE A GREAT TIME EATING ^_~\nTHANK YOU FOR VISITING!!!")

    import smtplib
    import csv
    
    confirmcode=random.randrange(2000,9000)
    subject = "ORDER CONFIRMATION MESSAGE"
    msg = "Your Order Confirmation code is "+str(confirmcode)
    
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login("steaminmugscs@gmail.com", "zutd mtru djgy jhog")
    message = 'Subject: {}\n\n{}'.format(subject, msg)
    server.sendmail("steaminmugscs@gmail.com",mail, message)
    server.quit()
    print("ORDER CONFIRMATION CODE SENT TO YOUR MAIL!")
    print("")
    print("")
    print("------------------------------------------------------------------------------")
    print("")
    print("")
    

        
    chances=0
    while chances<3:
        code=int(input("Enter the Order Confirmation Code sent to your e-mail account: "))
        if code==confirmcode:
            import mysql.connector
            from tabulate import tabulate
            mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
            mycursor=mydb.cursor()
            mycursor.execute("select sum(price) from bill")
            for i in mycursor:
                bill=i[0]
                                                                                                                       #order confirmation
                subject = "ORDER CONFIRMED!"
                with open("mailcontent.txt","r") as file:
                    msg1=file.readline()
                    msg2=file.readline()
                    msg3=file.readline()
                    mesg=msg1+msg2+msg3
                    
                try:
                
                    server = smtplib.SMTP('smtp.gmail.com:587')
                    server.ehlo()
                    server.starttls()
                    server.login("steaminmugscs@gmail.com", "rvtp324612")
                    message = 'Subject: {}\n\n{}'.format(subject, mesg)
                    server.sendmail("steaminmugscs@gmail.com",mail, message)
                    server.quit()
                    print("------------------------------------------------------------------------------ \n\n")
                    print("                                            !!!!WOHOOO!!!!\n\n\n★☆★☆★☆★☆★☆★☆★☆★☆   SUCCESS: Order confirmed by STEAMIN' MUGS!   ★☆★☆★☆★☆★☆★☆★☆ \n\n\n")
                    print("Email Sent to your email account!!!")
                    f1=open("valet.csv","r")
                    valetread=csv.reader(f1)
                    valetlist=[]                                                                                          #valet choosing
                    for rec in valetread:
                        valetlist.append(rec)
                    valet=random.choice(valetlist)
                    print("Your valet today is ", valet[0]," with ",valet[1]," and ",valet[2]," star ratings!!")

                                                                                                                          #entering record in csv
                    f3=open("Crecord.csv","a")
                    record=[random.randrange(1000,9000),cname,add,phone,age,mail,bill,valet[0]]
                    csvwrite=csv.writer(f3)
                    csvwrite.writerow(record)
                   
                except:
                    
                
                    print("We are really sorry for incovenience.\nBut there are no nearby valets available! :( \nMAYBE, TRY AGAIN AFTER SOMETIME! ಥ_ಥ")
            
            break        
        else:
            if chances==2:
                print("------------------------------------------------------------------------------\n\n")
            
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! \n")
                print("YOU EXCEEDED THE NUMBER OF GIVEN TRIALS\n\n Maybe, try again after sometime!\n")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            else:
                print("------------------------------------------------------------------------------\n\n")
                print("WRONG CODE ENTERED!!!!\n\n")
                print("Try again!\n\n\n")
                
        chances+=1
    
    print("")
    print("------------------------------------------------------------------------------")
    print("")
    print("")
    

        
def cdetails_n_mailoff(cname):
    import csv
    import random
    print("Please enter the following details")
    print("")
    print("")
                    
    add=input("Enter your address: ")
    print("")
    phone=int(input("Enter your phone no.: "))
    print("")
    age=int(input("Enter your age: "))
    print("")
    mail=input("Enter your e-mail address: ")
    print("")
    print("")
    print("")
    print("Choose a payment method")
    print("1.PayPal")
    print("2.GooglePay")
    print("3.Credit Card")
    print("4.MoonDelicacy Debit Card")
    payment_mode=int(input("Enter your choice: "))
    print("")
    print("------------------------------------------------------------------------------")
    print("")
    print("")
    print("\n\n\n\nENTER THE CODE DISPLAYED ON SCREEN : \n \n")
    print(random.randint(1000,9000))
    code=int(input())
    print("------------------------------------------------------------------------------ \n\n")
    print("                                            !!!!WOHOOO!!!!\n\n\n★☆★☆★☆★☆★☆★☆★☆★☆   SUCCESS: Order confirmed by STEAMIN' MUGS!   ★☆★☆★☆★☆★☆★☆★☆ \n\n\n")
    f1=open("valet.csv","r")
    valetread=csv.reader(f1)
    valetlist=[]                                                                                          #valet choosing
    for rec in valetread:
        valetlist.append(rec)
    valet=random.choice(valetlist)
    print("Your valet today is ", valet[0]," with ",valet[1]," and ",valet[2]," star ratings!!")
    import mysql.connector
    
    mydb=mysql.connector.connect(host="localhost",user="root",password="0000",database="rvtp")
    mycursor=mydb.cursor()
    mycursor.execute("select sum(price) from bill")
    for i in mycursor:
        bill=i[0]

                                                                                                                          #entering record in csv
        f3=open("Crecord.csv","a")
        record=[random.randrange(1000,9000),cname,add,phone,age,mail,bill,valet[0]]
        csvwrite=csv.writer(f3)
        csvwrite.writerow(record)


    print("")
    print("------------------------------------------------------------------------------")
    print("")
    print("")
    

cdetails_n_mailon("tanisha")
   

    
    
                
            

            
                
                
        
        
            
            
            
    
        
   
    
    
       
        
        

        


    



    




                                                                      

    
    
    
        

        

    
            
                    
                    



    

        
    
    
    



    
    
                    

                    
