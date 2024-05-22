class parent:
    def dis1(self):
        print("parent")
class grandpa:
    def dis3(self):
        print("Grandpa")
class Child(parent,grandpa):
    def dis2(self):
        print("child")
c=Child()
c.dis2()
c.dis1()
c.dis3()


class parent:
    def dis(self):
        print("parent")
class grandpa:
    def dis(self):
        print("Grandpa")
class Child(parent,grandpa):
    def dis2(self):
        print("child")
c=Child()
c.dis2()
c.dis()


class parent:
    def dis(self):
        print("parent")
class grandpa:
    def dis(self):
        print("Grandpa")
class Child(grandpa,parent):
    def dis2(self):
        print("child")
c=Child()
c.dis2()
c.dis()
