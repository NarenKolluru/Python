def mygen():
    yield 1
    yield 'a'

g=mygen()
print(next(g))
print(next(g))

for i in g:
    print(i)
