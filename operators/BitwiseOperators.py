#BITWISE OPERATORS
#<<,>>,&,|,~,^

print(4&5)

print(5|4)

bin(4)

bin(5)

print(int(0b0100))

print(int(0b100))

# print(10.3 & 12.6)
#TypeError: unsupported operand type(s) for &: 'float' and 'float'

print(True and True)

print("-------------------------------------------------------------------")
#Bitwise leftshift operator(<<)
print(4<<3)

bin(4)

bin(3)

bin(4<<3)


(9<<2)

bin(9)

bin(2)

bin(9<<2)

print(9<<2)

print(10<<0)

bin(10)

bin(0)

bin(10<<0)

#print(10.3<<2)#TypeError: unsupported operand type(s) for <<: 'float' and 'int'

#print(4<<-1)

#ValueError: negative shift count
print("------------------------------------------------------------------------")

#bitwise rightshift operator(>>)
a=10
b=a>>3
print(b)
bin(10)

bin(10>>3)

print(int(0b1))

print(16>>2)
bin(16)
print(int(0b00000100))

print(int(0b000100))


print(32>>3)

print(32>>2)

print(32>>0)

#print(23.4>>4)

#print(6>>-7)
print("-----------------------------------------------------")

#Bitwise AND(&)operator (&)
1 & 0

0 & 1

0 & 0

1 & 1
#Example-2
a=10
b=8
c=a&b	    
print(c)

a=6
b=8
c=a&b					  
print(c)

a and b
#1.2 & 2.3-------------------------TypeError: unsupported operand type(s) for &: 'float' and 'float'
1.2 and 2.3----------------------2.3
#"Python" & "Java"------------TypeError: unsupported operand type(s) for &: 'str' and 'str'
"Python" and "Java"

s1={10,20,30,40}
s2={20,30,50,60}
s4=s1&s2  # Bitwise AND (&) Performs Set Intersection.
print(s4,type(s4))
s1={1.2,2.3,4.5}
s2={11.2,2.3,13.5}
s3=s1&s2  # Bitwise AND (&) Performs Set Intersection.
print(s3,type(s3))
{1,2,3}&{4,5,1}&{1,7,8}
{1,2,3}&{4,5,1}&{2,7,8}

s1={"Apple","mango","Kiwi"}
s2={"Kiwi","Sberry","Guava"}
s3=s1&s2  # Bitwise AND (&) Performs Set Intersection.
print(s3,type(s3))

#[10,20,30]&[30,40,50]
set([10,20,30])&set([30,40,50])

#Bitwise OR(|)operator (|)
#Example-1
1|0

0|1

0|0

1|1


#Example-2

a=7
b=8
					
c=a|b				 
print(c)

print(7|8)
print(10|15)
print(3|4)
print(4|4)
print(456|456)
#print(1.2|2.3)-----------------------TypeError: unsupported operand type(s) for |: 'float' and 'float'
1.2 or 2.3
"Python" or "C"
#"Python" | "C"-------------------TypeError: unsupported operand type(s) for |: 'str' and 'strExamples-3
s1={10,20,30}
s2={10,15,25}
s3=s1|s2  # Bitwise OR Operator ( |)  Used for Finding Union of Sets
print(s3,type(s3))
{1.2,2.3,4.5}|{5.6,1.2,7.8}
{"Python","Java","C"}|{"Python","HTML","DSA"}

#"MISSISSIPPI" | "NISSON"
set("MISSISSIPPI") | set("NISSON")



