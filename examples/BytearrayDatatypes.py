#Bytearray Datatype:
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
>>> #bytearray
>>> lst=[100,0,134,156,126,187,255,167]
>>> print(lst,type(lst))
[100, 0, 134, 156, 126, 187, 255, 167] <class 'list'>
>>> b=bytearray(lst)
>>> print(b)
bytearray(b'd\x00\x86\x9c~\xbb\xff\xa7')
>>>
>>> b[6]
255
>>> b[6]=245
>>> print(b)
bytearray(b'd\x00\x86\x9c~\xbb\xf5\xa7')
>>> print(lst)
[100, 0, 134, 156, 126, 187, 255, 167]
>>>
>>> lst=[100,0,156,233,187,255,178,167]
>>> print(lst,type(lst))
[100, 0, 156, 233, 187, 255, 178, 167] <class 'list'>
>>> b=bytearray(lst)
>>> print(b,type(b))
bytearray(b'd\x00\x9c\xe9\xbb\xff\xb2\xa7') <class 'bytearray'>
>>> for val in b:
...
...
...     print(val)
...
100
0
156
233
187
255
178
167
>>> b[0]
100
>>> b[1]
0
>>> b[2]
156
>>> b[7]
167
>>> b[8]
Traceback (most recent call last):
  File "<python-input-60>", line 1, in <module>
    b[8]
    ~^^^
IndexError: bytearray index out of range
>>> b[6]
178
>>> b[1]=200
>>> b[0]=201
>>> b[2]=202
>>> b[-1]=203
>>> b[-2]=204
>>> for val in b:
...     print(vaL)
...
Traceback (most recent call last):
  File "<python-input-67>", line 2, in <module>
    print(vaL)
          ^^^
NameError: name 'vaL' is not defined. Did you mean: 'val'?
>>>
>>>
>>>
>>> lst=[100,132,0,56,24,178,198,288,167]
>>> print(lst,type(lst))
[100, 132, 0, 56, 24, 178, 198, 288, 167] <class 'list'>
>>> b=bytearray(lst)
Traceback (most recent call last):
  File "<python-input-73>", line 1, in <module>
    b=bytearray(lst)
ValueError: byte must be in range(0, 256)
>>> #ValueError becoz bytearray range is (0,256)
>>>  lst=[100,0,156,233,187,255,178,167]
  File "<python-input-75>", line 1
    lst=[100,0,156,233,187,255,178,167]
IndentationError: unexpected indent
>>>
>>> lst=[100,0,156,233,187,255,178,167]
>>> print(lst,type(lst),id(lst))
[100, 0, 156, 233, 187, 255, 178, 167] <class 'list'> 1259380163904
>>> b=bytearray(lst)
>>> print(b,type(b),id(b))
bytearray(b'd\x00\x9c\xe9\xbb\xff\xb2\xa7') <class 'bytearray'> 1259380165040
>>> for val  in b:
...     print(val)
...
100
0
156
233
187
255
178
167
>>> b[0]=100
>>> b[0]=200
>>> for val in b:
...
...
...     print(val)
...
200
0
156
233
187
255
178
167
>>> b[0]=201
>>> b[1]=202
>>> b[2]=203
>>> for val in b:
...     print(val)
...
201
202
203
233
187
255
178
167
>>> print(b,type(b),id(b))
bytearray(b'\xc9\xca\xcb\xe9\xbb\xff\xb2\xa7') <class 'bytearray'> 1259380165040
>>> for val in b:
...
...     print(val)
...
201
202
203
233
187
255
178
167
>>> print(b,id(b))
bytearray(b'\xc9\xca\xcb\xe9\xbb\xff\xb2\xa7') 1259380165040
>>> #bytearray is 'MUTABLE'becoz the value change and assign to the variable again in the range (0,256) olny.
>>>










