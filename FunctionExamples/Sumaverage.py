#Program for Calculating sum and average of n numbers
def readvalues():
    nov=int(input("Enter How Many Values Sum and Avg u want to find:"))
    if(nov<=0):
        return []  # here [] represents Empty List
    else:
        lst=list()
        for i in range(1,nov+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        return lst # returns non-empty list

def findsumavg(lst):
    if(len(lst)==0):
        print("List is empty-can't find sum and avg")
    else: # lst=[10,3,4,6,18]
        s=0
        for val in lst:
            s=s+val
        else:
            print("Sum={}".format(s))
            print("Avg={}".format(s/len(lst)))

print("----------------------------------------------------------")

#Program for Calculating sum and average of n numbers
def readvalues():
    nov=int(input("Enter How Many Values Sum and Avg u want to find:"))
    if(nov<=0):
        return []  # here [] represents Empty List
    else:
        lst=list()
        for i in range(1,nov+1):
            value=float(input("Enter {} Value:".format(i)))
            lst.append(value)
        return lst # returns non-empty list

def findsumavg(lst):
    if(len(lst)==0):
        print("List is empty-can't find sum and avg")
    else: # lst=[10,3,4,6,18]
        print("Sum={}".format(sum(lst)))
        print("Avg={}".format(sum(lst)/len(lst)))

#Main Program
vals=readvalues() # Function Call Obtains List as result
findsumavg(vals)