def total(*marks,name):
    sum=0
    for i in marks:
        sum+=i
    return (f'{name} your total is {sum}')

print(total(80,32,90,43,name="Naren"))


def fun(n,*s):
    print(n)
    for i in s:
        print(i,end=' ')
fun(2,4,5,6,7,8)
