#Special operators
#Identity operators
# we have Two Types of Identity Operators. They are
# 1. is Operator
# 2. is not Operator


#Examples

lst1=[10,"RS"]
print(lst1,type(lst1),id(lst1))
lst2=lst1 # Deep Copy
print(lst2,type(lst2),id(lst2))
lst1 is lst2
lst1 is not lst2
lst3=lst1.copy() # Shallow Copy
print(lst3,type(lst3),id(lst3))
lst1 is not lst3
lst1 is lst3
print("-------------------------------")
a=None
b=None
print(a,id(a))

print(b,id(b))

a is b
a is not b
print("-------------------------------")

d1={10:"Apple",20:"Mangoes"}
d2={10:"Apple",20:"Mangoes"}
print(d1,id(d1))

print(d2,id(d2))

d1 is d2

d1 is not d2
print("------------------------------")

s1={10,20,30,40}
s2={10,20,30,40}
print(s1,id(s1))
print(s2,id(s2))
s1 is s2

s1 is not s2
print("-----------------------------")

fs1=frozenset(s1)
fs2=frozenset(s1)
print(fs1,id(fs1))
print(fs2,id(fs2))
fs1 is fs2

fs1 is not fs2
print("------------------------------")

lst1=[10,20,30]
lst2=[10,20,30]
print(lst1,id(lst1))
print(lst2,id(lst2))
lst1 is lst2

lst1 is not lst2
print("-------------------------------")

tpl1=(1.2,2.3,4.5)
tpl2=(1.2,2.3,4.5)
print(tpl1,id(tpl1))
print(tpl2,id(tpl2))
tpl1 is tpl2

tpl1 is not tpl2
print("-------------------------------")

#NOTE: When multiple Str objects contains str Data with Same Case, Same Meaning and Same Order then 'is' Operator 
#Return True  and 'is not ' Operator retruns False
            
s1="PYTHON"
s2="PYTHON"
print(s1,id(s1))
print(s2,id(s2))
s1 is s2

s1 is not s2

s3="PYTHOn"
print(s3,id(s3))
s1 is s3
s1 is not s3

print("-----------------------------")
r1=range(10,21,2)
r2=range(10,21,2)
print(r1,id(r1))
print(r2,id(r2))
r1 is r2

r1 is not r2
print("-------------------------------")

b1=bytes([234,56,118,199])
b2=bytes([234,56,118,199])
print(b1,id(b1))
print(b2,id(b2))
b1 is b2

b1 is not b2
print("------------------------------")

b1=bytearray([234,56,118,199])
b2=bytearray([234,56,118,199])
print(b1,id(b1))
print(b2,id(b2))
b1 is b2
b1 is not b2

print("------------------------------")
a=2+3j
b=2+3j
print(a,id(a))
print(b,id(b))
a is b

a is not b
print("-------------------------------")

a=True
b=True
print(a,id(a))
print(b,id(b))
a is b

a is not b

a=1.2
b=1.2
print(a,id(a))
print(b,id(b))
a is b

a is not b

print("----------------------------------")
#NOTE: When int object contains values ranges from 0 to 256 then on those objects Contains Same Address Otherwise 
#contains Different Address.
a=256
b=256
print(a,id(a))
print(b,id(b))
a is b

a is not b

a=0
b=0
print(a,id(a))
print(b,id(b))
a is b

a is not b

a=257
b=257
print(a,id(a))
print(b,id(b))
a is b

a is not b
print("-------------------------------------")

#NOTE: When int object contains values ranges from -1 to -5 then on those objects Contains Same Address Otherwise 
#contains Different Address.
a=-1
b=-1
print(a,id(a))
print(b,id(b))
a is b

a is not b

a=-5
b=-5
print(a,id(a))
print(b,id(b))
a is b

a is not b
print("------------------------------------")
a=-6
b=-6
print(a,id(a))
print(b,id(b))
a is b
a is not b

print("-----------------------------------")
a,b=400,400
print(a,id(a))
print(b,id(b))
a is b
a is not b

a,b=1.2,1.2
print(a,id(a))
print(b,id(b))
a is b

a is not b

print("--------------------------------------")
lst1,lst2=[10,20,30],[10,20,30]
print(lst1,id(lst1))
print(lst2,id(lst2))
a is b
a is not b
