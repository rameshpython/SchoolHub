#While loops
#To print numbers from 1 to 10 by using while loop
x=1
while x<=10:
    print(x)
    x=x+1

#To display the sum of first n numbers

n=int(input("Enter number:"))
sum=0
i=1
while i<=n:
    sum=sum+i
    i=i+1
    print("The sum of first ",n,"numbers is:",sum)

#Write a program to prompt user to enter some name until entering ramss
name=""
while name!="ramss":
    name=input("Enter name:")
print("Thanks for confirmation")

#infinite loop
#i=0
#while True:
#    i=i+1
#    print("hello hii",i)

   # OR

#x=1
#while x>=1:
#    print("helloworld")
#    x=x+1
    
#program for generating 1 to N where N is +Ve
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("Numbers within:{}".format(n))
    print("-" * 50)
    i=1  # Initlization Part
    while(i<=n):  # Test Cond
        print("\t{}".format(i))
        i+=1 # OR i=i+1  ---Updation Part
    else:
        print("-"*50)
    print("Program execution Completed")

#program for generating  N  to 1 where N is +Ve
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("Numbers from {} to {}".format(n,1))
    print("*" * 50)
    i=n # Initlization part
    while(i>=1):#test code
        print("\t{}".format(i))
        i-=1 # OR i=i-1
    else:
        print("program is executed")

#program for generating  N  to 1 where N is +Ve
n=int(input("Enter How Many Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("Numbers from {} to {}".format(n,1))
    print("*" * 50)
    while(n>=1):
        print("\t{}".format(n))
        n-=1 # OR n=n-1
    else:
        print("program executed")

#program for generating all even numbers within in N
n=int(input("Enter How Many Even Number u want to generate:"))
if(n<=0):
    print("{} is invalid input".format(n))
else:
    print("Even numbers within :{}".format(n))
    i=1
    while(i<=1):
        if(i%2==0):
            print("{}".format(i))
        i=i+1
    else:
        print("program executed")

#program for generating all even numbers within in N
n=int(input("Enter How Many Even Number u want to generate:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("Even Numbers within :{}".format(n))
    i=2
    while(i<=n):
        print("\t{}".format(i))
        i+=2#OR i=i+2
    else:
        print("program executed")

#Program for generating Mul Table for a Given +Ve Numbers
n=int(input("Enter a Number for generating Mul Table:"))
if(n<=0):
    print("{} is Invalid Input".format(n))
else:
    print("Mul Table for {}".format(n))
    i=1
    while(i<=10):
        print("\t{} x {} = {}".format(n,i,n*i))
        i=i+1
    else:
        print("program executed")




