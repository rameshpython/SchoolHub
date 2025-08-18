#continue statement
for i in range(30):
    if i%2==0:
        continue
    print(i)

print("----------------------------------")

cart=[10,20,30,500,600,700,50,60]
for item in cart:
    if  item>=500:
        print("we can not process this item:",item)
        continue
    print(item)
print("----------------------------------")

numbers=[10,20,30,0,5,0,30]
for n in numbers:
    if n==0:
        print("hey how we can divide with zero..just skipping")
        continue
    print("100/{}={}".format(n,100/n))

#loops with else block
#inside loop  execution ,if break statement not executed ,then only else part will be executed
cart=[10,20,30,40,50]
for item in cart:
    if item>=500:
        print("we cannot process this order")
        break
    print(item)
else:
    print("congrats...all items processed successfully")

print("----------------------------------")

cart=[10,20,500,600,40,50]
for item in cart:
    if item>=500:
        print("we cannot process this order")
    print(item)
else:
    print("congrats...all items processed successfully")
    
print("------------------------------------------------------")

#Examples
#ContinueStmtEx-1
s="PYTHON"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("Iam from else part of for loop")
#Today:my req :PYHON
for ch in s:
    if(ch=="T"):
        continue
    print(ch,end=" ")
else:
    print()
    print("I am from else part of for loop")
    
print("_-----------------------------------------")

#ContinueStmtEx-2

s="PYTHON"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("I am from else part of for loop")

#Today: My Req: PYHON
i=0
while(i<len(s)): # s="PYTHON"
    if(s[i]=="T"):
        i=i+1
        continue
        #i=i+1--Can't execute
    print(s[i],end="")
    i=i+1
else:
    print()
    print("I am from else part of for loop")
    
print("----------------------------------------------------")

#ContinueStmtEx3.py
s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
#------------------------------------------
#Today: My Req: PYHN
for ch in s:
    if(ch=="T") or (ch=="O"):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")

print("----------------------------------------------------")

#ContinueStmtEx4.py

s="PYTHON"
print("By using for Loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("I am from else part of for loop")
#------------------------------------------
#Today: My Req: PYHN
for ch in s:
    if(ch in ["T","O"] ):
        continue
    print(ch,end="")
else:
    print()
    print("I am from else part of for loop")

print("-----------------------------------------------")


#ContinueStmtEx5.py
#Prtogram for Obtaining List of +Ve values from given List of elements

lst=[10,-23,20,-45,67,-11,78,-90,-89,29]
print("List of +Ve Values")
for val in lst:
    if(val<=0):
        continue
    print("\t{}".format(val))

print("-----------------------------------------------")


#ContinueStmtEx6.py
#Prtogram for Obtaining List of -Ve values from given List of elements

lst=[10,-23,20,-45,67,-11,78,-90,-89,29]
print("List of -Ve Values")
for val in lst:
    if(val>=0):
        continue
    print("\t{}".format(val))

print("-----------------------------------------------")
#ContinueStmtEx7
#Program for accepting a Line / word and obtains only Vowels
#ContinueStmtEx7.py
word=input("Enter a word:") # word="PYTHON"
for ch in word:
    if ch.lower() not in ['a','e','i','o','u']:
        continue
    print("{}".format(ch),end="")

