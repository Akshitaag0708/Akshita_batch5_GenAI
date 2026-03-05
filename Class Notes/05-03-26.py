
# task1: to extract kiv from bhavik 
# d={'a':'bhavik' , 'd':23 ,'c':'jaipur'}
# print(d['a'][-1:-4:-1])


# task2: print 10 to 1 using while
# i=10
# while(i>0):
#     print(i)
#     # i-=1



# TOPIC : pattern printing
# for i in range(1,4):
#     for j in range(1,4):
#         print('*')        // this will give output in vertical way all 8 * will be vertical
#         //so to solve this we need to add end

# for i in range(1,4):
#     for j in range(1,4):
#         print('*',end=' ')  //now only passing end will print all 8 * in same line 
# # so to solve this we need to pass print() after every row


# for i in range(1,4):
#     for j in range(1,4):
#         print('*',end=" ")
#     print()    //this will print perfectly


# task3 : to print # pattern by taking input of rows and columns from user
# a=int(input("enter rows"))
# b=int(input("enter columns"))
# for i in range(a):
#     for j in range(b):
#         print("#",end=' ')
#     print()



# task 4:   to print # in primary diagonal 
# for i in range(0,3):
#     for j in range(0,3):
#         if (i==j):
#             print("#",end=' ')
#         else:
#             print(" ",end=' ')
#     print()


# task 5: to print # in lower triangle , @ in upper triangle and * in primary diagonal 
# for i in range(0,6):
#     for j in range(0,6):
#         if (i==j):
#             print("*",end=' ')
#         elif i<j:
#             print("@",end=' ')
#         else:
#             print("#",end=' ')
#     print()



# task 6:to print in secondary diagonal
#  for index start from 0
# a=int(input("rows:"))
# b=int(input("columns:")) 
# for i in range(0,a):
#     for j in range(0,b):
#         if (i+j==a-1):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()

# for index start from 1
# a=int(input("rows:"))
# b=int(input("columns:")) 
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if (i+j==a+1):
#             print("*",end=' ')
#         else:
#             print(" ",end=' ')
#     print()


# task:7 to print # in secondary diagonal , @ in lower triangle and * in upper triangle
 
# a=int(input("rows:"))
# b=int(input("columns:")) 
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if (i+j==a+1):
#             print("#",end=' ')
#         elif i+j<a+1:
#             print("*",end=' ')
#         else:
#             print('@',end=' ')
#     print()


# task 8
# a=int(input("rows:"))
# b=int(input("columns:")) 
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if (i+j==a+1):
#             print("#",end=' ')
#         elif i+j==a-1:
#             print("*",end=' ')
#         elif i+j==2*a:
#             print("a",end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# task :9
# a=int(input("rows:"))
# b=int(input("columns:")) 
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if (i+j==a+1):
#             print("#",end=' ')
#         elif i==j:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()



# functions:
 
#  task 10:create a function which takes 2 values as input and return their product

#  no argument ,no return 
# def prod():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     print(a*b)
# prod()

# with argument and no return 
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# def prod(a,b):
#     print(a*b)
# prod(a,b)  //if we have values
# prod(int(input()),int(input()))

# without argument and with return
# def prod():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     return a*b
# print(prod())


# with argument and with return 
# a=int(input("enter a:"))
# b=int(input("enter b:"))
# def prod(a,b):
#     return a*b
# print(prod(a,b))


# def prod():
#     a=int(input("enter a:"))
#     b=int(input("enter b:"))
#     print(a*b)
#     # return
# print(prod())       
# //if we pass function in print and return has no value with it then none will also come in output
# whenever we pass only function to print then also none will come 
# return k sath value hoti h tb none nhi aaega print m call k baad bhui 


# task 11 : to return negative values from list using function
# l=eval(input("input the list"))
# def neg(l):
#     a=[]
#     for i in l:
#         if i <0:
#             a.append(i)
#     return a
# print(neg(l))


# task 12 : local scope vs global scope 
# a=10
# def b():
#     a=15
#     print(a)
# print(b())
# print(a)       // now value will be not beupdated to 15  


# a=10
# def b():
#     global a
#     a=15
#     print(a)
# print(b())
# print(a)       // now value will be updated to 15 bcz global a is used in function 


a=9
def f1():
    global a
    a=20
    b=2000
    def f2():
        nonlocal b    
        # we can access b in nested function but not change it so to change we use nonlocal keyword 
        # nonlocal b will be used to change value of variable of function into nested function 
        b=2
    print(b)
print(a)