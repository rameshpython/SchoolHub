#Break statements
#we can use break statements inside loops to break loop execution based on some condition
for i in range (10):
    if i==7:
        print("Processing is enough..plz break")
        break
    print(i)

print("-----------------------------------------------------")

for i in range (10):
    if i==4:
        print("Processin is enough..plz break")
        break
    print(i)

for i in range(10):
    print(i)

print("--------------------------------")

cart=[10,20,30,600,70,80]
for item in cart:
    if item >500:
        print("To place this order insurance must be required")
        break
    print(item)

print("---------------------------------------------")
#Examples:
#BreakstmtEx-1
s="python"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("-----------------")

#using break
for ch in s:
    if(ch=="0"):
        break
    print(ch,end=" ")
else:
    print("I am from else part of the loop")
print()


print("program execution is completed")

#BreakstmtEx-2
s="PYTHON"
print("By using while loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("------------------")

#Today my req to display: PYTH without using Indexing and Slicing
i=0
while(i<len(s)): # s=PYTHON
    if(s[i]=="O"):
        break
    print(s[i],end="")
    i=i+1
else:
    print("I am from else part of while loop")
print()
print("Program execution completed")

#BreakstmtEx-3
s="MISSISSIPPI"
print("By using for loop")
for ch in s:
    print("\t{}".format(ch))
else:
    print("-----------")

#Today My Req : To display 'MISS'
print("By using for loop")
ctr=0
for ch in s:
    if(ch=="S"):
        ctr=ctr+1
        if(ctr==2):
            break
        print("{}".format(ch),end=" ")

#BreakstmtEx-4
s="MISSISSIPPI"
print("By using while Loop")
i=0
while(i<len(s)):
    print("\t{}".format(s[i]))
    i=i+1
else:
    print("-------------------------------------")

#Today My Req : To display 'MISS'
print("By using while Loop")
i=0
ctr=0
while(i<len(s)): # s="MISSISSIPPI"
    if(s[i]=="I"):
        ctr=ctr+1
        if(ctr==2):
            break
    print("{}".format(s[i]),end="")
    i=i+1

#BreakstmtEx-5
n=int(input("Enter a Number :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res="PRIME"
    for i in range(2,n):
        if(n%i==0):
            res="NOT PRIME"
            break
    print("{} is {}".format(n,res))

#BreakstmtEx-6
#program for deciding whether the given number is prime or not
n=int(input("Enter a Number :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res=True
    for i in range(2,n):
        if(n%i==0):
            res=False
            break
    res="PRIME" if res else "NOT PRIME"
    print("{} is {}".format(n,res))

#BreakstmtEx-7
n=int(input("Enter a Number :"))
if(n<=1):
    print("\t{} is Invalid Input".format(n))
else:
    res=True
    i=2
    while(i<n):
        if(n%i==0):
            res=False
            break
        i=i+1
    res="PRIME" if res else "NOT PRIME"
    print("{} is {}".format(n,res))

#BreakstmtEx-8
word=input("Enter a word:")
res="NOT VOWEL"
for ch in word:
    if(ch.lower() in ['a','e','i','o','u']):
        res="VOWEL"
        break
print("{} is {} word".format(word,res))

#BreakstmtEx-9
#Program for Converting word or line of text into lower case
#Without using pre-defined Function
#ConvertIntoLower
line=input("Enter Line of Text:") # PYtHoN
print("Given Line={}".format(line))
lc=""
for ch in line:
    if ord(ch) in range(65,91):
        lc=lc+chr(ord(ch)+32)
    else:
        lc=lc+ch
else:
    print("Lower Case=",lc)

#BreakstmtEx-10
#Program for accepting Line of Text and Display Its words
#WordsFromLine
line=input("Enter Line of Text:")
print("Given Line=",line)
words=line.split()
for word in words:
    print("\t{}".format(word))


#BreakstmtEx-11
#Program for accepting Line of Text and Display Its words and find length of each word
#WordsLengthFromLine
line=input("Enter a Line of Text:")
words=line.split()
for word in words:
    print("\t{}--->{}".format(word,len(word)))

#BreakstmtEx-12
#Program for accepting Line of Text and Display Its words and find length of each word
#WordsLengthFromLine
Line=input("Enter a line of text:")
words=line.split()
d={}
for word in words:
    d[word]=len(word)
else:
    print("\tword\t\tlength")
    for W,L in d.items():
        print("\t{}\t\t{}".format(W,L))
    else:
        print("--------------")
        


