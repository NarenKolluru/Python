l={x:x**2 for x in range(1,10)}
print(l)

n={i:"even" if i%2==0 else "odd" for i in range(10)}
print(n)

a={1,2,3,4}
b={4,3,2,1}
o={i:(i,j) for i in a for j in b}
print(o)

x={i:[int(input()) for j in range(3)] for i in range(3)}
print(x)
