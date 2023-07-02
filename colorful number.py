lst1=[]
lst2=[]
x="326"
lst1.extend(x)
for i in range(0,len(lst1)):
     lst1[i]=int(lst1[i])
for i in range(0,len(lst1)):
    for j in range(i+1,len(lst1)):
        y=lst1[i]*lst1[j]
        lst2.append(y)
if len(lst1)==4:
    for i in range(0,1):
        for j in range(i+1,len(x)):
            for k in range(j+1,len(x)):
                y=lst1[i]*lst1[j]*lst1[k]
                lst2.append(y)
y=1
for i in lst1:
    y=y*i
lst2.append(y)
cmp=0
for i in range(0,len(lst2)):
    for j in range(i+1,len(lst2)):
        if lst2[i]==lst2[j]:
            cmp+=1
            break
if cmp==0:
    print("True")
else:
    print("False")