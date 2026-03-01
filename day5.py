# print(10,20,40,sep='@',end='@ \n')
# print(5,10,sep='@' ,end='\n')
#3
#  print('#','#',sep='%',end='% \n')
# print(1,2,3,sep='$',end='^ \n')

#3 digit number
# a=eval(input("enter number"))
# if 100<= a <=999:
#     print('a is 3 digit')
# else:
#     print('a is not 3 digit')

#check if string is >5
# a=input("enter string")
# if len(a)>5:
#     print("string length is greater than 5")
# else:
#     print('string length is less than or equal to 5')


#Check if number is zero so print ‘zero’ otherwise print ‘Not Zero’.
# a=int(input('enter number'))
# if a==0:
#     print('zero')
# else:
#     print('not zero')

#Check if person can enter club (age + ID check). If yes, print ‘Eligible’.
# a=int(input('enter age'))
# id=input('have id')
# if a>=18 and id.lower()=='yes':
#     print('can vote')
# else:
#     print('no voting')


#.	Check if number is within range 10–50 if yes print ‘In Range’ otherwise ‘Not in Range’
# a=eval(input("enter number"))
# if 10<= a <=50:
#     print('In Range')
# else:
#     print('Not In Range')


# Simple calculator (+ or -) take both number and operator symbol from user.
# a=eval(input('enter number1'))
# b=eval(input('enter number2'))
# op=input('choose operand from + or _')
# if op=='+':
#     print(a+b)
# else:
#     print(a-b)


# Check if username and password are correct if yes, print ‘Login Successful’.
# user=input('enter username')
# password=input('enter password')
# if user=='user' and password=='12345':
#     print("login successful")
# else:
#     print('error')


# Check if temperature is hot or cold.
# a=eval(input("enter temperature"))
# if a>30:
#     print('hot')
# else:
#     print('cold')


# Check if number is palindrome (basic version) or not. If yes, print ‘Palindrome’ if no, print ‘Not Palindrome’
# a=input("enter number")
# if a==a[::-1]:
#     print('palindrome')
# else:
#     print("not palindrome")




# Check if number is greater than 100.
# a=eval(input("enter number"))
# if a>100:
#     print('number is greater than 100')
# else:
#     print('Number is not greater than 100')




#Bank Loan Eligibility System
# age=int(input("enter age :"))
# income =int(input("enter income :"))
# credit =int(input("enter credit score"))
# if age>=21:
#     if income>=25000:
#         if credit >=700:
#             print("loan approved")
#         else:
#             print("Rejected (Low Credit Score)")
#     else:
#         print(" Loan Rejected (Low Income)")
# else:
#     print(" Loan Rejected (Age not eligible)")



# student marks 
# marks1=eval(input("enter marks in 1st subject"))
# marks2=eval(input("enter marks in 2nd subject"))
# marks3=eval(input("enter marks in 3rd subject"))
# avg=(marks1+marks2+marks3)/3
# if marks1>=40 and marks2>=40 and marks3>=40:
#     if avg>=75:
#         print("passed with distinction")
#     else:
#         print("pass")
# else:
#     print("fail")




# Income Tax Calculator
# income=int(input("enter income :"))
# if income > 500000:
#     if income<=1000000:
#         print("tax paid = ",income*0.2)
#     else:
#         print("tax paid = ",income*0.3)
# else:
#     if income>250000:
#         print("tax paid = " , income*0.05)
#     else:
#         print("no tax")
