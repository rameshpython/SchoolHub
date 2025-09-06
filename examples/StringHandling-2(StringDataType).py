# #string  Handling :
# #The pre-defined functions in sring object are  given :
# print("-------------")
# #1.capitalize()
# print("-------------")
# s="ramesh"
# s.capitalize()
# print(s,type(s))
#
#
# >>> s="python"
# >>> print(s,type(s))
# python <class 'str'>
# >>> s.capitalize()
# 'Python'
# >>> len(s)
# 6
# >>>
# >>> s='ramesh'
# >>> print(s,type(s))
# ramesh <class 'str'>
# >>> s.capitalize()
# 'Ramesh'
# >>>
# >>> s='''ramesh'''
# >>> print(s,type(s))
# ramesh <class 'str'>
# >>> s.capitalize()
# 'Ramesh'
# >>>
# >>> s="my name is  gaganam ramesh"
# >>> print(s,type(s))
# my name is  gaganam ramesh <class 'str'>
# >>> s.capitalize()
# 'My name is  gaganam ramesh'
#
# #2.title()
# >>> s="python"
# >>> print(s,type(s))
# python <class 'str'>
# >>> s.title()
# 'Python'
# >>>
# >>> s="my name is gaganam ramesh"
# >>> print(s,type(s))
# my name is gaganam ramesh <class 'str'>
# >>> s.title()
# 'My Name Is Gaganam Ramesh'
#
# #3.index()
#
# >>> s="python"
# >>> print(s,type(s))
# python <class 'str'>
# >>> s.index("t")
# 2
# >>> s.index('o')
# 4
# >>> s="my name is ramesh"
# >>> s.index("a")
# 4
# >>> s.index(y)
#             ^
# >>> s.index("y")
# 1
# >>> s.index('h')
# 16
#
# #4.upper()
# >>> s='hare rama hare krishna jai ganesha'
# >>> print(s,type(s))
# hare rama hare krishna jai ganesha <class 'str'>
# >>> s.upper()
# 'HARE RAMA HARE KRISHNA JAI GANESHA'
#
#
# #5.lower()
# >>> s.lower()
# 'hare rama hare krishna jai ganesha'
# >>>
# >>> s="Hello  How Are YOUR nAMe IS WhaT"
# >>> s.lower()
# 'hello  how are your name is what'
# >>>> s="IAM THE PERSON IN THE WORLD TO INTILLEGENT"
# >>> print(s,type(s))
# IAM THE PERSON IN THE WORLD TO INTILLEGENT <class 'str'>
# >>> s.lower()
# 'iam the person in the world to intillegent'
#
# #6.isupper() and 7.islower()
# >>> s="Python"
# >>> s.islower()
# False
# >>>
# >>> s="python is programing language"
# >>> s.islower()
# True
# >>>
# >>> s='PYTHON'
# >>> s.islower()
# False
# >>>
# >>> s="SAMRAT PHONED"
# >>> s.isupper()
# True
# >>> s="python is programing language"
# >>> s="@#$%^&*!"
# >>> s.islower()
# False
# >>> s.isupper()
# False
# >>> s.isupper()
# False
# >>> s="python is programing language"
# >>> s.islower()
# True
# >>>
# >>> There Is A Great PhilosPhEre
#   File "<python-input-73>", line 1
#     There Is A Great PhilosPhEre
#           ^^
# SyntaxError: invalid syntax
# >>> s="There Is A Great PhilosPhEER"
# >>> s.isupper()
# False
#
# #7.isalpha()
# >>> s="python"
# >>> s.isalpha()
# True
# >>>
# >>> s="python123"
# >>> s.isalpha()
# False
# >>> "1234"
# '1234'
# >>> s="1234"
# >>> s.isalpha()
# False
# >>> s="   "
# >>> s.isalpha()
# False
# >>> s="@#$%^&"
# >>> s.isalpha()
# False
#
# #8.isdigit()
# >>> s="python"
# >>> s.isdigit()
# False
# >>> s="12345"
# >>> s.isdigit()
# True
# >>> s="pytho123"
# >>> s.isdigit()
# False
# >>> s="@#$%^&"
# >>> s.isdigit()
# False
# >>> s=" "
# >>> s.isdigit()
# False
#
# #9.isalnum()
# >>> s="pytho1234"
# >>> print(s,type(s))
# pytho1234 <class 'str'>
# >>> s.isalnum()
# True
# >>> s="12345"
# >>> s.isalnum()
# True
# >>> s="rameshgaganam"
# >>> s.isalnum()
# True
# >>> s="rameshgaganam12344@#$%^"
# >>> s.isalnum()
# False
# >>> s="rameshgaganam987643"
# >>> s.isalnum()
# True
# #10.isspace()
# >>> s="  "
# >>> s.isspace()-----------True
# >>> s=""
# >>> s.isspace()--------------False
# >>> s="python Prog"
# >>> s.isspace()-------------False
# >>> s="Prasana Laxmi"
# >>> s.isspace()--------------False
# >>> s.isalpha()-----------False
# >>> s.isalpha() or s.isspace()-----------False
#
#
#
# #12.split()
# >>> #split()
# >>> s="python is opp language"
# >>> print(s)
# python is opp language
# >>> s.split()
# ['python', 'is', 'opp', 'language']
# >>> s.split("-")
# ['python is opp language']
# >>> s.split("_")
# ['python is opp language']
# >>>  s="python is opp language"
# >>> text="apple,banana,grape"
# >>> fruits=text.split(",")
# >>> print(fruits)
# ['apple', 'banana', 'grape']
# >>>
# >>> text="apple"
# >>> text.split()
# ['apple']
# >>> fruits=text.split()
# >>> print(fruits)
# ['apple']
# >>>
# >>>
# >>> s="python is an oop language"
# >>> s.split()
# ['python', 'is', 'an', 'oop', 'language']
# >>>
# >>> text="python is an oop language"
# >>> text.split()
# ['python', 'is', 'an', 'oop', 'language']
# >>>
# >>> s="python"
# >>> s.split()
# ['python']
# >>> s="python is an oop language"
# >>> s.split()
# ['python', 'is', 'an', 'oop', 'language']
# >>> len(s.split())
# 5
# >>> x=s.split()
# >>> print(x)
# ['python', 'is', 'an', 'oop', 'language']
# >>>
# >>> s="12-09-2025"
# >>> print(s)
# 12-09-2025
# >>> s.split()
# ['12-09-2025']
# >>> s.split("-")
# ['12', '09', '2025']
# >>>
# >>> s="12-09-2025"
# >>> dob=s.split("-")
# >>> print(dob)
# ['12', '09', '2025']
# >>> print("Day",dob[0])
# Day 12
# >>> print("month",dob[1])
# month 09
# >>> print("year",dob[2])
# year 2025
# >>>
# >>>
# >>> s="Apple#banana#kiwi/grape"
# >>> print(s)
# Apple#banana#kiwi/grape
# >>> s="Apple#banana#kiwi/grape"
# >>> words=s.split("#")
# >>> print(words)
# ['Apple', 'banana', 'kiwi/grape']
# >>>
# >>>
# >>> words=s.split("/")
# >>> print(words)
# ['Apple#banana#kiwi', 'grape']
# >>>
# >>> s="Apple#banana^kiwi;grapes_orange"
# >>> print(s)
# Apple#banana^kiwi;grapes_orange
# >>> fruits=s.split(";")
# >>> print(fruits)
# ['Apple#banana^kiwi', 'grapes_orange']
# >>> s.split("^")
# ['Apple#banana', 'kiwi;grapes_orange']
#
# #13.join()
# list=["hyd","bang","vij","Delhi"]
# print(list,type(list))
# s.join(list)
