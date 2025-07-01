#Complex Datatype examples
#Examples :
#A Complex number as real and immaginary part.
#1.What is a Complex datatype in python?Give an example.

#A compex number is written as:

#a + bj

#a-->real part(float or int)
#b-->imaginary(float  or int)
#j-->imaginary unit(like root-1),used in python instead of i

#creating a complex number
num=3+4j
print(num,type(num))
#Accessing real and imaginary parts
print("Real part:",num.real)
print("imaginary part:",num.imag)

#Another Example
c=complex(6,9)
print(c)

#2.Simple complex Number
z=3+4j
print(z)

#3.Accessing real  and imaginary parts.
z=5-3j
print(z.real)
print(z.imag)

#4.Using complex() function.
z=complex(7,8)
print(z)

#5.Adding two complex numbers.
a=3.6j
b=6.9j
result=a+b
print(result)

#6.Multiplying complex numbers.
z1=7.4j
z2=8.2j
result=z1*z2
print(result)

#7.conjugate of a complex number.
z=7.4j
print(z.conjugate())

#8.using abs() to find magnitude.
z=9+5j
print(abs(z))

#9.Complex division.
z1=7+3j
z2=4+8j
result=z1/z2
print(result)






