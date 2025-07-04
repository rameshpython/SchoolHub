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
>>> s[1:-1]
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

























































































