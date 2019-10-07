#1
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Myfunc(self):
        print("MY name is"+self.name)
p1=person("Areej",24)
p1.Myfunc()
print("*********")
#2
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Myfunc(self):
        print("MY name is"+self.name)
p1=person("Areej",24)
p1.age=40
print(p1.age)
print("*********")
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Myfunc(self):
        print("MY name is"+self.name)
p1=person("Areej",24)
del p1.age
print(p1.age)
print("*********")
class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Myfunc(self):
        print("MY name is"+self.name)
p1=person("Areej",24)
del p1
print(p1)