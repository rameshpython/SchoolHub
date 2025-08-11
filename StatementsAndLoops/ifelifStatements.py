#if-elif-else satements
#some programing examples
#Q.program for accepting Two Numerical values and Find Biggest
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
if(a>b):
    print("Max({},{})={}".format(a,b,a))
elif(b>a):
    print("Max({},{})={}".format(a,b,b))
else:
    print("Both values are equal")
print("program execution completed")

#Q.Accepting the Digits and Display Its Name
d=int(input("Enter Any Digits:"))
if(d==0):
    print("{} is zero".format(d))
elif(d==1):
    print("{} is one".format(d))
elif(d==2):
    print("{} is two".format(d))
elif(d==3):
    print("{} is three".format(d))
elif(d==4):
    print("{} is four".format(d))
elif(d==5):
    print("{} is five".format(d))
elif(d==6):
    print("{} is  six".format(d))
elif(d==7):
    print("{} is seven".format(d))
elif(d==8):
    print("{} is eight".format(d))
elif(d==9):
    print("{} is nine".format(d))
elif(d>9):
    print("{} is number".format(d))
elif(d<0)  and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -ve number".format(d))
else:
    print("{} is -ve Digit".format(d))
print("program execution completed")

#Q.elif using programing
brand=input("Enter your favourite Brand:")
if brand=="RC":
    print("it is childrens brand")
elif brand=="kf":
    print("it is not that much kick")
elif brand=="Bp":
    print("Buy one get one free")
else:
    print("other brands are not recomended")

#Example-1
#checking grades
marks=75
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=50:
    print("Grade C")
else:
    print("Fail")

#Example-2
#checking the day type
day="saturday"
if day=="monday":
    print("starts of the week")
elif day=="sunday":
    print("week of the day")
elif day=="saturday" or day=="sunday":
    print("its  the weekend")
else:
    print("just a normal weekend")

#Example-3
#Temperature check
temp=15
if temp>30:
    print("it is hot outside")
elif temp>20:
    print("its warm outside")
elif temp>10:
    print("its cool outside")
else:
    print("its cold outside")

    




