#Membership Operators
#we can use membership operators to check whether the given object is present in the given collection.
#It may be string,list,set,Tuple or Dict

#in -->Returns True if the given object present  in the specified collection
#not in -->Returns True if the given object not present in the  specified collection

x="hello learning python is very easy!!!"
print('h' in x)
print('d' in x)
print('o' in x)
print('d' not in x)
print('python' in x)
print('z' in x)

list1=("sunny","bunny","cherry","curry")
print("sunny" in list1)
print("munny" in list1)
print('h' in list1)
print("s" in list1)
print("kanni" in list1)

#Examples
s="PYTHON"
print(s)
print("P" in s)
print("N" in s)
print("K" in s)
print("K" not in s)
print("N" not in s)

print("--------------------------------")

s="PYTHON"
print(s)
print("PYT" in s)
print("PYT" not in s)
print("PTO" in s)
print("PTO" not in s)
print("NOH" in s)
print("NOH" in s[::-1])

print("---------------------------------")

lst=[100,"Rossum",23.45,2+3j]
print(lst)
"sum" in lst
"sum" not in lst
"sum" in lst[1]
"mus" in lst[1]
"mus" in lst[1][::-1]

#2.0 in lst[-1]--------------------TypeError: argument of type 'complex' is not iterable
#3.0 in lst[-1].imag------------TypeError: argument of type 'float' is not iterable

print("--------------------------------------")

lst=[100,"Rossum",23.45,2+3j]
print(lst)
[100,"Rosum"] in lst
lst=[[100,"Rossum"],23.45,2+3j]
print(lst)
[100,"Rossum"] in lst

print("-----------------------------------------------------------------------------------------------")

d1={10:"Python",20:"DSA",30:"HTML"}
print(d1)
"Python" in d1
#{10:"Python"} in d1#TypeError: unhashable type: 'dict'
(10,"Python") in d1.items()
"Python" not in d1.values()
"thon" in d1[10]
#d1 in d1------------------------------------TypeError: unhashable type: 'dict'

print("----------------------------------------------------------------------------------------------------")

#Operator precedence -->precedence means priority or importance in order
#operator precedence means the order in which operators are performed when an expression has more than one operator

#Example
a=30
b=20
c=10
d=5
print((a+b)*c/d)
print((a+b)*(c/d))
print(a+(b*c)/d)

print(3/2*4+3+(10/5)**3-2)


