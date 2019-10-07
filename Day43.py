#1
class person:
    def __init__(self,fname,lname):
        self.first=fname
        self.last=lname
    def printname(self):
       print(self.first,self.last)

x=person("areej","z")
x.printname()
print("***********")
#2
class person:
    def __init__(self,fname,lname):
        self.first=fname
        self.last=lname
    def printname(self):
       print(self.first,self.last)
class student(person):
    pass
x=person("mike","olsen")
x.printname()
print("***********")
#3
class person:
    def __init__(self,fname,lname):
        self.first=fname
        self.last=lname
    def printname(self):
       print(self.first,self.last)
class student(person):
       def __init__(self,fname,lname):
           person.__init__(self,fname,lname)

x=person("mike","olsen")
x.printname()
print("***********")





