l=tuple(x**2 for x in range(1,10))
print(l)

m=tuple(i for i in range(10) if i%2==0)
print(m)

n=tuple("even" if i%2==0 else "odd" for i in range(10))
print(n)

a=(1,2,3,4)
b=(4,3,2,1)
o=tuple((i,j) for i in a for j in b)
print(o)

x=(tuple(int(input()) for j in range(3)) for i in range(3))
print(*x)#3x3 matrixv
