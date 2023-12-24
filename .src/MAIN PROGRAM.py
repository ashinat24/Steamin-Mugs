import os
import sys
from easygui import passwordbox
password=passwordbox("Enter password: ")
if password=="smugs":
                                                                                                                             
    print("\n\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    print("")
    name=input("Enter your name: ")
    print("")
    N=name.title()
    
    print("-------------------------->>>>>>>>>>>>><<<<<<<<<<----------------------------")

    print("-------------------------->>>>>>>>>>>>><<<<<<<<<<----------------------------\n")
    print("                                 HI!",N,"                                    ")
    print("-------------------------->>>>>>>>>>>>><<<<<<<<<<----------------------------")

    print("-------------------------->>>>>>>>>>>>><<<<<<<<<<----------------------------\n")
    print("Are you a customer or an employee: ")
    print("ENTER 1 FOR CUSTOMER OR 2 FOR EMPLOYEE OR ENTER ANY OTHER NUMBER TO EXIT\n")
    c1=int(input())
    print('''                                        ⌈                                       ⌉
                                              Welcome to STEAMIN' MUGS  ✿◡‿◡  
                                        ⌊                                       ⌋  ''')
    if c1==2:
        import os
        import sys
        from easygui import passwordbox

        print("\nHello valued worker Enter the password\n\n\n")
        password=passwordbox("Enter password: ")
        if password=="rvtp":
            import retailer
            retailer.retailer_tasks()
        else:
            print("!!!!!!  WRONG PASSWORD   !!!!!!!")
        print("\n\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")

    elif c1==1:    
        while True:
            print("")
            print("")
            if c1==1:            
                print("DISPLAYING THE MENU  ")
                f1=open("MENUFILE1.txt","r")
                menu=f1.read()
                print(menu)
                print('''What would you like to eat? \^o^/
Please enter only index numbers''')                                                                                        
                c2=input()
                
                import Cfunc as F
                import billing as B
                F.choose(c2)
                
                if c2 not in '123456789':
                    break
                B.createbilltable()
                B.finalbill()
                print("")
                print("")
                while True:
                    ch=input("DO YOU WANT TO ADD MORE ITEMS?(y/n): ")
                    if ch in 'yY':
                        print("1. From same category")
                        print("2.From a different category")
                        choice=int(input())
                        if choice==1:
                            B.finalbill()
                        else:
                            print(menu)
                            c3=input('Enter the number of the food category:')
                            if c3 in '123456789':
                                F.choose(c3)
                                B.finalbill()
                                
                            else:
                                F.choose(c3)
                                B.generatebill()
                                opt=input("\n Do you have an internet connection(y/n): ")
                                if opt in 'Yy':
                                    F.cdetails_n_mailon(N)
                                else:
                                    F.cdetails_n_mailoff(N)
                                    
                                B.clearbill()
                                break
                    else:
                        B.generatebill()
                        opt=input("\n Do you have an internet connection(y/n): ")
                        if opt in 'Yy':
                            F.cdetails_n_mailon(N)
                        else:
                            F.cdetails_n_mailoff(N)
                        B.clearbill()
                        break
    
        print("\n\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
                                                                                                        


    else:
        print("\n\n☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆☆")
    

    
else:
    print("******************************** Wrong password  *********************************\n")
    print("********************************  ACCESS DENIED  ********************************")
                            
                 
                   
                
                    
                            
                
                

                
        
                    

                    
                    
                    

                    


        

                

                    

                    
                    
                
                
        
            
