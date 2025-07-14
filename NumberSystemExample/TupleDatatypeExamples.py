#pre-defined functio in tuple
#Examples :
t1=(10,"Rs",45.67)
print(t1,type(t1))
t1.index(10)
t1.index("Rs")

t1.count(10)
t1.count(45.67)
t1.count(100)

t1=(10,20,30,40,10,20,30,10,20)
print(t1,type(t1))
t1.count(10)
t1.count(20)
t1.count(50)

#Deep copy and shallow copy
t1=(10,20,30,40,50,20,10)
print(t1,type(t1))
t2=t1#Deep copy not shallow copy becoz tuple is immutable(not changeable of values)
print(t2,type(t2),id(t2))
t3=t1
print(t3,type(t3),id(t3))
t3=tuple(sorted(t1))
#t3.sort()
x=tuple(sorted(t1))
print("-------------------")
t1=(10,23,-56,-32,13,54,98,6,-2)
print(t1,type(t1))
#t1.sort()----------------------AttributeError: 'tuple' object has no attribute 'sort'
t2=sorted(t1)
print(t2,type(t2))
x=sorted(t1)
print(x,type(x))
t1=tuple(x)
t2=t1[::-1]
print(t2,type(t2))
print("---------------------------------")
t1=(10,23,-56,-32,13,54,98,6,-2)
print(t1,type(t1))
x=sorted(t1)
print(x,type(x))
#t1=sort()
t2=sorted(t1)
print(t2,type(t2))
t1=tuple(x)
t2=t1[::-1]
print(t2,type(t2))
t2=t1[::1]
print(t2,type(t2))
t2=tuple(sorted(t1,reverse=True))
print(t2,type(t2))
t2=tuple(sorted(t1)[::-1])
print(t2,type(t2))

t2=tuple(sorted(t1)[::1])
print(t2,type(t2))

print("--------------------")
t1=(10,23,-56,-32,13,54,98,6,-2)
l1=list(t1)
print(l1,type(l1))
l1.sort()
print(l1,type(l1))
t1=tuple(l1)
print(t1,type(t1))
#t1.sort()#AttributeError: 'tuple' object has no attribute 'sort'
#print(t1,type(t1))
t1=t1[::-1]
print(t1,type(t1))
t1=t1[::1]
print(t1,type(t1))













