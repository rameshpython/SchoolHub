#nested or inner Dict
#combination of Dict with List,tuple and set
#Dict in Dict --POSSIBLE
d={"sno":100,"name":"RS","mem":{"CM":20,"C++":18},"em":{"CM":70,"C++":80},"ColName":"OU"}
print(d,type(d))
for k,v in d.items():
    print(k,"-->",v,"-->",type(v),"-->",type(d))
d["mem"]
d.get("mem")
for k,v in d["mem"].items():
		print(k,v)

			
for k,v in d.get("mem").items():
		print(k,v)
			
for k in d.get("em"):
		print(k,d.get("em")[k])

for k in d.get("em"):
		print(k,d["em"][k])
print("---------------------------------------------------------------------------------------------------------------------------")
d={"sno":100,"name":"RS","mem":{"CM":20,"C++":18},"em":{"CM":70,"C++":80},"ColName":"OU"}
print(d)
d["mem"]["PM"]=19
d.get("em")["PM"]=70
print(d)


print(d)
{'sno': 100, 'name': 'RS', 'mem': {'C++': 18, 'PM': 19}, 'em': {'CM': 70, 'PM': 70}, 'ColName': 'OU', 'BM': {'CM': 1.2, 'C++': 2.3, 'PM': 1.5}, 'totm': {'tcpp': 100.3, 'tpm': 90.5}}
#for k in d['BM'].keys():
    #print(k)
		
d.popitem()
print(d)
d["em"].clear()
print(d)

d.get("mem")["PM"]=d.get("mem")["PM"]+(d.get("mem")["PM"])*(10/100)
print(d)
d["mem"]["C++"]=25
print(d)

#List in Dict--POSSIBLE

d={"sno":10,"name":"RS","me":[20,18,25],"em":[80,67,78],"cname":"OU"}
print(d)
for k,v in d.items():
    print(k,"-->",v,"--->",type(v),"-->",type(d))

		
      
d.get("me").append(22)
print(d)
d["em"].insert(1,72)
print(d)
d.get("me").sort()
print(d)
d["em"].sort(reverse=True)
print(d)
del d["me"][::2]
print(d)
del d.get("em")[1:]
print(d)
d.pop("me")
[20, 25]
print(d)
d["me"]=[20,25,12]
print(d)
del d["em"]
print(d)

#Tuple in Dict

d={"sno":10,"name":"RS","me":(20,18,25),"em":(80,67,78),"cname":"OU"}
for k,v in d.items():
    print(k,"-->",v,"--->",type(v),"-->",type(d))

		
d.get("em")[1:]
d["me"][::2]
d.get("me").count(18)
d.get("me").count(108)
sorted(d["me"])
tuple(sorted(d["me"]))
d["me"]=tuple(sorted(d["me"]))
print(d)
d["em"]=tuple(sorted(d.get("em"))[::-1])
print(d)

#Set  in Dict-------------POSSIBLE

d={"sno":10,"name":"RS","me":{20,18,25},"em":{80,67,78},"cname":"OU"}
print(d)
for k,v in d.items():
    print(k,"-->",v,"--->",type(v),"-->",type(d))


d.get("me").add(14)
d.get("em").add(49)
print(d)
d["allmarks"]=d["me"].union(d.get("em"))
print(d)
d.get("allmarks").remove(49)
print(d)
d.popitem()
print(d)

#Dict in List------------POSSIBLE

lst=[10,"RS",{"CM":20,"CPPM":18,"PM":17},"JNTU"]
print(lst,type(lst))
for val in lst:
    print(val,"-->",type(val),"-->",type(lst))


lst[2].get("CM")+lst[2]["CPPM"]+lst[-2]["PM"]

lst[2]["TOT"]=lst[2].get("CM")+lst[2]["CPPM"]+lst[-2]["PM"]
print(lst,type(lst))
lst[2]
lst[2].pop("PM")
print(lst,type(lst))
lst.insert(-1,{"TS":"HYD","KAR":"BANG"})
print(lst,type(lst))
del lst[2:4]
print(lst,type(lst))

#Dict in Tuple---POSSIBLE

tpl=(10,"RS",{"CM":20,"CPPM":18,"PM":17},"JNTU")
print(tpl,type(tpl))
for val in tpl:
    print(val,"-->",type(val),"-->",type(tpl))



tpl[2]
tpl[2].pop("CPPM")
print(tpl,type(tpl))
tpl[-2]["OS"]=19
print(tpl,type(tpl))
tpl[2:]

#Dict in Set--Not Possible

#>>> s1={10,"RS",{"CM":20,"CPPM":18,"PM":17},"JNTU"}-----------TypeError: unhashable type: 'dict'




			


