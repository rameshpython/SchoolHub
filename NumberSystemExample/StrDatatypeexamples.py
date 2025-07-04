#str datatype examples :
>>> s="PYTHON"
>>> s[0]
'P'
>>> s[1]
'Y'
>>> s[5]
'N'
>>> s[3]
'H'
>>> s[2]
'T'
>>> s[4]
'O'
>>> s[10]
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    s[10]
    ~^^^^
IndexError: string index out of range
>>>
>>> s="PYTHON"
>>> s[-1]
'N'
>>> s[-6]
'P'
>>> s[-3]
'H'
>>> s[-2]
'O'
>>> s[-4]
'T'
>>> s[-5]
'Y'
>>> s[-12]
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    s[-12]
    ~^^^^^
IndexError: string index out of range
>>> #slicing of strings
>>> s="PYTHON"
>>> #case 1:
>>> s[0:5]
'PYTHO'
>>> s[2:5]
'THO'
>>> s[4:2]
''
>>> s[3:6]
'HON'
>>> s[1:4]
'YTH'
>>> s[3:5]
'HO'
>>> s[2:3]
'T'
>>>
>>> #case 2:
>>> s="PYTHON"
>>> s[-6:-2}
  File "<python-input-30>", line 1
    s[-6:-2}
           ^
SyntaxError: closing parenthesis '}' does not match opening parenthesis '['
>>> s[-6:-2]
'PYTH'
>>> s[-5:-1]
'YTHO'
>>> s[-3:-1]
'HO'
>>> s[-1:-3]
''
>>> s[-3:-2]
'H'
>>> s[-6:-4]
'PY'
>>>
>>> #case 3:
>>> s="PYTHON"
>>> 
'YTHO'
>>> s[2:-4]
''
>>> s[2:-1]
'THO'
>>> s[0:-2]
'PYTH'
>>> s[0:-5]
'P'
>>> s[0:-5]
'P'
>>> s[0:-6]
''
>>>
>>> case 4:
  File "<python-input-48>", line 1
    case 4:
         ^
SyntaxError: invalid syntax
>>> #case 4
>>> s="PYTHON"
>>> s[:]
'PYTHON'
>>> s="PYTHON PROG"
>>> s[:]
'PYTHON PROG'
>>>
>>> #syntax 5:
>>>
>>> s="PYTHON"
>>> s[0:6]
'PYTHON'
>>> s[0:6:2]
'PTO'
>>> s[1:6:3]
'YO'
>>> s[0::4]
'PO'
>>> s[0::5]
'PN'
>>> s[3:6:2]
'HN'
>>> s[0:6:4]
'PO'
>>> s[3:6:1]
'HON'
>>> s[4:2:2]
''
>>>
s[6:3:2]

#More examples :
>> #how  to  create string in python
>>> name="Ramesh"
>>> print(name)
Ramesh
>>>
>>> #multi string
>>> message="""Hello,
... This  is multi_line
... string examples.
... we are using in python"""
>>> print(message)
Hello,
This  is multi_line
string examples.
we are using in python
>>>
>>> #string concatenation
>>> string concatenation means joing two or more strings together using + operator
  File "<python-input-9>", line 1
    string concatenation means joing two or more strings together using + operator
           ^^^^^^^^^^^^^
SyntaxError: invalid syntax
>>> # string concatenation means joing two or more strings together using + operator
>>> #Example:
>>> first_name="Ramesh"
>>> last_name="Babu"
>>> full_name=first_name+"   "+last_name
>>> print(full_name)
Ramesh   Babu
>>>
>>> greeting="Hello"
>>> name="sita"
>>> message=greeting+" "+name+!
  File "<python-input-19>", line 1
    message=greeting+" "+name+!
                              ^
SyntaxError: invalid syntax
>>> message=greeting+" "+name
>>> print(message)
Hello sita
>>>
>>> #Access a character
>>> Word="python"
>>> print(Word[3])
h
>>> print(Word[6])
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    print(Word[6])
          ~~~~^^^
IndexError: string index out of range
>>> print(Word[5])
n
>>>
>>> #slicing
>>> word="python"
>>> print(word[1:5])
ytho
>>> print(word[2:6])
thon
>>> print(word[2:4:6])
t
>>> print(word[1:6:3])
yo
>>>
>>> #upper()
>>> #convert "there is a beautiful rose in garden"
>>> text= "there is a beautiful rose in garden"
>>> print(text.upper())
THERE IS A BEAUTIFUL ROSE IN GARDEN
>>>
>>> #lower()
>>> text="THERE IS A BEAUTIFUL ROSE IN THE GARDEN"
>>> print(text.lower())
there is a beautiful rose in the garden
>>>
>>> #replace()
>>> text="Hello world"
>>> print(text.replace("world","garden"))
Hello garden
>>> print(text.replace("Hello","My"))
My world
>>> print(text.replace("My world","Your place"))
Hello world
>>>
>>> print(text.replace("Hello world","Nick name"))
Nick name
>>> print(text)
Hello world
>>>
>>> #split()
>>> #how to split a sentence into words
>>> sentence="All the country people are together to find rocket"
>>> print(sentence.split())
['All', 'the', 'country', 'people', 'are', 'together', 'to', 'find', 'rocket']
>>>
>>> sentence="python is fun"
>>> print(sentence.split())
['python', 'is', 'fun']
>>>
>>> #strip()
>>> #Remove white or empty spaces from start and end in strins.it removves spaces,tabs ans (\t)and newline(\n)from both sides .
>>> text="    Hello world     "
>>> print(text.strip())
Hello world
>>>
>>> text=###Welcome###
  File "<python-input-67>", line 1
    text=###Welcome###
         ^^^^^^^^^^^^^
SyntaxError: invalid syntax
>>> text="###Welcome###"
>>> print(text.strip(#))
... print(text.strip())
...
... text="\n\tHello world\n\t"
... print(text.strip())
...
  File "<python-input-69>", line 1
    print(text.strip(#))
                    ^
SyntaxError: '(' was never closed
>>> print(text.strip( ))
###Welcome###
>>> print(text.strip(#))
...
... text="\n\tHello\n\t"
... print(text.strip( ))
...
  File "<python-input-71>", line 1
    print(text.strip(#))
                    ^
SyntaxError: '(' was never closed
>>> print(text.strip())
###Welcome###
>>>
>>> #what will len("python")
>>> s="python"
>>> len(s)
6
>>> #or
>>> len("python")
6
>>>


































































































