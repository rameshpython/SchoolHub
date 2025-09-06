studentfile=open("studentData.txt","r")
print(studentfile)
studentData=studentfile.read()
print(studentData)





def smallLetterConversion(s):
    a=s.lower()
    print(a)


smallLetterConversion(studentData) 



def show_capitalize(text):
    print("Original string:",(text))
    print("After capitalize:",text.capitalize())

s="python"
show_capitalize(s)

print("----------------------------------------------")

def show_capitalize(text):
    s="python"
    print("Original string:", (text))
    print("After capitalize:", text.capitalize())

show_capitalize(s)

print("-----------------------------------------------")
def Title(string):
    s="string"
    print("original string:",(string))
    print("After Title:",string.title())

s="python is a good language"
Title(s)
Title(s)
Title(s)
Title(s)
print("-----------------------------------------------")

def index():
    s="python"
    print("index of 't':",s.index("t"))

index()
index()
index()

print("-------------------------------------------------")

def show_upper(text):
    print("Original String:", text)
    print("After upper():", text.upper())

# main program
s = "python"
show_upper(s)



def show_upper(text):
    return text.upper()

# main program
s = "python"
result =show_upper(s)

print("Original String:", s)
print("After upper():", result)

print("--------------------------------------------------")

def show_lower(text):
    print("Original String:", text)
    print("After lower():", text.lower())

#main program
s="GANAPATHI"
show_lower(s)


print("--------------------------------------------")

def show_lower(text):
    return text.lower()

# main program
s = "MaHEsh BAbu"
result =show_lower(s)

print("Original String:", s)
print("After lower():", result)

print("-----------------------------------------------")
def show_isupper(string):
    print("Original String:",string)
    print("After isupper():",string.isupper())

#main program
s="GANAPATHY"
show_isupper(s)



def show_isupper(text):
    return text.isupper()

# main program
s = "MaHEsh BAbu"
result =show_isupper(s)

print("Original String:", s)
print("After isupper():", result)


print("---------------------------------------")
def show_islower(string):
    print("Original String:",string)
    print("After islower():",string.isupper())

#main program
s="ramesh babu"
show_islower(s)



def show_islower(text):
    return text.islower()

# main program
s = "MaHEsh BAbu"
result =show_islower(s)

print("Original String:", s)
print("After islower():", result)

print("------------------------------------------")

def show_isalpha(string):
    print("Original String:",string)
    print("After isalpha():",string.isalpha())

#main program
s="rameshBabu"
show_isalpha(s)



def show_isalpha(text):
    return text.isalpha()

# main program
s = "123456"
result =show_isalpha(s)

print("Original String:", s)
print("After isalpha():", result)

print("-------------------------------------------")

def show_isdigit(string):
    print("Original String:",string)
    print("After isdigit():",string.isdigit())

#main program
s="rameshBabu"
show_isdigit(s)



def show_isdigit(text):
    return text.isdigit()

# main program
s = "123456"
result =show_isdigit(s)

print("Original String:", s)
print("After isdigit():", result)

print("-------------------------------------------")
def show_isalnum(string):
    print("Original String:",string)
    print("After isalnum():",string.isalnum())

#main program
s="rameshBabu"
show_isalnum(s)



def show_isalnum(text):
    return text.isalnum()

# main program
s = "123456ramesh"
s= "12345678"
s= "#$%^&"
result =show_isalnum(s)

print("Original String:", s)
print("After isalnum():", result)

print("---------------------------------------------")

def show_isspace(string):
    print("Original String:",string)
    print("After isspace():",string.isspace())

#main program
s="rameshBabu"
s=" "
show_isspace(s)
show_isspace(s)



def show_isspace(text):
    return text.isspace()

# main program
s = "123456ramesh"
s= "12345678"
s= "#$%^&"
s= ""
result =show_isspace(s)

print("Original String:", s)
print("After isspace():", result)

print("-----------------------------------------------")

def show_split(string):
    print ("Original string:",string)
    print("After split():",string.split())

#main program
s="my name is gaganam ramesh  babu"
show_split(s)



def show_split(text):
    return text.split()

#main program
s ="all  the public in the world are fully of  selfish beings only"
result =show_split(s)
print("Original String:", s)
print("After split():", result)


