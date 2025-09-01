#List Datatype :
#list Datatypes
list=[10,10.5,'durga',True,10]
print(list)
[10, 10.5, 'durga', True, 10]
list=[10,20,30,40]
list[0]
list[-1]
list[1:3]
list[0]=100
for i in list:
  print(i)
list=[10,20,30]
list.append("durga")
print(list)
[10, 20, 30, 'durga']
list.remove(20)
print(list)
list2=list*2
print(list2)
[10, 30, 'durga', 10, 30, 'durga']
list2=list*3
print(list2)
#NOTE:An ordered,mutable,heterogenous collection of elements is nothing but list,where dublicates also allowed.
#list is growable in nature based on our requirement we can increase or decrease the size.
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
lst=[10,"Rs",34.56,True]
print(lst,type(lst))
lst[::2]
lst[::2]=[100,45.67]
print(lst)
#Empty list[]
lst1=[]
print(lst1,type(lst1))
len(lst1)
#lst1=lst()
#TypeError: 'list' object is not callable
print("----------------------------")
s="PYTHON"
print(s,type(s))
#lst1=list(s)
print(lst1,type(lst1))
len(lst1)

s="PYTHON"
#lst=list([s])
print(lst,type(lst))

a=10
print(a,type(a))
#lst1=list([a])
print(lst1,type(lst1))
print(lst1)#TypeError: 'int' object is not iterable(means no more than one value)
print("----------------------------------------------------------------------------------")
#Inner list OR Nested list
print("--------------------------------------------")
lst=[10,'Rossum', [30,35,25] ,  [70,65,60]  , 'JNTU'  ]
print(lst,type(lst))
for val in lst:
  print(val,"-->",type(val),"-->",type(lst))
print(lst,type(lst))
lst[2].append(38)
print(lst,type(lst))
lst[-2].insert(1,58)
print(lst,type(lst))
lst[-2][::3]
# i want merge inner list values and append to existing list
lst[2]+lst[3]
[30, 35, 25, 38, 70, 58, 65, 60]
print(lst)
lst.insert(-1,lst[2]+lst[3])
print(lst,type(lst))
print(lst)
lst[-2][1]=lst[-2][1]+lst[-2][1]*(50/100)
print(lst)
lst[-2][-2:]
lst[-2][-2:]=[lst[-2][2]+lst[-2][2]*50/100, lst[-2][3]+lst[-2][3]*60/100]
print(lst)
del lst[-2]
print(lst)
lst[-2].pop()
print(lst)
del lst[2:4]
print(lst)
lst.insert(-1,[10,30,50])
print(lst)
print("------------------------------")
lst=[[10,20,30],[40,50,60],[70,80,90]]
print(lst,type(lst))
for val in lst:
  print(val)

lst=[[[10,20,30],[40,50,60],[70,80,90]],[[1,2,3],[4,5,6],[7,8,9]]]
print(lst,type(lst))
for matrix in lst:
  print(matrix)
for matrix in lst:
  for row in matrix:
    print(row)













    

