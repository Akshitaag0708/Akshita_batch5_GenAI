# task1
# store same extension name in one list where extension will be key and list will be value
# l=['p1.py','first.txt','t3.py','tk.txt','tfk.com']
# d={}
# for i in l:
#     v=i.split('.')
#     if v[1] in d:
#         d[v[1]].append(v[0])
#     else:
#         d[v[1]]=[v[0]]
# print(d)


# task2
# count occurance writ letter then occurance like aabbccc=a2b2c3
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


# task3
# store in dic where key will be string and value will be vowels in that string
l=[(2+3j),12,'Program','Python',False]
d={}
for i in l:
    if type(i)==str:
        a=''
        for j in i:
            if j.lower()  in 'aeiou':
                a+=j    
            d[i]=a
print(d)
