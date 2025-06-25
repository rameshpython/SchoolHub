#octal number system
#Digits : 0 1 2 3 4 5  6 7 = 8digits
#Base : 8
#The octal Data must be preceded with a letter  0o or 0O
#Examples :
a=0o17
print(a,type(a))

a=0O236
print(a,type(a))

a=0O765
print(a,type(a))

#Base conversion technique
# oct()

#Decimal to octal

a=45
ov=oct(a)
print(ov,type(ov))

a=745
ov=oct(a)
print(ov,type(ov))

b=766
ov=oct(b)
print(ov,type(ov))

#Binary to octal

a=0b1001
ov=oct(a)
print(ov,type(ov))

b=0B1111
ov=oct(b)
print(ov,type(ov))

c=0b1010
ov=oct(c)
print(ov,type(ov))

ov=oct(14)
print(ov,type(ov))

#hexa to octal

a=0x14
ov=oct(a)
print(ov,type(ov))

b=0X17
ov=oct(b)
print(ov,type(ov))

c=0xF
ov=oct(c)
print(ov,type(ov))

d=0XE
ov=oct(d)
print(ov,type(ov))






