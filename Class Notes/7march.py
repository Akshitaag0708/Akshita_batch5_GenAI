# Types of argument:

# def form(name,mail,ph,age=20):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age}")
# form("aksh",'akshita@gmail.com',7852849078,22) f form(name,mail,ph,age):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age}")
# form('akshita@gmail.com',7852849078,21)   # gives error as one parameter is not passed


# positional argument :value pass during function call is manadatory
# def form(name,mail,ph,age):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age}")
# form("aksh",'akshita@gmail.com',7852849078,21)   # gives correct output
# -------------------------------------------------------------------
# default argument
# def form(name,mail,ph,age=20):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age}")
# form("aksh",'akshita@gmail.com',7852849078)   # gives correct output no error bcz age value is default 

# def form(name,mail,ph,age=20):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age}")
# form("aksh",'akshita@gmail.com',7852849078,22)  # age output will be 22
 # if we provide new value to default argument during function call then the default value will be overridden by new value

# def form(name,mail,ph,age=20,alt_ph=None):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age} \n alternate phone is {alt_ph}")
# form("aksh",'akshita@gmail.com',7852849078)    #"alternate phone is None"is printed 

# def form(name,mail,ph,age=20,alt_ph=None):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age} \n alternate phone is {alt_ph}")
# form("aksh",'akshita@gmail.com',7852849078,22,5678901234 )    # alt ph value will be overridden by new value


# -----------------------------------------------------------------------
# keyword argument
# def form(name,mail,ph,age,alt_ph):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age} \n alternate phone is {alt_ph}")
# form(name="aksh",mail='akshita@gmail.com',ph=7852849078,age=22,alt_ph=5678901234 )  # output will be correct 

# def form(name,mail,ph,age,alt_ph):
#     print(f"Name is {name} \nmail is {mail} \nphone is {ph} \nage is {age} \n alternate phone is {alt_ph}")
# form(mail='akshita@gmail.com',ph=7852849078,age=22,name="aksh",alt_ph=5678901234 )
# order does not matter in this 
# -------------------------------------------------------------------------
# variable length argument
# def a(*b):
#     print('b:',b)
# a('aksh','bbcc',123,81989809090)     # o/p =b: ('aksh', 'bbcc', 123, 81989809090)

# def a(**b):
#     print('b:',b)
# a(w='aksh',x='bbcc',y=123,z=81989809090)   #o/p b: {'w': 'aksh', 'x': 'bbcc', 'y': 123, 'z': 81989809090}

# ---------------------------------------------------------------------

# TASK1:

# def form(name , age , course="btech", country='india' ):
#     print(f"Name:{name} Age:{age} Course:{course}  Country:{country} ")
# form(input("enter name"),kkcourse=input("enter course:"),age=int(input("enter age:")))

# --------------------------------------------------------------
# factorial of a number using function
# def fact(n):
#     if n<0:
#         return "not valid"
#     elif n==0:
#         return 1
#     else:
#         r=1
#         for i in range(1,n+1):
#             r*=i
#         return r
# print(fact(int(input("enter"))))

# fact using recursion:
# import sys
# sys.setrecursionlimit(2000)    //to increase the limit of recursion
# def fact(n):
#     if n<0:
#         return "not valid"
#     elif n==0 or n==1:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(int(input("enter"))))    

# ------------------------------------------------------------------------

#  wap to create a function that adds minimum 2 number and max 5 numbers
# def add(l):
#     if len(l) < 2 or len(l) > 5:
#         return "invalid"
#     total = 0
#     for i in l:
#         total = total + i
#     return total
# l = eval(input("Enter list: "))
# print(add(l))

# ---------------------------------------------------------------
# wap to sum of individual digit given in number

# def add(n):
#     total=0
#     for i in n:
#         total=total+int(i)
#     return total
# n = input("enter:")
# print(add(n))


# --------------------------------------------------------
# OOPs
