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

#8.enumarate()
#Examples :
lst=[10,20,30,10,20,30,10,20]
print(lst)
for index,value in enumerate(lst):
    print(index,"--->",value)
print("---------------")

for index,value in enumerate(lst):
    if(value==10):
            print(index,"--->",value)
print("-------------")
for index,value in enumerate(lst):
        if(value==20):
            print(index,"--->",value)
print("-------------")
for index,value in enumerate(lst):
    if(value==30):
        print(index,"--->",value)

#9.count()
#Examples :
lst=[10,20,30,10,20,30,40,20,10]
print(lst)
lst.count(10)
print(lst)
lst.count(20)
lst.count(30)
lst.count(40)
#lst.cout(50)#AttributeError: 'list' object has no attribute 'cout'. Did you mean: 'count'?
print(lst)

#lst("1234567")#TypeError: 'list' object is not callable.it is in string
#lst.count(1)
#lst.count('1')
print("-------------------------")
#10.copy()
lst1=[10,"Rossum",23.45]
print(lst1,id(lst1))
lst2=lst1.copy()#shallow copy
print(lst2,id(lst2))
lst1.append("NL")
lst2.insert(1,"HYD")
print(lst1,id(lst1))
print(lst2,id(lst2))
print("--------------------")
lst1=[10,"Rossum",23.56]
print(lst1,id(lst1))
ls2=lst1#Deep copy
print(lst2,id(lst2))
lst1.append("NL")
print(lst1,id(lst1))
print(lst2,id(lst2))
lst2.insert(0,"kol")
print(lst1,id(lst1))
print(lst2,id(lst2))

#11.reverse()
lst1=[10,20,12,"python",True,2+3j]
print(lst1,id(lst1))
lst2=lst1.reverse()
print(lst2,id(lst2))
lst1.reverse()
print(lst1,id(lst1))

lst=[1,3,6,-1,-0,11]
print(lst)
lst.reverse()
print(lst)

#12.sort()
lst1=[10,4,15,16,6,11,22,-2]
print(lst1,id(lst1))
lst1.sort()#sor means Assending order forming
print(lst1,id(lst1))
lst1.reverse()
print(lst1,id(lst1))
print("------------")
#lst1=[10,20,12,True,2+3j]#TypeError: '<' not supported between instances of 'complex' and 'int'
#print(lst1)
#lst1.sort()

lst1=[10,4,15,16,6,11,22,-2]
print(lst1)
lst1.sort(reverse=True)
print(lst1)
lst1.sort(reverse=False)
print(lst1)

#13.extend
lst1=[10,20,30]
lst2=["RS","TR","DR"]
print(lst1)
print(lst2)
lst1.extend(lst2)
print(lst1)
print(lst2)
lst2.extend(lst1)
print(lst2)

lst1=[10,20,30]
lst2=["RS","TR","DR"]
lst3=[1,2,3,4,5,6,7,8]
#lst1=extend(lst2,lst3)#NameError: name 'extend' is not defined
lst1.extend(lst2)
lst1.extend(lst3)
print(lst1)
print("------------------")
#meging multiple list elements in single line by using + operator
lst1=[10,20,30]
lst2=["RS","TR","DR"]
lst3=[1,2,3,4,5,6,7,8]
print(lst1,id(lst1))
lst1=lst1+lst2+lst3
print(lst1,id(lst1))



















    








