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