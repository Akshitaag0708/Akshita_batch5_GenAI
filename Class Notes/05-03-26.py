
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
print(dir(tuple))
