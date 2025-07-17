#Frozenset Datatypes :
#Examples :
s1={10,20,30,10,20,60,70}
print(s1,type(s1))
fs1=frozenset(s1)
print(fs1,type(fs1))
s1={10,"RS",33.33,True}
print(s1,type(s1))
fs2=frozenset(s1)
print(fs2,type(fs2))
len(fs2)
fs3=frozenset()
print(fs3,type(fs3))
len(fs3)
print("-------------------------")
s=[10,20,30,"RS",True]
print(s,type(s))
fs=frozenset(s)
print(fs,type(fs))

s1={10,"RS",33.33,True}
print(s1,type(s1))
fs2=frozenset(s1)
print(fs2,type(fs2))
#fs2[0]-------------------------TypeError: 'frozenset' object is not subscriptable
#fs2[0:3]----------------------TypeError: 'frozenset' object is not subscriptable
#fs2[0]=23--------------------TypeError: 'frozenset' object does not support item assignment

#del fs2[0]-------------------TypeError: 'frozenset' object doesn't support item deletion
#del fs2[0:2]-----------------TypeError: 'frozenset' object does not support item deletion
del fs2  # Possible
#print(fs2)-----------------NameError: name 'fs2' is not found

#pre-defined functions in frozensset :
fs1=frozenset({10,20,30,40,50,60,70})
print(fs1,type(fs1),id(fs1))
fs2=fs1.copy()
print(fs2,type(fs2),id(fs2))
print(fs1)

fs1=frozenset({10,20,30,40,50,60,70})
fs2=frozenset((10,20,30))
fs1.issuperset(fs2)
fs2.issuperset(fs1)
fs2.issubset(fs1)
fs1.issubset(fs2)

fs1=frozenset({10,20,30,40,50,60,70})
fs2=frozenset((100,200,300))
fs3=frozenset((10,2,3))
fs1.isdisjoint(fs2)
fs1.isdisjoint(fs3)
print(fs1)
print(fs2)
fs1.union(fs2)
fs1.intersection(fs2)
fs1.difference(fs2)
fs2.difference(fs1)
frozenset({10,20,30,40}).symmetric_difference(frozenset([10,20,50,60]) )
fs1|fs2
