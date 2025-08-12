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



