class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def dis1(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self,name,age,empid):
        super().__init__(name,age)
        self.empid=empid
    def dis(self):
        print(self.name,self.age,self.empid)
e=Employee("E1",20,'E301')
e.dis1()
e.dis()
