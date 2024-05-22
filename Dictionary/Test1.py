d={}
for i in range(10):
    d[i]=chr(i+65)
print("Pairs")
for i,j in d.items():
    print((i,j),end=" ")
print("\nKeys")
for i in d.keys():
    print(i,end=" ")
print("\nValues")
for i in d.values():
    print(i,end=" ")
