#Program for Cal Roots of Quadratic Equation
def getvals():
    a=float(input("Enter Value of a:"))
    b = float(input("Enter Value of b:"))
    c = float(input("Enter Value of c:"))
    return a,b,c

def caldes():
    a,b,c=getvals() # Function Call
    d1=(b*b)-(4*a*c)
    d=d1**0.5
    if(type(d)==float):
        if(d==0):
            print("Roots are Real and Equal")
            r1=-b/(2*a)
            r2=-b/(2*a)  # OR r2=r1
            print("Root1={}".format(r1))
            print("Root1={}".format(r2))
        elif(d>0):
            print("Roots are Real and Distinct")
            r1=(-b+d)/(2*a)
            r2=(-b-d)/(2*a)
            print("Root1={}".format(r1))
            print("Root1={}".format(r2))
    else:
        print("Roots are Real and Imaginary")
        r1 = (-b + d) / (2 * a)
        r2 = (-b - d) / (2 * a)
        print("Root1={}".format(r1))
        print("Root1={}".format(r2))

#main program
caldes()

print("---------------------------------------------------")

#Program for Cal Roots of Quadratic Equation

def getvals():
    a=float(input("Enter Value of a:"))
    b = float(input("Enter Value of b:"))
    c = float(input("Enter Value of c:"))
    return a,b,c

def caldes():
    a,b,c=getvals() # Function Call
    d=((b*b)-(4*a*c))**0.5
    return a,b,c,d

def calroots():
    a,b,c,d=caldes() # Function Call
    if (type(d) == float):
        if (d == 0):
            print("Roots are Real and Equal")
            r1 = -b / (2 * a)
            r2 = -b / (2 * a)  # OR r2=r1
            print("Root1={}".format(r1))
            print("Root1={}".format(r2))
        elif (d > 0):
            print("Roots are Real and Distinct")
            r1 = (-b + d) / (2 * a)
            r2 = (-b - d) / (2 * a)
            print("Root1={}".format(r1))
            print("Root1={}".format(r2))
    else:
        print("Roots are Real and Imaginary")
        r1 = (-b + d) / (2 * a)
        r2 = (-b - d) / (2 * a)
        print("Root1={}".format(r1))
        print("Root1={}".format(r2))
#main program
calroots()