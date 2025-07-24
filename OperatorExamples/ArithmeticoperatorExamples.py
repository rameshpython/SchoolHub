#All Types of Arithmetic models
#1.Addition of two numbers
a=24
b=56
result=a+b
print("Addition:",result)

#2.Subtraction of two  numbers
a=76
b=34
result=a-b
print("Subtraction:",result)

#3.Multiplication of two numbers
a=23
b=15
result=a*b
print("Multiplication:",result)

#4.Division of two numbers
a=54
b=45
result=a/b
print("Division:",result)

#5.Floor Diision of  two numbers
a=54
b=45
result=a//b
print("Floor division:",result)

#6.Modulus
a=28
b=19
result=a%b
print("Modulus:",result)

#7.Exponention
base=4
power=6
result=base**power
print("4^6:",result)

#8.Average of two numbers
a=100
b=250
avg=(a+b)/2
print("Average:",avg)
#Average=
#Number of values
#Sum of all values

#Average of three numbers
a=10
b=20
c=30
avg=(a+b+c)/3
print("Average:",avg)

#9.Area of triangle
base=15
height=5
area=(base*height)/2
print("area of  triangle:",area)

base=75
height=55
area=(base*height)/2
print("area of triangle:",area)

#10.convert fahrenheit to celsius

#Formula ==> Celsius=5/9*(98.6-32)=5/9*66.6 = 37 degree celsius
#Convert 98.6°F to Celsius:
fahrenheit = 98.6
celsius = (5/9) * (fahrenheit - 32)
print("Celsius:", celsius)

#11.convert celsius to fahrenheit
#Formula ==> Fahrenheit=(celsius*9/5)+32
#Convert 37°C to Fahrenheit:
#Fahrenheit=(37*9/5)+32=66.6+32=98.6 degree F
celsius = 37
fahrenheit = (celsius * 9/5) + 32
print("Fahrenheit:", fahrenheit) 

#12.swap two numbers (without third variable)
a = 10
b = 20

# Swapping
a, b = b, a

print("a:", a)  
print("b:", b)  

a=5
b=7
a=a+b
b=a-b
a=a-b
print("a:",a,"b:",b)

#13.Simple interest
p=10000#(p=principle anount)
t=5#(t=time)
r=10#(r=rate of interest)
si=(p*t*r)/100
print("simple interst:",si)


p=2450#(p=principle anount)
t=8#(t=time)
r=6#(r=rate of interest)
si=(p*t*r)/100
print("simple interst:",si)

#14.Total marks and percentage
#Formula ==> Percentage=(Obtained Marks/Total marks)×100
#Example:You scored 450 out of 500 marks:
#Percentage=(450/500)×100=0.9×100=90%
obtained = 450
total = 500
percentage = (obtained / total) * 100
print("Percentage:", percentage)
m1=80
m2=90
m3=75
m4=85
m5=95
total=m1+m2+m3+m4+m5
percentage=(total/500)*100
print("Total:",total)
print("Percentage:",percentage)

#15.Calculate speed (distance/time)
distance=170#km
time=4#hours
speed=distance/time
print("speed:",speed,"km/hr")

#16.perimeter of a rectangle
length=16
breadth=12
perimeter=2*(length+breadth)
print("Perimeter:",perimeter)

#17.Area of circle(approximate pi=3.14)
radius=7
pi=3.14
area=pi*radius*radius
print("Area of circle:",area)

#18.Convert Days to weeks and Days
days=20
weeks=days//7
remaining_days=days%7
print("weeks:","weeks,Days:",remaining_days)

#19.Digit sum of 3-digit numbers(e.g-456-->4+5+6)
num=456
hundreds=num//100
tens=(num%100)//10
units=num%10
total=hundreds+tens+units
print("Digit sum:",total)

#20.Calculate square and cube
num=15
square=num**2
cube=num**3
print("square:",square)
print("cube:",cube)














