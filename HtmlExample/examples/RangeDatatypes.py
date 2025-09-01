#range Datatypes :
#form 1:
r=range(10)
for i in r:
    print(i)

#form 2:
r=range(10,20)
for i in r:
    print(i)

#form 3:
range(10,20,2)
for i in range(10,20,2):
    print(i)

r=range(10,20)
r[0]
#r[12]-->IndexError: range object index out of range
#1-->range(vvalue)
#syntax:varname=range(value)
#This syntax generates range of values from 0 to value -1
#Examples:
r=range(5)
print(r,type(r))
for val in r:
    print(val)

for val in range(6):
    print(val)

for val in range(-6):
    print(val)

#NOTE:default step in this syntax is +1 in forward direction

#2-->range(start,stop)
#synax:varname=range(start,stop)
#This syntax generates range from start to stop -1
#Examples:
r=range(10,16)
for v in range(10,16):
    print(v)

for v in range(100,120):
    print(v)

for v in range(10,-20):
    print(v)

#3--->range(start,stop,step)
#synax:varname=range(start,stop,step)
#This syntax generates range of value from start to stop -1 either in forward and backword  Direction by maintaing equal interals
#Examples :
r=range(20,30,2)
for v in range(20,30,2):
    print(v)

for v in range(20,30,3):
    print(v)

for v in range (-1,-6,-1):
    print(v)
for v in range (-1-10,2):
    print(v)

for v in range(10,21):
    print(v)

for v in range(10,21,2):
    print(v)
    

    
    



    
    
