l=[(2+3j),12,'Program','Python',False]
d={}
for i in l:
    if type(i)==str:
        a=''
        for j in i:
            if j.lower()  in 'aeiou':
                a+=j    
            d[i]=a
print(d