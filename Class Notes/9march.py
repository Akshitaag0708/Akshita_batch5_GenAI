# oops
# class College:
#     c_name="jecrc"              #these c_name and c_location are attributes of class 
#     c_location="jaipur"
# s1=College()
# print(College)          #its o/p is "<class '__main__.College'>" which tells College is class
# print(s1)               #its o/p is "<__main__.College object at 0x0000021F583686E0>" which tells id at which object s1 is created and class of s1
# print(s1.c_name)         #o/p is jecrc
# s2=College()           
# s2.c_name="pu"
# print(s2.c_name)        #o/p is pu
# s1.name="aksh"            #object attribute
# print(s1.name)             # o/p will be aksh
# print(s2.name)              #this will give error "College' object has no attribute 'name'"


# TASK-1 create a class have 3 attribute and 2 object each has 3 attribute

# class Student():
#     coll="ju"
#     nationality="indian"
#     course="btech" 
# s1=Student()
# s2=Student()
# s1.name="aksh"
# s1.age=21
# s1.add="jaipur"
# s2.state="raj"
# s2.number="7890123456"
# s2.sex="female"
# print(s1.name)
# print(s1.age)
# print(s1.add)
# print(s2.state)
# print(s2.number)
# print(s2.sex)


# -------------------------------------------------------------
# constructor

# class Student():
#     coll="ju"
#     nationality="indian"
#     course="btech" 
#     def __init__(self, name,id,age):
#         self.name=name
#         self.id=id
#         self.age=age
# s1=Student("aditi",1087,21)
# print(s1.name)
# print(s1.id)
# print(s1.age)

# ----------------------------------------------------------------------
# TASK2 : task1 k object attribute init k through

# class Student():
#     coll="ju"
#     nationality="indian"
#     course="btech" 
#     def __init__(self , name , age , sex , state , number):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.state=state
#         self.number=number
#     def display(self):
#         print(f"name:{self.name} age:{self.age} gender:{self.sex} state:{self.state} phone:{self.number}")

# s1=Student("aksh",21,"male","raj","7890123456")
# s2=Student("akshita",21,"female","raj","1234567890")
# s1.display()
# s2.display()

# -------------------------------------------------------------------------
# types of method:
# object method
# class Student():
#     coll="ju"
#     nationality="indian"
#     course="btech" 
#     def __init__(self , name , age , sex , state , number):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.state=state
#         self.number=number
#     def display(self):
#         print(f"name:{self.name} age:{self.age} gender:{self.sex} state:{self.state} phone:{self.number} college:{self.coll} ,nationalitty:{self.nationality} city:{self.course}")
# # here display method is object method which can access both object and class properties
# s1=Student("aksh",21,"male","raj","7890123456")
# s1.display()

# ----------------------------------------------------
# class method and difference between class and object method
# class Student():
#     coll="ju"
#     nationality="indian"
#     course="btech" 
#     def __init__(self , name , age , sex , state , number):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.state=state
#         self.number=number
#     @classmethod
#     def class_display(cls):
#         cls.coll="pu"
#         print(f"class attributes values are : college:{cls.coll} nationality: {cls.nationality} course : {cls.course}" )
#     def display(self):
#         self.coll="muj"
#         print(f"name:{self.name} age:{self.age} gender:{self.sex} state:{self.state} phone:{self.number}")
# # here display method is object method which can access both object and class properties
# s1=Student("aksh",21,"male","raj","7890123456")
# s1.display()
# # s1.class_display()
# Student.class_display()
# print(s1.coll)                          # o/p is muj as changed s1 as s1 called display(object method called so changed for that object only)
# s2=Student("a",2,"f","gh","u8u49305094")
# print(s2.coll)                          #o/p is pu bcz changes bcz class method is called (class method called so changed for all objects)

# -------------------------------------------------------------------------------------------------------
# static method:
# class MathOperations:
#     @staticmethod
#     def add(x, y):
#         return x + y
#     @staticmethod
#     def subtract(x, y):
#         return x - y
# print(MathOperations.add(5, 3))  
# m1=MathOperations()     
# print(m1.subtract(10, 4))   

# -------------------------------------------------------------------------------------------
# 4 pillars of oops

# abstraction and encapsulation 

class Car:
    def __init__(self):
        self.acc=False
        self.clutch=False
        self.brk=False
    def start(self):
        self.acc=True
        self.clutch=True
        self.brk=False
        print("car started...")
c1=Car()
c1.start()     # the values which we made true is not shown only result is shown 

# ---------------------------------------------------------------------------------------

