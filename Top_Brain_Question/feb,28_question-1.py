a=int(input("enter units:"))
if a<=100:
    print(5*a)
elif 100<a<=300:
    print(5*100 + 7*(a-100))
else:
    print(5*100 + 7*200 +(a-300)*10)