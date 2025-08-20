#Inner loops
#Examples
#InnerLoopEx-1
for i in range (1,6):
    print("outer loop--value of i={}".format(i))
    for j in range(1,5):
        print("\tInner loop--value of j={}".format(j))
    else:
        print("\tIam else part of inner loop")
else:
    print("I am from else part of outer loop")

print("------------------------------------------------------")
    
#InnerLoopEx-2
i=5
while(i>=1):#outer Loop
    print("outer loop--value of i={}".format(i))
    j=4
    while(j>=1):#Inner Loop
        print("\tInner loop--value of j={}".format(j))
        j=j-1
    else:
        i=i-1
        print("\tIam from else part of inner loop")
else:
    print("i am from else part of outer loop")

print("------------------------------------------------------")


#InnerLoopEx-3
i=1
while(i<=5):#outer loop
    print("outer loop--value of i={}".format(i))
    for j in range(4,0,-2):#inner loop
        print("\touter loop--value of j={}".format(j))
    else:
        i=i+1
        print("\tIam from else part of inner loop")
else:
    print("Iam from else  part of outer loop")

print("-------------------------------------------------------")

#InnerLoopEx-4
for i in range(7,0,-2):#outer loop
    print("outer loop--value of i={}".format(i))
    j=1
    while(j<=1):#inner loop
        print("\tinner loop--value of j={}".format(j))
        j=j+1
    else:
        print("\tIam from else part of inner loop")
else:
    print("iam from else part of outer loop")

print("-------------------------------------------------------")

#InnerLoopEx-5
n=int(input("Enter How Many Mul Tables u want:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    for num in range(1,n+1): # outer loop
        print("Mul Table for:{}".format(num))
        for i in range(1,11): # inner loop--Display Mul Table
            print("\t{} x {} = {}".format(num,i,num*i))
        else:
            print("-"*50)

print("-------------------------------------------------")

#InnerLoopEx-6
n=int(input("Enter How Many Values Mul Tables u Want:"))
if(n<=0):
    print("\t{} is invalid Input".format(n))
else:
    lst=[] #empty list-for adding values
    for i in range(1,n+1):
        value=int(input("Enter {} Value:".format(i)))
        lst.append(value)
    else:
        print("Content of List")
        print(lst) 
        #Mul Code for random Numbers
        for num in lst: # outer loop
            if(num<=0):
                print("\t{} is Invalid Input".format(num))
            else:
                print("Mul Table for :{}".format(num))
                for i in range(1,11): # inner loop
                    print("\t{} x {}={}".format(num,i,num*i))
                else:
                    print("-" * 50)

print("-------------------------------------------------------")

#InnerLoopEx-7
ranval=int(input("Enter the Range Value in which u want primes:")) # 10
if(ranval<=1):
    print("\t{} is Invalid ".format(ranval))
else:
    print("-"*40)
    print("List of Primes within:{}".format(ranval))
    print("-" * 40)
    for num in range(2,ranval+1): # Supply the Value--outer
        res=True
        for i in range(2,num): # inner loop
            if(num%i==0):
                res=False
                break
        if(res):
            print("\t{}".format(num))
    print("-" * 40)



    

