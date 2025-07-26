#Assignment Operators
#1. += --> Add and Assign
x = 10
x += 5  # same as x = x + 5
print(x)

x=-10
x+=5
print(x)

x=10.5
x+=4
print(x)

#x="ramesh"
#x+=4
print(x)#TypeError: can only concatenate str (not "int") to str

x="ramesh"
x+="gaganam"
print(x)
print("--------------------------------------------------")
#x+=200
print(x)
text="Hello"
text+="World"
print(text)

list=[1,2]
my_list=[1,2]
my_list+=[3,4]
print(my_list)

total=0
for i in range(1,6):
     total+=i
     print(i)


#2. -= --> Subtract and Assign
x = 20
x -= 7  # same as x = x - 7
print(x)

#3. *= --> Multiply and Assign
x = 6
x *= 3  # same as x = x * 3
print(x)

#4. /= --> Divide and Assign (Float division)
x = 20
x /= 4  # same as x = x / 4
print(x)

#5. //= --> Floor Divide and Assign
x = 17
x //= 4  # same as x = x // 4
print(x)

#6. %= --> Modulus and Assign
x = 10
x %= 3  # same as x = x % 3
print(x)

#7. **= --> Exponentiate and Assign
x = 3
x **= 2  # same as x = x ** 2 → 3^2
print(x)







