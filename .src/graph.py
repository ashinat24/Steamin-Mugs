import mysql.connector
from tabulate import tabulate
import matplotlib.pyplot as plt
def graph():
    
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='monday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y11=int(i[0])  
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='tuesday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y12=int(i[0])  
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='wednesday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y13=int(i[0])  
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='thursday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y14=int(i[0])  
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='friday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y15=int(i[0])  
  
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='saturday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y16=int(i[0])  
    
    mydb=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="rvtp")
    mycursor=mydb.cursor()
    sql="select sum(bill) from crecord where day='sunday'"
    mycursor.execute(sql)
    y1=mycursor.fetchall()
    for i in y1:
      y17=int(i[0])  
    
    x=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
    y=[y11,y12,y13,y14,y15,y16,y17]
    print(y)
    plt.plot(x,y)
    plt.xlabel("days")
    plt.ylabel("sales")
    plt.title("sales analysis")
    plt.show()
    
graph()
