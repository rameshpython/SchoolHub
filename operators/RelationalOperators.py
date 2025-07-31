#Relational operators (comparisions)
#operators are : ==,!=,>,<,>=,<=
#Operators
#==	Equal to
#!=      Not equal to
#>       Greater than
#<       Less than
#>=      Greater than or equal
#<=      Less than or equal

#1.==	Equal to
a = 10
b = 10
print(a == b)

a=10
b=20
print(a==b)

a=10
b=15
print(a==b)

a=12
b=12
print(a==b)
print("-"*60)

#2.!=      Not equal to
a = 8
b = 5
print(a != b)

a=34
b=84
print(a!=b)

a=102
b=102
print(a!=b)
print("-"*60)

#3.>    Greater than
print(7 > 2)   # True
print(3 > 5)   # False
print(17>21)
print(55>43)
print(22>22)
print(1>1)
print("-"*60)

#4.<       Less than
print(3 < 10)  # True
print(4<8)

print(25<29)

print(39<28)

print(32<32)

print(3<3)
print("-"*60)

#5.>=      Greater than or equal
print(6 >= 6)  # True
print(9 >= 3)  # True

print(27>=24)
print(43>=98)
print(29>=29)
print(29>=48)
print("-"*60)

#6.<=      Less than or equal
print(4 <= 4)  # True
print(2 <= 9)  # True

print(37<=24)

print(43<=98)

print(29<=29)

print(29<=48)

print("-"*60)

a=10
b=20
print("a>b is",a<b)
print("a>=b is",a>=b)
print("a<b is",a<b)
print("a<=b is",a<=b)
print("-"*50)

#we can apply relational operaqtors for str type also
a="gaganam"
b="ramesh"
print("a>b is",a>b)
print("a>=b is",a>=b)
print("a<b is",a<b)
print("a<=b is",a<=b)
print("-"*50)

a="durga"
b="durga"
print("a>b is",a>b)
print("a>=b is",a>=b) 
print("a<b is",a<b)
print("a<=b is",a<=b)
print("-"*50)

a="rajesh"
b="rohan"
print("a>b is",a>b)
print("a>=b is",a>=b)
print("a<b is",a<b)
print("a<=b is",a<=b)
print("-"*50)

#== (and) !=
print(10==20)

print(10!=20)
print(10!=10)

print(10==True)
print(10==False)

print(30==30)
print(2==20)

print(10!=20)
print(20!=20)

#Relational  operator programming
#float 
a=float(input("Enter Value of a:"))
b=float(input("Enter value of b:"))
print("\tresults of relatioal expreesions")
print("-"*50)
print("\t\t{}<{}={}".format(a,b,a<b))
print("\t\t{}>{}={}".format(a,b,a>b))
print("\t\t{}=={}={}".format(a,b,a==b))
print("\t\t{}!={}={}".format(a,b,a!=b))
print("\t\t{}<={}={}".format(a,b,a<=b))
print("\t\t{}>={}={}".format(a,b,a>=b))
print("-"*50)

#int
a=int(input("Enter Value of a:"))
b=int(input("Enter value of b:"))
print("\tresults of relatioal expreesions")
print("-"*50)
print("\t\t{}<{}={}".format(a,b,a<b))
print("\t\t{}>{}={}".format(a,b,a>b))
print("\t\t{}=={}={}".format(a,b,a==b))
print("\t\t{}!={}={}".format(a,b,a!=b))
print("\t\t{}<={}={}".format(a,b,a<=b))
print("\t\t{}>={}={}".format(a,b,a>=b))
print("-"*50)

#Relational operators with string
#Python compares strings lexicographically (alphabetical order, using Unicode value of characters).
#lexicographically means assending order in unicode(like ascii type)
print("apple" == "apple")   # True
print("apple" != "banana")  # True
print("apple" < "banana")   # True (a < b)
print("Zebra" > "ant")      # False ('Z' > 'a' in Unicode)
print("Apple" < "apple")    # True ('A' < 'a' in Unicode)
print("Apple" <= "apple")    # True ('A' <= 'a' in Unicode)
print("Zebra" >= "ant")      # False ('Z' >='a' in Unicode)
print("-"*50)

#Relational operators with boolean
#True is treated as 1, and False is treated as 0 in comparisons.
print(True == True)     # True
print(True != False)    # True
print(True > False)     # True  (1 > 0)
print(False < True)     # True  (0 < 1)
print(True >= False)    # True
print(True <=False)     #False
print(False>True)       #False
print("-"*50)

#Mixes Examples(string and boolean)
print("hello" == True)     # False
print(True == 1)           # True
print(False == 0)          # True
print("True" == True)      # False (string ≠ boolean)
#print(True>"ant")         #TypeError: '>' not supported between instances of 'bool' and 'str'
#print("Zebra"<=True)       #TypeError: '<=' not supported between instances of 'str' and 'bool'










