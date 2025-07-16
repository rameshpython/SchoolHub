#Set Datatpes 
#Pre-Defined functions in set with Examples :
#1. add()
s1={10,"RS",34.56}
print(s1,type(s1),id(s1))
s1.add(100)
print(s1,type(s1),id(s1))
s1.add("NL")
s1.add("PYTHON")
print(s1,type(s1),id(s1))
print("------------------")
#2. remove()
s1={'NL', 34.56, 100, 10, 'RS', 'PYTHON'}
print(s1,type(s1),id(s1))
s1.remove(100)
print(s1,type(s1),id(s1))
s1.remove(10)
print(s1,type(s1),id(s1))
s1.remove("PYTHON")
print(s1,type(s1),id(s1))
#s1.remove(100)
#set().remove(100)---------------------------KeyError: 100
#list().remove(100)---------------------------ValueError: list.remove(x): x not in list
print("---------------------")
#3.  discard()
s1={'NL', 34.56, 100, 10, 'RS', 'PYTHON'}
print(s1,type(s1),id(s1))
s1.discard(100)
print(s1,type(s1),id(s1))
s1.discard("RS")
print(s1,type(s1),id(s1))
s1.discard(10)
print(s1,type(s1),id(s1))
s1.discard(100)
set().discard(10)
#set().remove(10)-----------------------------KeyError: 10
print("----------------------")
#4. pop()
s1={10,20,30,40,50,60,70,15}
s1.pop()-----------70
s1.pop()-----------40
s1.pop()-----------10
s1.pop()-----------15
s1.pop()-----------50

s1={'NL', 34.56, 100, 10, 'RS', 'PYTHON'}
print(s1)
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
print(s1,type(s1),id(s1))
#s1.pop()------------------------KeyError: 'pop from an empty set'
#list().pop()--------------------IndexError: pop from empty list
print("-------------------")
#5. clear()
s1={10,20,30,40,50,60,70,15}
print(s1)
len(s1)
s1.clear()
print(s1)
print(s1.clear())
s1.clear()
print(set().clear())
print("-----------------------")
#6. copy()
s1={10,20,30,40}
print(s1,id(s1))
s2=s1.copy()
print(s2,id(s2))
s1.add(100)
s2.add(12.34)
print(s1,id(s1))
print(s2,id(s2))

s3=s1 # Deep Copy
print(s3,id(s3))
s3.remove(40)
print(s1,id(s1))
print(s3,id(s3))

#NOTE: del operator with set object
#del s1[0]#TypeError: 'set' object doesn't support item deletion
#del s1[0:2]#TypeError: 'set' object does not support item deletion
del s1
print(s2)

print("----------------------")

#7. isdisjoint()
s1={10,20,30,40}
s2={10,15,25,35}
s3={3,4,5,6}
s1.isdisjoint(s2)#----------False
s1.isdisjoint(s3)#----------True
s2.isdisjoint(s3)#----------True

set().isdisjoint(set())#------------------True
set().isdisjoint({10,20,30})#----------True
{10,20,30}.isdisjoint(set())#----------True

#8. issuperset()
s1={10,20,30,40}
s2={20,30}
s3={30,45,15}
s1.issuperset(s2)#--------------True
s2.issuperset(s1)#--------------False
s2.issuperset(s3)#--------------False
s1.issuperset(s3)#--------------False

set().issuperset(set())#----------True
{10,20,30}.issuperset(set())#----True
set().issuperset({10,20,30})#----False

#9. issubset()
s1={10,20,30,40}
s2={20,30}
s3={30,45,15}
s2.issubset(s1)#--------------True
s1.issubset(s2)#--------------False
s3.issubset(s2)#--------------False
s3.issubset(s1)#--------------False
set().issubset(set())#---------------True
set().issubset({10,20,30})#-------True

#10. union()
s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))#-----------------{40, 10, 20, 30} <class 'set'>
print(s2,type(s2))#-----------------{50, 20, 30, 60} <class 'set'>
s3=s1.union(s2)
print(s3,type(s3))#------------------{40, 10, 50, 20, 60, 30} <class 'set'>
s4=s1.union(s2,{1,2,3,4})
print(s4,type(s4))#-------------------{1, 2, 3, 4, 40, 10, 50, 20, 60, 30} <class 'set'>

