#iterative  statements (repeats again and again until a condition met or a result reached)
#For loops
s="Gaganam Ramesh"
for x in s:
    print(x)

#    OR
for x in s:
    print(s)


#To print characters present in string index wise:
s=input("Enter some string:")
i=0
for x in s:
    print("The character present at",i,"index is:",x)
    i=i+1

#To print hello  10 times
s="hello"
for x in range(10):
    print("hello")
    
#To display numbers from 0 to 10
for x in range(11):
    print(x)

#To display odd numbers from 0 to 20
for x in range(21):
    if(x%2!=0):
        print(x)
    
#To display numbers from 10 to 1 in desending order
for x in range(10,0,-1):
    print(x)

for o in range(10,0,-2):
    print(o)

for r in range(30,20,-2):
    print(r)


#To print sum of numbers present inside list
list=eval(input("Enter List:"))
sum=0
for x in list:
    sum=sum+x
print("The sum=",sum)

#Loop  through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#Loop throgh a range of numbers
for i in range(5):
    print(i)

#Loop with a step
for i in range(2, 11, 2):
    print(i)

#Loop through a string
for letter in "Python":
    print(letter)

#Loop with else
for i in range(3):
    print(i)
else:
    print("Loop finished!")


##For loops more examples :
s="python"
print("by using for loop programing")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
    print("by using for loop")
    for ch  in s:
        print("\t{}".format(ch))
    else:
        print("empty programing")
        
print("-"*50)

#for loop
s="python"
print("By using for loop logic-1 forward direction")
for ch in s:
    print("\t{}".format(ch))

print("-"*50)
        
print("By using for loop logic-2 forward direction with +ve index")
for i in range (len(s)):
    print("\t{}".format(s[i]))
    
print("-"*50)

        
print("By using for loop logic-3 forward direction with -ve index")
for i in range(-len(s),0):
    print("\t{}".format(s[i]))

print("-"*50)
        
print("by using for loop logic-4 backward direction ")
for ch in s[::-1]:
    print("\t{}".format(ch))
    
print("-"*50)

print("By using for loop logic-5 backward ddirection with +ve index")
for i in range(len(s)-1,-1,-1):
    print("\t{}".format(s[i]))

print("-"*50)

print("By using for loop logic-6 backward direction with -ve index")
for i in range(-1,-(len(s)+1),-1):
    print("\t{}".format(s[i]))
    
print("-"*50)

##program for Displaying the Values of List and dict by using for loop
lst=[100,"swathi","Delhi",34.56,"python"]
for value in lst:
    print("\t{}".format(value))

print("-"*50)
                                                  
d={10:"mango",20:"Apple",30:"sberry",40:"kiwi"}
for x in d:
    print("\t{}--->{}".format(x,d[x]))

print("-"*50)

d={10:"mango",20:"Apple",30:"sberry",40:"kiwi"}   
for x in d:
    print("\t{}--->{}".format(x,d.get(x)))


#for loop
n=int(input("Enter How Many Numbers u want to generate:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("List of  Numbers within:{}".format(n))
    for i in range(1,n+1):
        print("\t{}".format(i))
print("------------------------------------------")
print("List of Even Numbers within:{}".format(n))
for i in range(2,n+1,2):
    print("\t{}".format(i))
print("------------------------------------------")
print("List of Odd Numbers within:{}".format(n))
for i in range(1,n+1,2):
    print("\t{}".format(i))
print("------------------------------------------")

#To generate tables with for loops
n=int(input("Enter a Number for Generating Mul table:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Mul Table for {}".format(n))
    print("-" * 50)
    for i in range(1,11):
        print("\t{} x {}={}".format(n,i,n*i))
    else:
        print("-" * 50)

#Program for Finding sum of First N Natural Numbers.
n=int(input("Enter How Natural Nums Sum U want to Find:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Natural Numbers within:{}".format(n))
    p=0 # Additive Identity--Keeps Track of repeated sum
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p+i
    else:
        print("-"*50)
        print("sum={}".format(p))
        print("-" * 50)


#Program for Finding sum of First N Natural Numbers
# also find Sum of Square and Sum of Cubes First N Natural Numbers.
n=int(input("Enter How Natural Nums U want to Find:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Nat Nums\t\tSquares\t\t\tCubes")
    s,ss,cs=0,0,0 # Additive Identity--Keeps Track of repeated sum
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}\t\t\t\t{}\t\t\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("-"*50)
        print("\t{}\t\t\t\t{}\t\t\t{}".format(s,ss,cs))
        print("-" * 50)

#Program for Finding Product of First N Natural Numbers.
n=int(input("Enter How Natural Nums Product U want to Find:"))
if(n<=0):
    print("\t{} is Invalid Input".format(n))
else:
    print("-"*50)
    print("Natural Numbers within:{}".format(n))
    p=1 
    print("-" * 50)
    for i in range(1,n+1):
        print("\t{}".format(i))
        p=p*i
    else:
        print("-"*50)
        print("Product={}".format(p))
        print("-" * 50)

#Program for Finding Fcatorial of a Number
n=int(input("Enter a Number for Finding Factorial:"))
if(n<0):
    print("\t{} is -VE Value--can't cal Factrial".format(n))
else:
    fact=1
    for i in range(1,n+1):
        fact*=i # OR fact=fact*i
    else:
        print("factroail({})={}".format(n,fact))



