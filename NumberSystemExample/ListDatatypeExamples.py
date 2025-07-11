#pre defined functions in List
#In list  we can perform the Following operations
#1.append()
#Examples :
lst=[10,"Rossum",37.45]
print(lst,type(lst),id(lst))
lst.append(True)
print(lst,id(lst))
lst.append(2+3j)
print(lst,id(lst))
lst.append(1000)
lst.append(234.987)
lst.append('ramesh')
print(lst,id(lst))
print("-------------------")
#2.insert()
#Examples :
lst=[10,"Rossum",37.45]
print(lst,id(lst))
lst.insert(3,'ramesh')
print(lst,id(lst))
lst.insert(1,'NL')
lst.insert(2,987)
lst.insert(0,1000)
print(lst,id(lst))
print("--------------------")
#3.remove()
#Examples :
lst=[10,20,30,40, 50, 60,20,10,70,80]
print(lst,id(lst))
lst.remove(20)
lst.remove(10)
lst.remove(20)
#lst.remove(20)#ValueError: list.remove(x): x not in list#Already 20 removed from list ,another time remove means get valueError
#because there is no more extra 20 number in list.
print(lst,id(lst))
#[].remove(30) inalid syntax
#lst().remove(40) inalid syntax
#lst[].remove(50) inalid syntax
print("---------------------")
#4.pop(index)___Based index.
#Examples :
lst=[10,20,30,40,10,20,30,40]
print(lst,id(lst))
lst.pop(-1)
print(lst,id(lst))
lst.pop(3)
print(lst,id(lst))
lst.pop(1)
print(lst,id(lst))
lst.pop(4)
print(lst,id(lst))

#5.pop()
#Examples :
lst=[10,20,30,40,"Python",True,2+3j]
print(lst,id(lst))
lst.pop()
print(lst,id(lst))
lst.pop()
print(lst,id(lst))
lst.pop()
print(lst,id(lst))
lst.pop(1)
print(lst,id(lst))
#[].pop()
#list[].pop()

#6.clear()
#Examples :
lst=[10,20,30,40,"Python",True,2+3j]
print(lst,id(lst))
len(lst)
print(lst,id(lst))
lst.clear()#we get empty list like []-->notation of list
print(lst,id(lst))
[].clear()
print(lst,id(lst))

#Delete operator
#Examples :
#syntax-1:
lst=[10,20,30,40]
print(lst)
del lst[2]
del lst[1]
del lst[0]
print(lst)
#syntax-2:
lst=[10,20,30,40,50,60,70,80]
print(lst)
del lst[2:4]
print(lst)
del lst[1:5]
print(lst)
lst=[10,20,30,40,50,60,70,80]
del lst[-2:2]
print(lst)
del lst[1:-3]
print(lst)
del lst[::2]
print(lst)
#del lst#NameError: name 'lst' is not defined. Did you mean: 'list'?
#print(lst)
#immutable object'str'
s="PYTHON"
#del s[0]TypeError: 'str' object doesn't support item deletion
#del s[0:4]TypeError: 'str' object does not support item deletion
del s
#print(s)

#7.index()
#Examples :
lst=[10,20,30,40,10,30,10,20]
print(lst)
[10, 20, 30, 40, 10, 30, 10, 20]
lst.index(10)
lst.index(30)
lst.index(10)
lst.index(10)
lst.index(40)

list=("mississippi")
list.index('i')
1
list.index('s')
2
list.index('p')
8
list=("123456")
print(list)
#list.index(1) TypeError: index() argument 1 must be str, not int
list.index('2')
print(list)








