#what ia a float in python?give an example.
#A float is a number with a decimal point.
#1.Examples :Basic questions.
#A float is a number with a decimal point.
price=99.99
print(price,type(price))

#2.Write a program to add two float numbers.
a=5.9
b=9.7
result=a+b
print(result)
#  or
print("sum:",result)#This shows,sum = o/p.

#3.Writre a program to multiply a float with an intiger.
a=54.9
b=8
total=a+b
print("Total Marks:",total)

#4.convert an integer to a float.
num =10
float_num=float(num)
print(float_num)

#5.convert a string to a float
a="542.864"
float_number=float(a)
print(float_number)

#intermediate questions.

#6.Divide two float numbers and round the result.
a=5.6
b=8.4
result=round(a/b,2)
print(result)

#7.Check if a number is of float type using.(isinstance().)
x=54.65
print(isinstance(x,float))
#   or
print(isinstance(x,int))

#8.Take user input for float numbers and calculate average.
a=45.45
b=54.95
avg=(a+b)/2
print(avg,type(avg))#for given value only gives output
#   or
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
avg=(a+b)/2
print("Average:",avg)#we have give numbers to get output

#9.Calculate simple interest using float values.
#simple interst mention in 'PTR'=principle,time,rate
P=float(input("Enter Principle:"))
T=float(input("Enter Time:"))
R=float(input("Enter Rate:"))
SI=(P*T*R)/100
print("simple Interest:",SI)
#   or
P=5000
T=10
R=4
SI=(P*T*R)/100
print(SI)

#10.Program to find area of a  circle using float.
radius=float(input("Enter radius:"))
area=5.8546*radius*radius
print("Area of circle:",area)

#11.What happens if you divide an integer by a float.
result=18/7.8
print(result,type(result))
print(15/5.4)
print(54/2.7)
print(585/54.8)

print(4/2,type)
print(4/2.0,type)

#12.Can a float value be used in range() function.
#No,a float  value cannot be used directly in the range()function in python.

#Example:
#for i in range(1.0,5.0):
#    print(i)

    #TypeError:'float'object cannot be interpreted as an integer.

#13.How to control number of Decimal places in output.
num=5.65424854
print(round(num,2))
print(format(num,".2f"))
      
                   







