#string  Handling :
#The pre-defined functions in sring object are  given :
print("-------------")
#1.capitalize()
print("-------------")
s="ramesh"
s.capitalize()
print(s,type(s))


>>> s="python"
>>> print(s,type(s))
python <class 'str'>
>>> s.capitalize()
'Python'
>>> len(s)
6
>>>
>>> s='ramesh'
>>> print(s,type(s))
ramesh <class 'str'>
>>> s.capitalize()
'Ramesh'
>>>
>>> s='''ramesh'''
>>> print(s,type(s))
ramesh <class 'str'>
>>> s.capitalize()
'Ramesh'
>>>
>>> s="my name is  gaganam ramesh"
>>> print(s,type(s))
my name is  gaganam ramesh <class 'str'>
>>> s.capitalize()
'My name is  gaganam ramesh'

#2.title()
>>> s="python"
>>> print(s,type(s))
python <class 'str'>
>>> s.title()
'Python'
>>>
>>> s="my name is gaganam ramesh"
>>> print(s,type(s))
my name is gaganam ramesh <class 'str'>
>>> s.title()
'My Name Is Gaganam Ramesh'

#3.index()

>>> s="python"
>>> print(s,type(s))
python <class 'str'>
>>> s.index("t")
2
>>> s.index('o')
4
>>> s="my name is ramesh"
>>> s.index("a")
4
>>> s.index(y)
            ^
>>> s.index("y")
1
>>> s.index('h')
16

#4.upper()
>>> s='hare rama hare krishna jai ganesha'
>>> print(s,type(s))
hare rama hare krishna jai ganesha <class 'str'>
>>> s.upper()
'HARE RAMA HARE KRISHNA JAI GANESHA'


#5.lower()
>>> s.lower()
'hare rama hare krishna jai ganesha'
>>>
>>> s="Hello  How Are YOUR nAMe IS WhaT"
>>> s.lower()
'hello  how are your name is what'
>>>> s="IAM THE PERSON IN THE WORLD TO INTILLEGENT"
>>> print(s,type(s))
IAM THE PERSON IN THE WORLD TO INTILLEGENT <class 'str'>
>>> s.lower()
'iam the person in the world to intillegent'

#6.isupper() and 7.islower()
>>> s="Python"
>>> s.islower()
False
>>>
>>> s="python is programing language"
>>> s.islower()
True
>>>
>>> s='PYTHON'
>>> s.islower()
False
>>>
>>> s="SAMRAT PHONED"
>>> s.isupper()
True
>>> s="python is programing language"
>>> s="@#$%^&*!"
>>> s.islower()
False
>>> s.isupper()
False
>>> s.isupper()
False
>>> s="python is programing language"
>>> s.islower()
True
>>>
>>> There Is A Great PhilosPhEre
  File "<python-input-73>", line 1
    There Is A Great PhilosPhEre
          ^^
SyntaxError: invalid syntax
>>> s="There Is A Great PhilosPhEER"
>>> s.isupper()
False

#8.isalpha()
>>> s="python"
>>> s.isalpha()
True
>>>
>>> s="python123"
>>> s.isalpha()
False
>>> "1234"
'1234'
>>> s="1234"
>>> s.isalpha()
False
>>> s="   "
>>> s.isalpha()
False
>>> s="@#$%^&"
>>> s.isalpha()
False

#9.isdigit()
>>> s="python"
>>> s.isdigit()
False
>>> s="12345"
>>> s.isdigit()
True
>>> s="pytho123"
>>> s.isdigit()
False
>>> s="@#$%^&"
>>> s.isdigit()
False
>>> s=" "
>>> s.isdigit()
False

#10.isalnum()
>>> s="pytho1234"
>>> print(s,type(s))
pytho1234 <class 'str'>
>>> s.isalnum()
True
>>> s="12345"
>>> s.isalnum()
True
>>> s="rameshgaganam"
>>> s.isalnum()
True
>>> s="rameshgaganam12344@#$%^"
>>> s.isalnum()
False
>>> s="rameshgaganam987643"
>>> s.isalnum()
True

#11.split()
>>> #split()
>>> s="python is opp language"
>>> print(s)
python is opp language
>>> s.split()
['python', 'is', 'opp', 'language']
>>> s.split("-")
['python is opp language']
>>> s.split("_")
['python is opp language']
>>>  s="python is opp language"
