# practice question

# 1
# l=['p1.py','first.txt','t3.py','tk.txt','tfk.com']
# d={}
# for i in l:
#     v=i.split('.')
#     if v[1] in d:
#         d[v[1]].append(v[0])
#     else:
#         d[v[1]]=[v[0]]
# print(d)



# 2
# a='aaabbaabcc'
# count=1
# s=''
# for i in range(len(a)):
#     if i <len(a)-1 and a[i]==a[i+1]:
#         count+=1
#     else:
#         s+=a[i]+str(count)
#         count =1
# print(s)



# nested for loop
# l=['Aditi','Sarvesh','Pradipt','Bhavik']
# v=''
# for i in l:
#     for j in i:
#         if j.lower() in 'aeiou':
#             v+=j
# print(v)



# 3
# l=[(2+3j),12,'Program','Python',False]
# d={}
# for i in l:
#     if type(i)==str:
#         a=''
#         for j in i:
#             if j.lower()  in 'aeiou':
#                 a+=j    
#             d[i]=a
# print(d)



# intermediate termination condition 

# for i in range(1,11):
#     if i==6:
#         break
#     print(i)      


# for i in range(1,11):
#     if i==6:
#         continue
#     print(i)    


# for i in range(1,11):
#     pass
# print('a')     
