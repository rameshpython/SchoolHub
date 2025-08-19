#pass statement
for i in range(1,6):#outer loop 
    print("outer loop--value of i={}".format(i))
    for j in range(1,4):#inner loop
        print("\tInner loop--value of j={}".format(j))
    else:
        print("\t I am from also part of Inner loop")
else:
    print("I am from else part of outer loop")


for i in range(1,8): # Outer loop
    print("Outer Loop--Value of i={}".format(i))
    print("-"*50)
    for j in range(1,6): # inner loop
        print("\tInner Loop--Value of j={}".format(j))
    else:
        print("\tI am from else part of Inner Loop")
        print("-" * 50)
else:
    print("I am from else part of Outer Loop")
print("--------------------------------------------------")

#Examples of pass in python
#Example-1
# for loop with pass
for i in range(5):
    if i == 2:
        pass   # placeholder, does nothing
    else:
        print(i)

# while loop with pass
n = 3
while n > 0:
    pass   # infinite loop (does nothing)
    n -= 1 #n=-1

print("----------------------------------------------------")

#pass with operators(inside conditions)
x = 10
y = 20

# using pass in if with relational operator
if x < y:
    pass   # do nothing when condition true
else:
    print("x is not less than y")

# using pass in logical operator
if (x > 0 and y > 0):
    pass   # both positive, but no action
else:
    print("At least one is not positive")

print("-----------------------------------------------")

#pass in datatypes
# in function that works with list (datatype)
def process_list(mylist):
    for item in mylist:
        if isinstance(item, int):
            pass   # skip integers
        else:
            print(item)

process_list([1, "apple", 2, "banana"])

# in class (custom datatype)
class Student:
    pass   # empty class (placeholder)
