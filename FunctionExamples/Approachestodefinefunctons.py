#calculating sum of two numbers
#Approach-1
def sumop(a,b):
    c=a+b
    return c
print("type of sumop=",type(sumop))
res=sumop(a=100,b=200)
print("sum=",res)
k=float(input("Enter first value:"))
v=float(input("Enter second value:"))
res=sumop(k,v)#function call
print("sum=",res)
print("sum({}+{}={}".format(k,v,res))

print("----------------------------------------")

#Approach-2
def sumop():
    a=float(input("Enter first value:"))
    b=float(input("Enter second value:"))
    #process
    c=a+b
    print("sum({},{})={}".format(a,b,c))

print("Iam from main program")
sumop() #fuction call

print("------------------------------------------")
#Approach-3
def sumop(k,v):
    r=k+v
    print("sum({},{})={}".format(k,v,r))

#main program
G=float(input("Enter firstalue:"))
R=float(input("Enter second value:"))
sumop(G,R) #function call

print("-------------------------------------------")
#Approach-4
def sum( ):
    a=float(input("Enter first value:"))
    b=float(input("Enter second value:"))
    #proccess
    c=a+b
    return a,b,c
#main program
res=sumop(10,20) #function call
print("sum=",res)
#print("sum={}".format(res))





