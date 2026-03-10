# task1 
# class Bank:
#     balance=0
#     def withdraw(self,amt):
#         if self.balance<amt:
#             print("unsuccessful transaction")
#         else:
#             self.balance-=amt
#             print(f"{amt} debitted successfully")
#     def deposit(self,amt):
#         self.balance+=amt
#         print(f"{amt} credited successfully")
#     def show_balance(self,id):
#         print(f"current balance:{self.balance}")
#     def __init__(self,name,id,initial_deposit):
#         self.name=name
#         self.id=id
#         self.balance+=initial_deposit
# c1=Bank("aksh",1234,5000)
# c1.withdraw(8000)
# c1.deposit(1000)
# c1.show_balance(1234)
        
# -------------------------------------------------------------------
# inheritance
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         print("Animal name:", self.name)
# class Dog(Animal):
#     def sound(self):
#         print(self.name, "barks")
# d = Dog("Buddy")
# d.info()      
# d.sound()

# -----------------------------------------------------------
# super keyword
# Parent Class: Animal
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def info(self):
#         print("Animal name:", self.name)
# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)   
#         self.breed = breed
#     def details(self):
#         print(self.name, "is a", self.breed)
# d = Dog("Buddy", "Golden Retriever")
# d.info()      
# d.details()   


# ------------------------------------------------------------------------------------------------
# task 2
# class Employee:
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
# class Manager(Employee):
#     def __init__(self,name,salary,dept):
#         super().__init__(name,salary)
#         self.dept=dept
#     def details(self):
#         print(f"name: {self.name} ,salary:{self.salary} ,department:{self.dept}")
# m1=Manager("aksh",300000,"finance")
# m1.details()


# -------------------------------------------------------------------------------------------------
# @property decorator:
# class A():
#     def __init__(self,name):
#         self.name=name
#     @property
#     def info(self):
#         print(self.name)
# b=A("Aksh")
# b.info   


# ------------------------------------------------------------------------------------
# polymorphism
# method overloading 
# class Calculator:
#     def multiply(self, a,b):
#         result = a * b
#         return result
#     def multiply(self , a,b,*args):
#         result=a*b
#         for i in args:
#             result*=i
#         return result

# c = Calculator()
# print(c.multiply(2, 3))       
# print(c.multiply(2, 3, 4))
# ------------------------------------------------------------------------------
# method overriding
# class Payment:
#     def processPayment(self):
#         print("Processing pmt")

# class CreditCard(Payment):
#     def processPayment(self , amt):
#         print(f"Credit Card Payment Successful of {amt}")

# class UPI(Payment):
#     def processPayment(self,amt):
#         print(f"UPI Payment Successful of {amt}")

# class Cash(Payment):
#     def processPayment(self,amt):
#         print(f"Cash Payment Successful of {amt}")

# pmts = [CreditCard(),UPI(),Cash()]
# for payment in pmts:
#     payment.processPayment(300)
    

# ----------------------------------------------------------------------------
# Task:3
# class Circle:
#     radius=eval(input("enter radius"))
#     def area(self):
#         print(f"area : {3.14*self.radius*self.radius}")
#     def perimeter(self):
#         print(f"perimeter :{2*3.14*self.radius}")
# c=Circle()
# c.area()
# c.perimeter()

# ---------------------------------------------------------------------------------
# file handling:
# only write
# file = open('temp.txt','w')
# # file.write('first line')
# # file.write('new data')          # overwrite the above 'first line'
# # file.writelines(['first line ','second line'])   # both will be in same line so we use \n 
# file.writelines(['first line \n ','second line']) 
# file.close()               
# ----------------------------------------------------------------------------
# only read
# file=open('temp.txt','r')
# print(file.read())      #print data of file as it is
# print(file.readline())    # only first line will be printed 
# print(file.readline())     # one line space b/w this and pvs line and second line will be printed 
# if we want to print whole file using readline() then you have to pass it till no. of lines
# print(file.readlines())    #o/p=['first line \n', ' second line']



# ============

# print(file.read())      # if we pass all 3 read together then this will first print all data and now interpreter is pointing at last
# print(file.readline())    #as interpreter is pointing at last nothing to print so empty line
# print(file.readline())   #as interpreter is pointing at last nothing to print so empty line
# print(file.readlines())         #as interpreter is pointing at last nothing to print so empty list
# file.close()

# ------------------------------------------------------------------------------
# write +read

# file = open('temp.txt','w+')
# file.writelines(['first line \n ','second line']) 
# # print(file.read())     #this will not give any output as not it is not pointing to any line
# file.seek(0)     # send to 0 index line  , seek() is used to make interpreter point to specific index and inside it we pass index value
# print(file.read())     # now we will be able to see the content 
# file.close()


# -----------------------------------------------------
# append + read
# file = open('temp.txt','a+')
# file.write("\n hii")           #this will append data at last     
# file.writelines(['first line \n ','second line']) 
# file.seek(0)
# print(file.read())
# file.close()

# this is all about text files 
# ------------------------------------------------------------------------------
# csv files(comma seperat value)
# to work with csv file csv package is important 
# write operations 

# import csv
# from datetime import date

# file=open('temp.csv','a+')
# w=csv.writer(file)

# w.writerow(['DATE','CATEGORY','AMOUNT'])    # colums
# w.writerows(
#     [
#         [date.today(),'Travel',2000],
#         [date.today(),'food',200],
#         [date.today(),'drinks',3000]
#     ]
# )

# file.close()


# -------------------------------
# read operations
# import csv
# from datetime import date

# file=open('temp.csv','a+')
# r=csv.reader(file)

# # print(r)     # this will give o/p ='<_csv.reader object at 0x000001415B81B1C0>' means id of object so we use list to print
# file.seek(0)
# print(list(r))
# file.close()
# ----------------------------------------------------------------------------------

# dumps(): used for encryption
# loads(): used for decryption 
# json

# import json
# file=open('temp.txt','a+')
# data={
#     'full-name':'Akshita Agarwal',
#     'id':1234,
#     'password':'***************'
# }
# # print(f"original data:{data}")
# # print(f"type of original data: {type(data)}")    # its type is dictionary

# enc_data=json.dumps(data)
# # print(f"encrypted data:{enc_data}")
# # print(f"type of encrypted data: {type(enc_data)}")   # its type will be string 

# # dec_data=json.loads(enc_data)
# # print(f"decrypted data:{dec_data}")
# # print(f"type of decrypted data: {type(dec_data)}")   # its type will be again dictionary  

# # file.write(enc_data)    # this will write data in string format as encrypted data is of string type
# file.seek(0)
# enc=file.read()
# print(enc)
# print(type(enc))

# org_data=json.loads(enc_data)
# print(org_data,type(org_data))
# file.close()

# ----------------------------------------------------------------------
# pickle
# same as json jaha jaha json ko kia tha vha pickle krna h 
# yh encryption bytes m krta h to mode wb+ or wb or rb or rb+ OR ab or ab+  hoga 

# import pickle
# file=open('temp.txt','ab+')
# data={
#     'full-name':'Akshita Agarwal',
#     'id':1234,
#     'password':'***************'
# }
# enc_data=pickle.dumps(data)
# print(f"encrypted data:{enc_data}")
# print(f"type of encrypted data: {type(enc_data)}")   

# dec_data=pickle.loads(enc_data)
# print(f"decrypted data:{dec_data}")
# print(f"type of decrypted data: {type(dec_data)}")  

# # file.write(enc_data)  
# file.seek(0)
# enc=file.read()
# print(enc)
# print(type(enc))

# file.close()

# -------------------------------------------------------
