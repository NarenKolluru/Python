class A:
    def dis1(self):
        print("A")
class parent(A):
    def dis2(self):
        print("parent")
class Child(parent):
    def dis3(self):
        print("child")
c=Child()
c.dis1()
c.dis2()
c.dis3()
