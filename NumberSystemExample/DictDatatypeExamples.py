#Pre defined functions in dict :
#1. clear()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
len(d1)
d1.clear()
print(d1,type(d1),id(d1))
len(d1)
print(d1.clear())
print({}.clear())
print(dict().clear())

#2. pop()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d1.pop(20)
print(d1,type(d1),id(d1))
d1.pop(30)
print(d1,type(d1),id(d1))
d1.pop(40)
print(d1,type(d1),id(d1))
#d1.pop(30)-------------------------------KeyError: 30
#{}.pop(10)--------------------------------KeyError: 10
#dict().pop(20)---------------------------keyError: 20

#3. popitem()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
d1.popitem()
print(d1,type(d1),id(d1))
#d1.popitem()------------------------------KeyError: 'popitem(): dictionary is empty'
#{}.popitem()-------------------------------KeyError: 'popitem(): dictionary is empty'
#dict().popitem()-------------------------KeyError: 'popitem(): dictionary is empty'

#4. copy()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
d2=d1.copy() # Shallow Copy
print(d2,type(d2),id(d2))
d1[10]=12.3
d2[40]=14.4
print(d1,type(d1),id(d1))
print(d2,type(d2),id(d2))

#5. get()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1,type(d1),id(d1))
val=d1.get(10)
print(val)
val=d1.get(20)
print(val)
val=d1.get(200)
print(val)
statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)
cap=statescaps.get("TS")
print(cap)
cap=statescaps.get("KAR")
print(cap)
cap=statescaps.get("AMPT")
print(cap)
print({}.get(10))
print("-------------------------")
d1={10:1.2,20:2.2,30:2.3,40:4.4}
d1[10]-----------------1.2
d1[40]-----------------4.4
#d1[400]----------------KeyError: 400

#6. keys()
statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)
states=statescaps.keys()
print(states,type(states))
for k in states:
    print(k)

			
for k in statescaps.keys():
    print(k)

		
for k in {10:"Apple",20:"Mango",30:"Kiwi"}.keys():
    print(k)

		
for k in {10:"Apple",20:"Mango",30:"Kiwi"}.keys():
    print(k,"--->",{10:"Apple",20:"Mango",30:"Kiwi"}[k])

		
for k in {10:"Apple",20:"Mango",30:"Kiwi"}.keys():
    print(k,"--->",{10:"Apple",20:"Mango",30:"Kiwi"}.get(k))

		
print("-------------------------------")
for de in enumerate(statescaps):
    print(de)

		
for de in enumerate(statescaps):
    print(de,"-->",statescaps[de[1]])

		
for de in enumerate(statescaps):
    print(de,"-->",statescaps.get(de[1]))

		
#7. values()
statescaps={"TS":"HYD","AP":"VIJ","KAR":"BANG","MH":"MUM"}
print(statescaps)
caps=statescaps.values()
print(caps,type(caps))
for v in caps:
	print(v)

		
for v in statescaps.values():
		print(v)

for v in {'TS': 'HYD', 'AP': 'VIJ', 'KAR': 'BANG', 'MH': 'MUM'}.values():
			print(v)

			

#8. items()
d1={10:1.2,20:2.2,30:2.3,40:4.4}
print(d1)
kvs=d1.items()
print(kvs,type(kvs))
for kv in kvs:
		print(kv)

for kv in kvs:
	print(kv[0],"-->",kv[1])

for kv in d1.items():
		print(kv[0],"-->",kv[1])

		
for k,v in d1.items():
		print(k,"==>",v)

		

#9. update()
d1={10:1.2,20:2.3}
d2={30:3.3,40:4.4}
d1.update(d2)
print(d1)
print("--------------------")
d1={10:1.2,20:2.3}
d2={20:13.3,40:4.4}
d2.update(d1)
print(d2)
print("---------------------")
d1={10:11.2,20:12.3}
d2={10:1.2,20:2.3}
d1.update(d2)
print(d1)

print("----------------------------------------------------------------------------------------------------------------------------------")

