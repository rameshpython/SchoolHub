#Hexa Decimal number system
#Digits : 0 1 2 3 4 5 6 7 8 9
#A or a(10),B or b(11),C or c(12),D or d(13),E or e(14),F or f(15)
#Total Digits :16
#Hexa decimal data must be preceded with 0x or 0X
#Examples :
a=0xac
print(a,type(a))

b=0xBEE
print(b,type(b))

c=0x789
print(c,type(c))

d=0XEFB
print(d,type(d))

#Base conversion technique
#Deccimal to hexa decimal 
a=76
hv=hex(a)
print(hv,type(hv))

b=9876
hv=hex(b)
print(hv,type(hv))

c=2356
hv=hex(c)
print(hv,type(hv))

#Binary ti hexa decimal
a=0b1010
hv=hex(a)
print(hv,type(hv))

b=0B1111
hv=hex(b)
print(hv,type(hv))

c=0b0101
hv=hex(c)
print(hv,type(hv))

#octal to Hexa decimal
a=0o143
hv=hex(a)
print(hv,type(hv))

b=0O745
hv=hex(b)
print(hv,type(hv))

c=0o167
hv=hex(c)
print(hv,type(hv))








