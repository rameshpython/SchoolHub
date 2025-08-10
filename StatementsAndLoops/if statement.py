#if statement Conditions :
#program for accepting Three Numerical values and Find Bigest
#Conditional statements
#if statement
#moviee.py
tkt=input("Do u have Ticket(yes/no):")
if(tkt.lower()=="yes"):
    print("\tenter into theater")
    print("\twatch the movee")
    print("\tenjoy and Understand the message")
print("Goto Home--Read python Notes")

#Q.program for accepting Three Numerical values and Find Bigest
#SimpleIfStmtEx2.py
a=float(input("Enter value of a :"))
b=float(input("Enter value of b :"))
if(a>b):
    print("Big({},{})={}".format(a,b,a))
if(b>a):
    print("Big({},{})={}".format(a,b,b))
if(a==b):
    print("Both values are equal")
    print("program Execution completed")

#Q.program for accepting Three Numerical values and Find Bigest
#SimpleIfStmtEx2.py
a=float(input("Enter value of a :"))
b=float(input("Enter value of b :"))
c=float(input("Enter value of c :"))
if(a<=b)and(a>c):
    print("Max({},{},{})={}".format(a,b,c,a))
if(b>a)and(b>=c):
    print("Max({},{},{})={}".format(a,b,c,b))
if(c>=a) and (c>b):
    print("Max({},{},{})={}".format(a,b,c,c))
if(a==b) and (b==c) and (c==a):
    print("All values are equal")


#Q.#program for accepting Three Numerical values and Find Bigest
#SimpleIfStmtEx3.py
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
c=float(input("Enter value of c:"))
if(b<=a>c):
    print("Max({},{},{})={}".format(a,b,c,a))
if(a<b>=c):
    print("Max({},{},{})={}".formaat(a,b,c,b))
if(a<=c>b):
    print("Max({},{},{})={}".format(a,b,c,))
if(a==b==c):
    print("All values are equal")

#Q.program for accepting a Numerical value
#SimpleIfStmtEx4.py
a=float(input("Enter Value of a:")) 
if(a==0):
    print("{} is Zero".format(a))
if(a>0):
    print("{} is +VE".format(a))
if(a<0):
    print("{} is -VE".format(a))

#Q.Program for Calculating Simple Interest
# provided all values (p,t,r) values are +Ve
#otherwise Corresponding Error Messages
p=float(input("Enter Principle Amount:"))
t=float(input("Enter Time:"))
r=float(input("Enter Rate of Interest:"))
if(p>0) and (t>0) and (r>0):
    si=(p*t*r)/100
    totamt=p+si
    print("-"*50)
    print("\tPrinciple Amount:{}".format(p))
    print("\tTime:{}".format(t))
    print("\tRate of Interest:{}".format(r))
    print("\tSimple interest:{}".format(si))
    print("\tTotal Amount to Pay:{}".format(totamt))
    print("-" * 50)
if(p<=0):
    print("\tprinciple Amount :{} is Invalid".format(p))
if(t<=0):
    print("\tTime :{} is Invalid".format(t))
if(r<=0):
    print("\tRate of Interest :{} is Invalid".format(r))    
    

