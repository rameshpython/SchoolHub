#We ha 4  types of number systems They are
#1.Decimal number system
#2.Binary number system
#3.octal number system
#4.hexa decimal numner system
#decimal number system=0 1 2  4 5  6 7 8 9
#digits :10
#base :10

#binary number system = 0 1
#digits :2
#base :2
#The binary number preceded with a Letter 0b or 0B
#Examples :

a=0b0101
print(a,type(a))
b=0B00010000
print(b,type(b))

print(0b1111)
print(0b100)

c=0b1001
print(c)

a=5
bv=bin(a)
print(bv,type(bv))
a=16
bv=bin(a)
print(bv,type(bv))

#base conersion technique in python
#To convert the one base value to another base value
#3 types in it :bin(),oct(),hex()
# 1.bin()

#Decimal to binary

a=45
bv=bin(a)
print(bv,type(bv))

bv=bin(20)
print(bv,type(bv))

bv=bin(124)
print(bv,type(bv))

#octal to binary

a=0o15
bv=bin(a)
print(bv,type(bv))
bv=bin(0O17)
print(bv,type(bv))
bv=bin(0o1347)
print(bv,type(bv))

#hexa Decimal to binary

a=0x15
bv=bin(a)
print(bv,type(bv))

a=0XF
bv=bin(a)
print(bv,type(bv))

bv=bin(0xe)
print(bv,type(bv))









