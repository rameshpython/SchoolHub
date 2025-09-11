#ValueTypeEx.py
def dispvaluetype(x):
    if(type(x)==int):
        print("\tValue={} Type={}".format(x,type(x)))
    elif(type(x)==float):
        print("\tValue={} Type={}".format(x, type(x)))
    elif(type(x)==bool):
        print("\tValue={} Type={}".format(x, type(x)))
    elif (type(x) == complex):
        print("\tValue={} Type={}".format(x, type(x)))
        print("\tReal Part={}".format(x.real))
        print("\tImaginary Part={}".format(x.imag))
    elif (type(x) == str):
        print("\tValue={} Type={}".format(x, type(x)))
        print("\tLower Case={}".format(x.lower()))
    elif (type(x) == bytes):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == bytearray):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == range):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == list):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == tuple):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == set):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == frozenset):
        print("\tValue={} Type={}".format(x, type(x)))
        for val in x:
            print("\t{}".format(val))
    elif (type(x) == dict):
        print("\tValue={} Type={}".format(x, type(x)))
        for key,val in x.items():
            print("\t{}--->{}".format(key,val))
    else:
        print("\tValue={} Type={}".format(x, type(x)))
#main program
dispvaluetype(10) # Function Call Takes int type
dispvaluetype(10.34) # Function Call Takes float type
dispvaluetype(True) # Function Call Takes bool type
dispvaluetype(2+3.5j) # Function Call Takes complex type
#-------------------------------------------
dispvaluetype("PYTHON") # Function Call Takes str type
dispvaluetype(bytes([178,245,234,204])) # Function Call Takes bytes type
dispvaluetype(bytearray([178,245,234,204])) # Function Call Takes bytearray type
dispvaluetype(range(10,21,2)) # Function Call Takes range type
#-------------------------------------------
dispvaluetype([10,"RS",34.56,True])# Function Call Takes List type
dispvaluetype((10,"RS",34.56,True))# Function Call Takes tuple type
#-------------------------------------------
dispvaluetype({10,20,30,40,10,20,30})# Function Call Takes set type
dispvaluetype(frozenset({10,20,30,40,10,20,30}))# Function Call Takes frozenset type
#-------------------------------------------
dispvaluetype({10:"Python",20:"Java",30:"C",40:"HTML"})# Function Call Takes dict type
#-------------------------------------------
dispvaluetype(None)# Function Call Takes NoneType ype

print("--------------------------------------------------------------------------------------")

#ValueTypeEx2.py
def dispvalue(x:str):
    print("Given data={}".format(x))
    print("Upper Case data=",x.upper())
    print("lower Case data=", x.lower())

#main Program
dispvalue("Python Is an Oop Lang")