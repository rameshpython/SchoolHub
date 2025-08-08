#Assignment Operators
#1. += --> Add and Assign
x = 10
x += 5  # same as x = x + 5
print(x)

x=-10
x+=5
print(x)

x=10.5
x+=4
print(x)

#x="ramesh"
#x+=4
print(x)#TypeError: can only concatenate str (not "int") to str

x="ramesh"
x+="gaganam"
print(x)
print("--------------------------------------------------")
#x+=200
print(x)
text="Hello"
text+="World"
print(text)

list=[1,2]
my_list=[1,2]
my_list+=[3,4]
print(my_list)

total=0
for i in range(1,6):
     total+=i
     print(i)


#2. -= --> Subtract and Assign
x = 20
x -= 7  # same as x = x - 7
print(x)

#3. *= --> Multiply and Assign
x = 6
x *= 3  # same as x = x * 3
print(x)

#4. /= --> Divide and Assign (Float division)
x = 20
x /= 4  # same as x = x / 4
print(x)

#5. //= --> Floor Divide and Assign
x = 17
x //= 4  # same as x = x // 4
print(x)

#6. %= --> Modulus and Assign
x = 10
x %= 3  # same as x = x % 3
print(x)

#7. **= --> Exponentiate and Assign
x = 3
x **= 2  # same as x = x ** 2 → 3^2
print(x)


#8. &= → Bitwise AND and Assign

#Bitwise AND(&) and assign operator
a=1 & 0
b=0 & 1
c=0 & 0
d=1 & 1
print(a,b,c,d)


a=16
b=bin(a)
print(b)

a = 13        
b = 6     
c = a & b     
print(c)

a = 7   # binary: 0111
b = 3   # binary: 0011

a &= b  # same as a = a & b

print(a)

flags=15
mask=13
flags&=mask #-->flags=flags & mask
print(flags)

s={1,2,3}
s&={2,3,4}
print(s)

s={1,2,3}
s1={2,3,4}
s&=s1
print(s)





#9. |= → Bitwise OR and Assign

#Bitwise OR (|) and assign operator
a= 1 | 0
b= 0 | 1
c= 0 | 0
d= 1 | 1
print(a,b,c,d)


x = 12   # binary: 1100
y = 5    # binary: 0101

x &= y   # x = x & y

print(x)
print("------------------------")
x = 1100  #(12 in binary)
y =  101 #(5 in binary)
  
x &= y  #(4 in binary)
print(x)


a = 65     
b = 58       
a|= b   
print(a)

True | False     # → True (bitwise)
True or False    # → True (logical)

s1 = {1, 2}
s2 = {2, 3}
s1 |= s2

#10. ^= → Bitwise XOR and Assign
#The ^= is a compound assignment operator
#a^=b --> a=a^b
#Rule :Returns 1 only if the bits are different

a=1 ^ 0 # a^=b

b=0 ^ 1 #b^= 

c=1 ^ 1 

d=0 ^ 0

print(a,b,c,d)


a = 10 # 1010
b = 7  # 0111

a ^= b
print(a)

x = 12# 1100
y = 5# 0101

x ^= y# x = x ^ y
print(x)

#Swapping variables
a = 5
b = 7

a ^= b #a=a^b
b ^= a #b=b^a
a ^= b #a=a^b

print(a, b)



#11. >>= → Right Shift and Assign
x = 8      # binary: 1000
x >>= 2    # shifts two bits → 0010
print(x)

a = 16      # binary: 10000
a >>= 2     # shift right by 2 bits
print(a)

x = 20      # binary: 10100
x >>= 1
print(x)

x = 10      # binary: 1010
x >>= 3
print(x)

x = 5       # binary: 0101
x >>= 2
print(x)


#12. <<= → Left Shift and Assign
x = 3      # binary: 0011
x <<= 2    
print(x)

a = 5       # binary: 0101
a <<= 2     # shift left by 2 bits
print(a)

x = 3       # binary: 0011
x <<= 1
print(x)

x = 4       # binary: 0100
x <<= 3
print(x)

a = 1       # binary: 0001
a <<= 4
print(a)


#Examples with programing :
#AssignmentOp1.py
a,b=input("Enter Value of a:"),input("Enter Value of b:")
print("-"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
#Swapping logic
a,b=b,a # Multi Line assigment
print("-"*50)
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("-"*50)

#AssignmentOp2.py
a,b=input("Enter Value of a:"),input("Enter Value of b:")
print("-"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
#Swapping logic
t=a
a=b
b=t
print("-"*50)
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("-"*50)

#AssignmentOp3.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
print("-"*50)
#Swapping Logic
a=a+b
b=a-b
a=a-b
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("-"*50)

#AssignmentOp4.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
print("-"*50)
#Swapping Logic
a=a*b
b=a//b
a=a//b
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("-"*50)


#AssignmentOp5.py
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("-"*50)
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
print("-"*50)
#Swapping Logic
a=a^b # Bitwise XOR ( ^ )
b=a^b
a=a^b
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
print("-"*50)



print("--------------------------------------------------------")
#assignmentop1.py
#multi
#multiline Assignment
a,b=input("Enter a value of a:"),input("Enter a value of b:")
print("-"*50)
print("_______________________________")
print("\toriginal value of a ={}".format(a))
print("\toriginal value of b ={}".format(b))
#swapping logic
a,b=b,a #multi line assignment
a,b=int(input("Enter Value of a:")),int(input("Enter Value of b:"))
print("\tOriginal value of a={}".format(a))
print("\tOriginal value of b={}".format(b))
a=a^b # Bitwise XOR ( ^ )
b=a^b
a=a^b
print("\tSwapped value of a={}".format(a))
print("\tSwapped value of b={}".format(b))
bin(84)

bin(45)
45^84
print(int(0b111001))
84^45



#Short hand operators
#Examples
bal=5000
damt=6000
bal=bal+damt#normal  Expression
print(bal)

print("_"*50)

bal=5000
damt=7000
bal+=damt #+= is called short and operator
print(bal)

print("_"*50)

a=10
b=20
a=a*b
print(a)

print("----------------")

a=10
b=2
a=a-b

#OR

a=10
b=2
a-=b
print(a)

print("---------------------")

a=3
b=4
c=5
a=a+b*c
print(a)

#OR

a=3
b=4
c=5
a+=b*c
print(a)

print("-----------------------------------")

a=23
b=56
c=98
a+=b/c
print(a)

a=34
b=67
c=21
a-=b**c
print(a)





