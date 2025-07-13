#Tuple Datatypes :
t2=(100,'RS',45.67,True,2+3j)
print(t2,type(t2))
t2[0]
t2[1]
t2[-1]
t2[1]
t2[-1]
for val in t2:
    print(val)
print("-----------------------")
t1=(10,20,30,10,20,56,78,-12)
print(t1,type(t1))
print("-----------------------")
t2=(100,'RS',45.67,True,2+3j)
print(t2,type(t2))
t2[0]
t2[1]
t2[-1]
t2[1:4]
t2[::-1]
print("-----------------------")
t2=(100,'RS',45.67,True,2+3j)
print(t2,type(t2))
t2[0]
#t2[0]=1000#TypeError: 'tuple' object does not support item assignment
print("--------------------------")
t1=()
print(t1,type(t1))
len(t1)

t2=tuple()
print(t2,type(t2))
len(t2)

t1=(10,20,30,10,20,56,87,-32)
print(t1,type(t1))
len(t1)

t2=10,20,30,40,50,60,10,20
print(t2,type(t2))

t3=12.4,98.3,12.6,98.4,67.2
print(t3,type(t3))
print("--------------------")
t=(10)
print(t,type(t))

#t1=tuple(t)#TypeError: 'int' object is not iterable
#print(t1,type(t1))

t=(10,)
print(t,type(t))

x=("PYTHON")
print(x,type(x))

x=("PYTHON",)
print(x,type(x))

s=("python")
print(s,type(s))

t=tuple(s)
print(t,type(t))

t=tuple([s])
print(t,type(t))

a=10
print(a,type(a))

#t=tuple(a)#TypeError: 'int' object is not iterable
#print(t,type(t))

#t=tuple(a,)#TypeError: 'int' object is not iterable
#print(t,type(t))

t=tuple((a,))
print(t,type(t))

t=tuple([a,])
print(t,type(t))

a=1.2
print(a,type(a))

#t=tuple(a)#TypeError: 'float' object is not iterable
#print(t,type(t))

t=tuple((t,))
print(t,type(t))

t=tuple([t])
print(t,type(t))












