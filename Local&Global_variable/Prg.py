y=100
def f1():
    x=10
    global y
    print("x=",x)
    print("y=",y)
   
    y=2000
    print("Updated y=",y)
    
def f2():
    y=10
    print("y=",y)
    print("Global y=",globals()['y'])
    
    
def f3():
     print("y in F3 function is =",y)


f1()
f2()
f3()
