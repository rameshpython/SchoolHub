n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(i-j,end=" ")
    for k in range(0,i):
        print(k,end=" ")
    print()

print("--------------------------------------------")
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i):
        print(chr(i-j+65),end=" ")
    for k in range(0,i):
        print(chr(k+65),end=" ")
    print()


print("--------------------------------------------")
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(1,i):
          print(i-j,end=" ")
     for k in range(0,1):
          print(k,end=" ")
     print()


print("---------------------------------------------")
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(i+2):
          print(i-j,end=" ")
     print()


print("---------------------------------------------")
n=int(input("Enter the number of rows:"))   
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(i+2):
          print(i-j,end=" ")
     print()

print("----------------------------------------------")
n=int(input("Enter the number of rows:"))   
for i in range(1,n+1):
    print(" "*(n-1),end=" ")
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    for k in range(1,i):
        print(chr(64+k),end=" ")
    print()
  
