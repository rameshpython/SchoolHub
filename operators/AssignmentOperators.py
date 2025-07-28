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






