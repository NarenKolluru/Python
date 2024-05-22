s=input()
d={}
for i in s:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1
for i,j in d.items():
    print("{}-{}".format(i,j),end=',')
