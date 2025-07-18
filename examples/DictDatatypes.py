#Dict Datatypes :
#Examples :
d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1))
len(d1)
d2={"Python":1,"C":2,"Java":3,"C++":4}
print(d2,type(d2))
len(d2)
d3={100:1.2,200:1.3,300:1.2,400:1.3}
print(d3,type(d3))
print("---------------------------------")
d1={10:1.2,10:2.3,10:4.5,10:0.2}
print(d1)
d1={10: 1.2, 20: 2.3, 10: 1.9, 80 : 2.9}
print(d1)
print("----------------------------------")
d1={10:1.2,10:2.3,10:4.5,10:0.2}
print(d1)
d1={10: 1.2, 20: 2.3, 10: 1.9, 80 : 2.9}
print(d1)
print("-----------------------------------")
d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1))
#d1[0]#---------KeyError: 0
d1[10]#--------'Apple'
d1[20]#--------'Mango'
d1[30]#--------'Kiwi'
d1[40]#---------'Sberry'
#d1[50]#--------KeyError: 50
print("------------------------------------")
d1={10:"Apple",20:"Mango",30:"Kiwi",40:"Sberry"}
print(d1,type(d1),id(d1))
d1[10]="Guava" # Udating Value of Value by using Value of Key
print(d1,type(d1),id(d1))
print("-------------------------------------")
d1={}
print(d1,type(d1))
len(d1)
#  0R
d2=dict()
print(d2,type(d2))
len(d2)

print("--------------------------------")
d1={}
d1[100]=1.2
d1[200]=2.3
d1[300]=3.5
d1[400]=6.7
d1[500]=7.3
print(d1,type(d1))
d1[300]=9.9
print(d1,type(d1))
len(d1)
d1[500]=23.56
print(d1)
d1[300]=0.2 # Modified Entry bcoz the key 300 already exist in d1 
print(d1,type(d1),id(d1))

