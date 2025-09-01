#bytes Datatype :
>>> #Datatypes :
>>> #Examples :
>>> lst=[100,0,123,235,221,134,176,231,245]
>>> print(lst,type(lst))
[100, 0, 123, 235, 221, 134, 176, 231, 245] <class 'list'>
>>> b=bytes(lst)
>>> print(b)
b'd\x00{\xeb\xdd\x86\xb0\xe7\xf5'
>>>
>>> lst=[100,0,123,235,221,134,176,231,245]
>>> print(lst,type(lst))
[100, 0, 123, 235, 221, 134, 176, 231, 245] <class 'list'>
>>>
>>> lst=[100,200,233,145,176,299,232]
>>> print(lst,type(lst))
[100, 200, 233, 145, 176, 299, 232] <class 'list'>
>>> print(bytes(lst))
Traceback (most recent call last):
  File "<python-input-12>", line 1, in <module>
    print(bytes(lst))
          ~~~~~^^^^^
ValueError: bytes must be in range(0, 256)
>>> lst=[100,0,156,199,255,123,248,167]
>>> print(lst,type(lst))
[100, 0, 156, 199, 255, 123, 248, 167] <class 'list'>
>>> b=bytes(lst)
>>> print(b)
b'd\x00\x9c\xc7\xff{\xf8\xa7'
>>> print(b,type(b))
b'd\x00\x9c\xc7\xff{\xf8\xa7' <class 'bytes'>
>>>
>>> for val in b:
...     print(val)
...
100
0
156
199
255
123
248
167
>>> for val in b[::-1]
  File "<python-input-20>", line 1
    for val in b[::-1]
                      ^
SyntaxError: expected ':'
>>> for val  in b[::-1]:
...
...
...     print(val)
...
167
248
123
255
199
156
0
100
>>> for val in b[2:6]:
...     print(val)
...
156
199
255
123
>>> for val in  b[3:7]:
...     print(val)
...
199
255
123
248
>>> b[0]
100
>>> b[7]
167
>>> b[5]
123
>>> b[0]
100
>>> b[0]
100
>>> b[100]
Traceback (most recent call last):
  File "<python-input-29>", line 1, in <module>
    b[100]
    ~^^^^^
IndexError: index out of range
>>> b[0]=144
Traceback (most recent call last):
  File "<python-input-30>", line 1, in <module>
    b[0]=144
    ~^^^
TypeError: 'bytes' object does not support item assignment
>>> #TypeError:'bytes'objects does not support item assignment.
>>>
>>>
>>> lst=[100,232,165,187,145,249,276]
>>> print(lst,type(lst))
[100, 232, 165, 187, 145, 249, 276] <class 'list'>
>>> b=bytes(lst)
Traceback (most recent call last):
  File "<python-input-36>", line 1, in <module>
    b=bytes(lst)
ValueError: bytes must be in range(0, 256)
>>>
>>> #ValueError becoz bytes must be in range (0,256)
>>>























