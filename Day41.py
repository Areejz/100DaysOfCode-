#1
class Myclass:
    x=5
print(Myclass)
p1=Myclass()
print(p1.x)
print("**********")
#2
class preson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=preson("Areej",23)
print(p1.name)
print(p1.age)
print("**********")
#3
class preson:
    def __init__(Mysillyobject,name,age):
        Mysillyobject.name=name
        Mysillyobject.age=age

    def Myfunc(abc):
      print("Hello my name is   "   +abc.name,abc.age)

p1=preson("Ali",26)
p1.Myfunc()