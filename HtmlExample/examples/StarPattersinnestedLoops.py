n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(i-j,end=" ")
    for k in range(0,i):
        print(k,end=" ")
    print()

print("--------------------------------------------1")
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print()


print("--------------------------------------------2")
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(1,i):
          print(i-j,end=" ")
     for k in range(0,1):
          print(k,end=" ")
     print()


print("---------------------------------------------3")
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(i+2):
          print(i-j,end=" ")
     print()


print("---------------------------------------------4")
n=int(input("Enter the number of rows:"))   
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(i+2):
          print(i-j,end=" ")
     print()

print("----------------------------------------------5")
n=int(input("Enter the number of rows:"))   
for i in range(1,n+1):
    print(" "*(n-1),end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,i):
        print(chr(64+k),end=" ")
    print()
  
print("---------------------------------------------6")
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(0,num+1-i):
        print(num+1-i,end=" ")
    for k in range(1,num+1-i):
        print(num+1-i,end=" ")
    print()

print("-----------------------------------------------7")
n=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(0,num+1-i):
        print(2*num+1-2*i,end=" ")
    for k in range(1,num+1-i):
        print(2*num+1-2*i,end=" ")
    print()

print("-----------------------------------------------8")
n=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(j,end=" ")
    for k in range(2,num+2-i):
        print(num+k-i,end=" ")
    print()

print("-------------------------------------------------9")
n=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(chr(65+2*num-2*i),end="")
    for k in range(2,num+2-i):
        print(chr(65+2*num-2*i),end="")
    print()
 
print("--------------------------------------------------10")
n=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+2-i):
        print(chr(64+j),end=" ")
    for k in range(2,num+2-i):
        print(chr(68+k-i),end=" ")
    print()

print("---------------------------------------------------")
n=int(input("Enter a number:"))
for i in range(1,n+1):
     print(" "*(n-1),end="")
     for j in range(1,i+1):
         print(n-i+j,end=" ")
     for k in range(2,i+1):
         print(n+1-k,end=" ")
     print()
for i in range(1,n+1):
     print(" "*i,end="")
     for j in range(1+i,n+1):
         print(j,end=" ")
     for k in range(2,n+1-i):
         print(n+1-k,end=" ")
     print()

print("----------------------------------------------------")


for i in range(1,n+1):
     print(" "*(n-1),end="")
     for j in range(1,i+1):
         print(n+i-j,end=" ")
     for k in range(2,i+1):
         print(n-1+k,end=" ")
     print()
for i in range(1,n+1):
     print(" "*i,end="")
     for j in range(1,n+1-i):
         print(n+1-j,end=" ")
     for k in range(2,n+1-i):
         print(i+k,end=" ")
     print()

print("----------------------------------------------------")
num=int(input("Enter a number:"))
for i  in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(i,i+1):
        print("*",end="")
        if i>=2:
            print(" "*(2*i-4),end="")
    for k in range(i,i+1):
        print("*",end=" ")
        print()

print("---------------------------------------------------")
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(i,i+1):
        print("*",end=" ")
        if i<=4:
            print(" "*(2*num-2*i-2),end="")
            for k in range(i,i+1):
                print("*",end="")
    print()

print("---------------------------------------------------")
n=int(input("Enter a number:"))
for a in range(1,n+1,2):
    for i in range(1,n+1):
        print(" "*(2*n-i-a),end="")
        for j in range(1,i+a):
            print("*",end="")
        print()
for b in range(1,n+1):
    print(" "*(n-2),end="")
    print("*"*3)
    
print("--------------------------------------------------")
n=int(input("Enter a number:"))
for i in range(1,2*n+1):
    if i%2==0:
        print("*"*i,end="")
    else:
        print("*"*(i+1),end=" ")
    print()

print("---------------------------------------------------")
n=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(2*num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,num+1):
    print(" "*(num-i),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print(" "*(num-i),end="")
    for k in range(1,i+1):
        print("*",end=" ")
    print()

print("-------------------------------------------------")
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(2*num-i+3),end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,num+3):
    print(" "*(2*num-i+1),end="")
    for j in range(-1,i+1):
        print("*",end=" ")
    print()
for i in range(1,num+5):
    print(" "*(2*num-i),end=" ")
    for j in range(-2,i+1):
        print("*",end=" ")
    print()
for i in range(1,num+3):
    print(" "*((2*num)),end="")
    print("*"*3)

print("----------------------------------------------------")
num=int(input("Enter a number:"))
for i in range(1,n+1):
    for i in range(1,i+1):
        if(i%2!=0 and j%2!=0):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print()

print("-----------------------------------------------------")
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print(" "*(i-1),end="")
    for j in range(1,num+1):
        print("*",end=" ")
    print()
