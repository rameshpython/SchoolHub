#OPERATORS :
1. Arithmetic Operators
2. Assignment Operator
3. Relational Operators (Comparision )
4. Logical Operators (Comparision )
5. Bitwise Operators
6. Membership Operators
    a) in operator
    b) not in Operator
7. Identity Operators
    a) is operator
    b) is not Operator


print("---------------------------------------------------------------------------------------------------------")

>>> a=float(input("Enter Value of a:"))
Enter Value of a:54
>>> b=float(input("Enter value of b:"))
Enter value of b:87
>>> print("-"*50)
--------------------------------------------------
>>> print("-"+100)
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    print("-"+100)
          ~~~^~~~
TypeError: can only concatenate str (not "int") to str
>>> print('-'*100)
----------------------------------------------------------------------------------------------------
>>> print("\t\t{}+{}={}".format(a,b,a+b))
                54.0+87.0=141.0
>>> print("\t\t{}-{}={}"̣format(a,b,a-b))
  File "<python-input-10>", line 1
    print("\t\t{}-{}={}"̣format(a,b,a-b))
                        ^
SyntaxError: invalid character '̣' (U+0323)
>>> print("\t\t{} - {} = {}".format(a,b,a-b))
                54.0 - 87.0 = -33.0
>>> print("\t\t{}*{}={}".format(a,b,a*b))
                54.0*87.0=4698.0
>>> print("\t\t{}%{}={}".format(a,b,a%b))
                54.0%87.0=54.0
>>> print("\t\t{}\{}={}".format(a,b,a/b))
<python-input-14>:1: SyntaxWarning: invalid escape sequence '\{'
                54.0\87.0=0.6206896551724138
>>> print("\t\t{} / {} = {}".format(a,b,a/b))
                54.0 / 87.0 = 0.6206896551724138
>>> print("\t\t{}//{}={}".format(a,b,a//b))
                54.0//87.0=0.0
>>> print('\t\t{}**{}={}".format(a,b,a**b))
  File "<python-input-17>", line 1
    print('\t\t{}**{}={}".format(a,b,a**b))
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("\t\t{} ** {} = {}".format(a,b,a**b))
                54.0 ** 87.0 = 5.22705541827666e+150
>>> print("-"*50)
--------------------------------------------------
>>>
>>> a=10
>>> b=5
>>> print(a+b)
15
>>> print(a-b)
5
>>> print(a*b)
50
>>> print(a/b)
2.0
>>> print(a%b)
0
>>> print(a//b)
2
>>> print(a**b)
100000
>>> print("-"*100)
----------------------------------------------------------------------------------------------------
>>>
>>>
>>> a=25
>>> b=65
>>> print('a+b='a+b)
  File "<python-input-35>", line 1
    print('a+b='a+b)
          ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print('a+b=',a+b)
a+b= 90
>>> print('a-b=',a-b)
a-b= -40
>>> print('a*b=',a*b)
a*b= 1625
>>> print('a/b=',a/b)
a/b= 0.38461538461538464
>>> print('a%b=',a%b)
a%b= 25
>>> print('a//b=',a//b)
a//b= 0
>>> print('a**b=',a**b)
a**b= 7346839692639296924804603357639035486366659729825547009429698164240107871592044830322265625
>>> print("-"*60)
