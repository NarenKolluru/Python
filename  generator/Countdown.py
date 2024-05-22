def count(n):
    for i in range(n,-1,-1):
        yield i

vals=count(5)
for j in vals:
    print(j)
