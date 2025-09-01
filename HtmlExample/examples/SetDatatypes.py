s1={10,20,30,40,50,60,70,10,20}
print(s1,type(s1))
#s1[0]---------------------------------TypeError: 'set' object is not subscriptable
#s1[0:3]------------------------------TypeError: 'set' object is not subscriptable
for index,value in enumerate(s1):
		print(index,"-->",value)
print("----------------------------")
s1={10,20,30,40,50,60,70,10,20}
print(s1,type(s1),id(s1))
#s1[0]=100#TypeError: 'set' object does not support item assignment

s1.add("HYD")
print(s1,type(s1),id(s1))
s1.remove(40)
print(s1,type(s1),id(s1))
print("----------------------------")
s1=set()
print(s1,type(s1))
len(s1)
print("----------------------")

s="PYTHON"
s1=set(s)
print(s1,type(s1))

print("-----------------------------")
a=10
#s=set(a)#TypeError: 'int' object is not iterable

s=set([a])
print(s,type(s))
s=set((a,))
print(s,type(s))
len(s)


print("-----------------------------")
>>> s={100,20,30,40,0,200,10,'durga'}
>>> s[0]
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    s[0]
    ~^^^
TypeError: 'set' object is not subscriptable
>>> s.add(50)
>>> print(s)
{0, 100, 40, 200, 10, 'durga', 50, 20, 30}
>>> print(s,type(s))
{0, 100, 40, 200, 10, 'durga', 50, 20, 30} <class 'set'>
>>> s.remove(100)
>>> print(s,type(s))
{0, 40, 200, 10, 'durga', 50, 20, 30} <class 'set'>
>>> s.insert(1,500)
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    s.insert(1,500)
    ^^^^^^^^
AttributeError: 'set' object has no attribute 'insert'
>>> s={100,20,30,40,0,200,100,10,'durga'}
>>> print(s,type(s))
{0, 100, 40, 200, 10, 'durga', 20, 30} <class 'set'>
>>>  s={10,20,30,40,50,60,70,20,10}
  File "<python-input-10>", line 1
    s={10,20,30,40,50,60,70,20,10}
IndentationError: unexpected indent
>>> s={10,20,30,40,50,60,70,20,10}
>>> print(s,type(s))
{50, 20, 70, 40, 10, 60, 30} <class 'set'>
>>> s1={10,"Rossum",True,45.67,2+3j}
>>> print(s1,type(s1))
{True, 'Rossum', 10, (2+3j), 45.67} <class 'set'>
>>> print("---------------------------")
---------------------------
>>> s[0]
Traceback (most recent call last):
  File "<python-input-16>", line 1, in <module>
    s[0]
    ~^^^
TypeError: 'set' object is not subscriptable
>>> s[1:3]
Traceback (most recent call last):
  File "<python-input-17>", line 1, in <module>
    s[1:3]
    ~^^^^^
TypeError: 'set' object is not subscriptable
>>> s={10,20,30,40,50,60,70,20,10}
>>> print(s)
{50, 20, 70, 40, 10, 60, 30}
>>> s={10,20,30,40,50,60}
>>> print(s)
{50, 20, 40, 10, 60, 30}
>>> s={10,20,30,40,50,60,70,20,10}
>>> print(s,type(s))
{50, 20, 70, 40, 10, 60, 30} <class 'set'>
>>> for index,value in enumerate(s):
...     print(index,"--->",value)
...
0 ---> 50
1 ---> 20
2 ---> 70
3 ---> 40
4 ---> 10
5 ---> 60
6 ---> 30
>>>
>>> s[2]=50
Traceback (most recent call last):
  File "<python-input-26>", line 1, in <module>
    s[2]=50
    ~^^^
TypeError: 'set' object does not support item assignment
>>> s.add("ramesh")
>>> print(s)
{50, 20, 70, 40, 10, 60, 'ramesh', 30}
>>> s.remove(30)
>>> print(s)
{50, 20, 70, 40, 10, 60, 'ramesh'}
>>> s.insert(3,76)
Traceback (most recent call last):
  File "<python-input-31>", line 1, in <module>
    s.insert(3,76)
    ^^^^^^^^
AttributeError: 'set' object has no attribute 'insert'
>>> s=set()
>>> print(s,type(s))
set() <class 'set'>
>>> len(s)
0
>>> s1={10,"Rossum",True,45.67,2+3j}
>>> print(s1,type(s1))
{True, 'Rossum', 10, (2+3j), 45.67} <class 'set'>
>>> s1[1]
Traceback (most recent call last):
  File "<python-input-37>", line 1, in <module>
    s1[1]
    ~~^^^
TypeError: 'set' object is not subscriptable
>>> s1[2]
Traceback (most recent call last):
  File "<python-input-38>", line 1, in <module>
    s1[2]
    ~~^^^
TypeError: 'set' object is not subscriptable
>>> s1[1]="ramesh"
Traceback (most recent call last):
  File "<python-input-39>", line 1, in <module>
    s1[1]="ramesh"
    ~~^^^
TypeError: 'set' object does not support item assignment
>>> for index,value in enumerate(s):
...     print(index,"----->",value)
...
>>>
>>>  for index,value in enumerate(s1):
  File "<python-input-42>", line 1
    for index,value in enumerate(s1):
IndentationError: unexpected indent
>>> s1.add("gaganamramesh")
>>> print(s1,type(s1))
{True, 'Rossum', 'gaganamramesh', 10, (2+3j), 45.67} <class 'set'>
>>> s1.remove(45.67)
>>> print(s1,type(s1))
{True, 'Rossum', 'gaganamramesh', 10, (2+3j)} <class 'set'>
>>>






