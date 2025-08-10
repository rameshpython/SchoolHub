#if_else statement conditions :

name =input("Enter Name:")
if name=="ramesh":
    print("hello")
else:
    print("bye")
print("program is completed")
    
print("------------------------------------------")

#Q.Program for Deciding Whether the given Value is Palindrome or Not
value=input("Enter any value:")
if(value==value[::-1]):
    print("{} is palindrome".format(value))
else:
    print("{} is not palindrome".format(value))
print("program execution completed")

#Q.program for accepting Two Numerical values and Find Biggest
a=float(input("Enter value of a:"))
b=float(input("Enter value of b:"))
if(a>b):
    print("max({},{})={}".format(a,b,a))
else:
    if(b>a):
       print("max({},{})={}".format(a,b,b))
    else:
        print("Both values are equal")
    print("\tI am from other statement of inner if..else stmt")
print("I am from Other Statement of Outer if..else Stmt")


#Q.Accepting the Digits and Display Its Name
d=int(input("Enter any digit:"))
if(d==0):
    print("{} is zero".format(d))
else:
        if(d==1):
            print("{} is one".format(d))
        else:
            if(d==2):
                print("{} is two".format(d))
            else:
                if(d==3):
                    print("{} is three".format(d))
                else:
                    if(d==4):
                        print("{} is  four".format(d))
                    else:
                        if(d==5):
                            print("{} is five".format(d))
                        else:
                            if(d==6):
                                print("{} is  six".format(d))
                            else:
                                if(d==7):
                                    print("{} is seven".format(d))
                                else:
                                    if(d==8):
                                        print("{} is eight".format(d))
                                    else:
                                        if(d==9):
                                            print("{} is nine".format(d))
                                        else:
                                            if(d>9):
                                                print("{} is number".format(d))
                                            else:
                                                if(d<0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
                                                    print("{} is -ve number".format(d))
                                                else:
                                                    print("{} is -ve digit".format(d))
print("program execution completed")

#Q.Accepting the Digits and Display Its Name
#This program is from if statement examlple of upper one to written in if statement only
d=int(input("Enter Any Digits:")) #  0 1 2 3 4 5 6 7 8 9
if(d==0):
    print("{} is Zero".format(d))
if(d==1):
    print("{} is ONE".format(d))
if(d==2):
    print("{} is TWO".format(d))
if(d==3):
    print("{} is THREE".format(d))
if(d==4):
    print("{} is FOUR".format(d))
if(d==5):
    print("{} is FIVE".format(d))
if(d==6):
    print("{} is SIX".format(d))
if(d==7):
    print("{} is SEVEN".format(d))
if(d==8):
    print("{} is EIGHT".format(d))
if(d==9):
    print("{} is NINE".format(d))
if(d>9):
    print("{} is Number".format(d))
if(d<0) and d not in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -VE Number".format(d))
if(d<0) and d in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
    print("{} is -Ve Digit".format(d))
print("Program execution Completed")
