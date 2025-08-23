#star patterns in range formats in loops and nestes(or)inner loops
n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
     print(" "*(n-i),"*"*(2*i-1))
         

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    print(" "*(n-i),"*"*(2*i-1))

          
for i in range(1,5):
     for j in range(i+2):
         print(" "*" ")

for i in range(1,5):
     for j in range(i+2):
         print(" "*"i+2")


for i in range(1,5):
     for j in range(i+2):
         print(" "*"(2*i-1)*" ")

 
for i in range(1,5):
     for j in range(i+2):
         print(" "*"(2*i-1)*")


n=int(input("Enter the number of rows:"))
Enter the number of rows:5
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(1,2*i):
         print(j,end=" ")
     print()

   
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(i+2):
          print(j,end=" ")
     print()

    
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(i


                  
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(2*i):
          print(j,end=" ")
     print()

   
for i in range(1,n+1):
     print(" "*(n-i),end="")
     for j in range(1,2*i):
          print(j,end=" ")
     print()

for i in range(1,n+1):
                    print(" "*(n-i),end="")
                    for j in range(1,i+2):
                    print(j,end=" ")
                    print()