#11. intersection()
s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))#-----------------{40, 10, 20, 30} <class 'set'>
print(s2,type(s2))#-----------------{50, 20, 30, 60} <class 'set'>
s3=s1.intersection(s2)
print(s3,type(s3))#-----------------{20, 30} <class 'set'>
s4=s1.intersection(s2,{1,2,3,4})
print(s4,type(s4))#---------set() <class 'set'>
{10,20,30}.intersection({1,2,3,4})#-----------set()

#12. difference()
s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))#-----------------{40, 10, 20, 30} <class 'set'>
print(s2,type(s2))#-----------------{50, 20, 30, 60} <class 'set'>
s3=s1.difference(s2)
print(s3,type(s3))#--------------{40, 10} <class 'set'>
s4=s2.difference(s1)
print(s4,type(s4))#--------------{50, 60} <class 'set'>
{10,20,30}.difference({10,20,30})#----------set()
{10,20,30}.difference({1,2,3})#--------------{10, 20, 30}

#13. symmetric_difference()  ( InMaths--It is Called Delta Operation )
#Formula1:  setobj1.symmetric_difference(setobj2) =>setobj1.union(setobj2) .difference(setobj1.intersection(setobj2) )
#Formula2: setobj1.symmetric_difference(setobj2) =>(setobj1.difference(s2)) .union (setobj2.difference(s1) )
s1={10,20,30,40}
s2={20,30,50,60}
print(s1,type(s1))#-----------------{40, 10, 20, 30} <class 'set'>
print(s2,type(s2))#-----------------{50, 20, 30, 60} <class 'set'>
s3=s1.symmetric_difference(s2)
print(s3,type(s3))#--------------------{40, 10, 50, 60} <class 'set'>
{10,20,30}.symmetric_difference({10,20,30})#--------set()
set().symmetric_difference({10,20,30})#----------------{10, 20, 30}
#			By Formula-1
s1={10,20,30,40}
s2={20,30,50,60}
s3=s1.union(s2).difference(s1.intersection(s2))
print(s3,type(s3))#-------------------------{40, 10, 50, 60} <class 'set'>
#			By Formula-2
s1={10,20,30,40}
s2={20,30,50,60}
s3=(s1.difference(s2)).union(s2.difference(s1))
print(s3,type(s3))#--------------{40, 10, 50, 60} <class 'set'>

#14. update()
s1={10,20,30,40}
s2={15,25,35}
print(s1,id(s1))#---------------{40, 10, 20, 30} 3006140867840
s3=s1.update(s2)
print(s3)#--------------------None
print(s1,id(s1))#-----------{35, 20, 40, 25, 10, 30, 15} 3006140867840

s1={10,20,30,40}
s2={10,20,15,25}
s1.update(s2)
print(s1)#---------------------{40, 10, 15, 20, 25, 30}

s1={10,20,30,40}
s2={10,20,30,40}
s1.update(s2)
print(s1)#-------------{40, 10, 20, 30}

#15. intersection_update()
s1={10,20,30,40}
s2={20,30,25,35}
s1.intersection_update(s2)
print(s1)#-----------------{20, 30}
s1={10,20,30,40}
s2={1,2,3}
s1.intersection_update(s2)
print(s1)#----------------------set()

#16. difference_update()
s1={10,20,30,40}
s2={20,30,45,55}
s1.difference_update(s2)
print(s1)#------------------{40, 10}
s1={10,20,30,40}
s2={10,20,30,40,55}
s1.difference_update(s2)
print(s1)#----------------set()
s1={10,20,30,40}
s2={15,25}
s1.difference_update(s2)
print(s1)#---------------{40, 10, 20, 30}

#17. symmetric_difference_update()
s1={10,20,30,40}
s2={10,20,50,60}
s1.symmetric_difference_update(s2)
print(s1)#-------------------------{40, 50, 60, 30}
s1={10,20,30,40}
s2={10,20,30,40}
s1.symmetric_difference_update(s2)
print(s1)#-----------------set()







