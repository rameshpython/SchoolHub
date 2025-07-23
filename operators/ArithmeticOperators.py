#OPERATORS :
#1. Arithmetic Operators
#2. Assignment Operator
#3. Relational Operators (Comparision )
#4. Logical Operators (Comparision )
#5. Bitwise Operators
#6. Membership Operators
#    a) in operator
#    b) not in Operator
#7. Identity Operators
#    a) is operator
#    b) is not Operator


print("---------------------------------------------------------------------------------------------------------")

a=float(input("Enter Value of a:"))
b=float(input("Enter value of b:"))
print("-"*50)

print('-'*100)
print("------------------------------------------------------------------")
print("\t\t{}+{}={}".format(a,b,a+b)) 
print("\t\t{} - {} = {}".format(a,b,a-b))
print("\t\t{}*{}={}".format(a,b,a*b))
print("\t\t{}%{}={}".format(a,b,a%b))
print("\t\t{}/{}={}".format(a,b,a/b))
print("\t\t{} / {} = {}".format(a,b,a/b))
print("\t\t{}//{}={}".format(a,b,a//b))
print("\t\t{}**{}={}".format(a,b,a**b))
 
print("\t\t{} ** {} = {}".format(a,b,a**b))
print("-"*50)
a=10
b=5
print(a+b)

print(a-b)

print(a*b)

print(a/b)
print(a%b)
print(a//b)

print(a**b)
print("-"*100)


a=25
b=65
print('a+b=',a+b)
          
#SyntaxError: invalid syntax. Perhaps you forgot a comma?
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a%b=',a%b)
print('a//b=',a//b)
print('a**b=',a**b)
print("-"*60)

print("----------------------------------------------------------------------------------------------------------")

#We use operators +,* in "str" and the results will shown in examples
#Examples :
#   "durga"+10
#TypeError: can only concatenate str (not "int") to str
"durga"+"10"
#"durga"+10
#TypeError: can only concatenate str (not "int") to str

    
#TypeError: can only concatenate str (not "int") to str
"durga"+"durga"
"durga"+"10"
"rames"+"7995898858"
"durga"*2
2*"durga"

#4.6*"durga"
#TypeError: can't multiply sequence by non-int of type 'float'

    
#"durga"+2.4
#TypeError: can only concatenate str (not "float") to str

   
#"durga"*"durga"
#TypeError: can't multiply sequence by non-int of type 'str'

"durga"+"durga"
'durgadurga'
#"durga"-"durga"#TypeError: unsupported operand type(s) for -: 'str' and 'str'

#"durga"-"durga"
#TypeError: unsupported operand type(s) for -: 'str' and 'str'

print('-------------------------------------------------------------------------------')

# + ===> string concatenation operator, only(+)can use in sring for concatenation
# * ===> string multiplication operator ,only(*)can use in string for multiply values

a="Hello"
b="World"
result=a+b
print(result)
result=(a+"  "+b)
print(result)

#list concatenation
a=[1,3,6]
b=[9,8,7]
print(a+b)

List1=[54,65,90]
List2=[76,34,22]
print(List1+List2)

name="ramesh"
age=25
#print(name+age)
#TypeError: can only concatenate str (not "int") to str

name="ramesh"
age="25"
print(name+age)
print("-"*50)

name="ramesh"
age=25
print(name+str(age))


first="Good"
second="Morning"
combined=first+"    "+second+"!"
print(combined)

# * ===> string multiplication operator ,only(*)can use in string for multiply values
print("goodmorning"*5)

print("Hi"*3)

print("ramesh"*4)

#print("ram"*"3")
#TypeError: can't multiply sequence by non-int of type 'str'


print(6*"Hello")

print("*"*10)

#print("ram"*2.5)
#TypeError: can't multiply sequence by non-int of type 'float'



#Arithmetic operators in python (+,-,*,/,%,//,**)are mainly used with Numeric datatypes They are-int,float,bool,complex
#1.integer(int)
a=10
b=20
print('a+b=',a+b)
print('a-b=',a-b)
print('a*b=',a*b)
print('a/b=',a/b)
print('a%b=',a%b)
print('a//b=',a//b)
print('a**b=',a**b)

#2.floating point(float)
x=2.4+6.7
print(x)
y=3.5-1.2
print(y)

x=2.4+6.7
print(x)
y=3.5-1.2
print(y)

z=4.5*5.8
print(z)

a=1.1/2.3
print(a)

b=2.3/4.5
print(b)
b=2.3//4.5
print(b)

#3.Boolean(bool)
#True=1
#False=0
print(True+5)
print(True+5)

print(False+2)

print(True+False)

print(True-3)
print(-5-True)
print(True-(-3))

a=True+4
print(a)

b=False+2
print(b)
c=False-2
print(c)
print(True*2)

print(False*2)

print(True/3)
print(False//2)

print(True**4)

print(False**3)

#4.Complex Numbers (complex)
x=(2+3j)+(3+4j)
print(x)
y=(3+4j)-(3+5j)
print(y)
z=(6+7j)*(8+9j)
print(z)
a=(2+3j)/(3+4j)
print(x)
#b=(3+4j)//(3+5j)#TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
print(y)
c=(6+7j)**(8+9j)
print(c)








