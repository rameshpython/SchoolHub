#List Datatype :
>>> #list Datatypes
>>> list=[10,10.5,'durga',True,10]
>>> print(list)
[10, 10.5, 'durga', True, 10]
>>> list=[10,20,30,40]
>>> list[0]
10
>>> list[-1]
40
>>> list[1:3]
[20, 30]
>>> list[0]=100
>>> for i in list:
...     print(i)
...
100
20
30
40
>>>
>>> list=[10,20,30]
>>> list.append("durga")
>>> print(list)
[10, 20, 30, 'durga']
>>>
>>> list.remove(20)
>>> print(list)
[10, 30, 'durga']
>>>
>>> list2=list*2
>>> print(list2)
[10, 30, 'durga', 10, 30, 'durga']
>>> list2=list*3
>>> print(list2)
[10, 30, 'durga', 10, 30, 'durga', 10, 30, 'durga']
>>> #NOTE:An ordered,mutable,heterogenous collection of elements is nothing but list,where dublicates also allowed.
>>> #list is growable in nature based on our requirement we can increase or decrease the size.
print("-------------------------------------------------")
lst1=[10,20,30,40,10,20,40,10,60,70,1.2]
print(lst1,type(lst1))
lst2=[10,"rossum",45.67,True,2+3j]#Given hetrogeneous type values to list(means multi types of datatypes added in one place,it is in list type.
print(lst2,type(lst2))
print("----------------------------")
lst2=[100,"Rossum",45.67,True,2+3j]
print(lst2,type(lst2),id(lst2))
lst2[0]
lst2[-1]
lst2[0:4]
lst2[0]=1000
print(lst2,type(lst2),id(lst2))
print('--------------------------')
>>> lst=[10,"Rs",34.56,True]
>>> print(lst,type(lst))
[10, 'Rs', 34.56, True] <class 'list'>
>>> lst[::2]
[10, 34.56]
>>> lst[::2]=[100,45.67]
>>> print(lst)
[100, 'Rs', 45.67, True]
>>>
>>> #Empty list[]
>>> lst1=[]
>>> print(lst1,type(lst1))
[] <class 'list'>
>>> len(lst1)
0
>>> lst1=lst()
Traceback (most recent call last):
  File "<python-input-34>", line 1, in <module>
    lst1=lst()
TypeError: 'list' object is not callable
>>>
print("----------------------------")
s="PYTHON"
print(s,type(s))
lst1=list(s)
print(lst1,type(lst1))
len(lst1)

s="PYTHON"
lst=list([s])
print(lst,type(lst))

a=10
print(a,type(a))
lst1=list([a])
print(lst1,type(lst1))

lst1=list(a)
print(lst1)#TypeError: 'int' object is not iterable(means no more than one value)

