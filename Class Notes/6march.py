# global vs local scope

# a=10
# def i():
#     a=9
#     print(a)
# i()          # output will be 9 
# print(a)     #output will be 10 as a=9 is in local scope 
# ----------------------------------------------------------
# global keyword

# a=10
# def i():
#     global a
#     a=9
#     print(a)
# i()          # output will be 9 
# print(a)     #output will be 9 as a=9 is global in local scope 
# ----------------------------------------------------------------------
# nonlocal keyword

# def i():
#     b=9
#     print(b)
#     def j():
#         b=5
#         print(b)
#     j()       #o/p = 9
# i()      #o/p =5


# def i():
#     b=9
#     print(b)
#     def j():
#         nonlocal b 
#         b=5
#         print(b)
#     j()       #o/p = 9
# i()      #o/p =5

# -----------------------------------------------------------------------------

# # task1  product of  list elements
# def pro():
#     a=eval(input("enter list"))
#     p=1
#     for i in a:
#         p=p*int(i)
#     return p
# result=pro()
# print(result)

# ---------------------------------------------------------------------
# # task 2:  wap to print initial index of char present in given string
 
# def ind(name , letter):
#     for i in range(len(name)):
#             if name[i]==letter:
#                 return i
# print(ind(input("enter str"),input("enter char")))

# ----------------------------------------------------------------------

# packing and unpacking:

# def ind(s , ch):
#     for i in range(len(s)):
#         if s[i]==ch:
#             return i
# print(ind('aksh','i','t'))       #gives error

# def ind(v,t):
#     for i in range(len(t)):
#         if t[i]==v:
#             return i
# print(ind(100,20,30,20,30,100))     #error : ind() takes 2 positional arguments but 6 were given

# ---------------------------------------------------------------------------

# tuple packing
# def ind(v,*t):
#     for i in range(len(t)):
#         if t[i]==v:
#             return i
# print(ind(100,20,30,20,30,100))     #o/p =4 v ke baad ki jo bhi values hogi vo t m store ho jaegi as a tuple

# Note : we need to pass packing argument as last argument otherwise it gives error

# def ind(*t,v):
#     for i in range(len(t)):
#         if t[i]==v:
#             return i
# print(ind(100,20,30,20,30,100))    # gives error bcz tuple arg is passed first with *

# ------------------------------------------------------------------------------

# dictionary packing

# def dic(d):
#     return d
# print(dic(a=100,b=200,c=30,d=70))      #error 


# def dic(*d):
#     return d
# print(dic(a=100,b=200,c=30,d=70))   # error 


# def dic(**d):
#     return d
# print(dic(a=100,b=200,c=30,d=70))     # o/p={'a': 100, 'b': 200, 'c': 30, 'd': 70}

# def dic(**d):
#     return d
# print(dic(a=100,b=200,12='aksh',d=70))  # number can not be key


# def dic(**d):
#     return d
# print(dic(a=100,b=200,c1=30,d=70))  #o/p={'a': 100, 'b': 200, 'c1': 30, 'd': 70}
#  keys here are like variable so must follow those 6 rules of identifier

# -----------------------------------------------------------------------

# unpacking of tuple
# def addition(a, b, c):
#     return a + b + c
# num = (1, 5, 10)  
# print( addition(*num) )     #o/p=16 ,Explanation: *num unpacks numbers into a, b, c.


# def p(a,b,c,d):
#     print(a,b,c,d)
# s='wxyz'
# p(*s)       #o/p = w x y z   ,here every index element of string is assigned with a , b , c , ressp.
# --------------------------------------------------------------------------

# unpacking of dictionary

# def info(name, age, country):
#     print(f"Name: {name}, Age: {age}, Country: {country}")

# data = {"name": "akshita", "age": 30, "country": "India"}
# info(**data) 
# only values will be printed 
# o/p =Name: akshita, Age: 30, Country: India
# Explanation: **data unpack dictionary values and assign them to parameters.



# def info(name, age, country):
#     print(name,age,country)

# data = {"name": "akshita", "age": 30, "country": "India"}
# info(**data)     # o/p = akshita 30 India   , only values will be printed