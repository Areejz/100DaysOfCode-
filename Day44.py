#1
class person:
     def __init__(self,fname,lname):
         self.first=fname
         self.last= lname

     def printname(self):
         print(self.first,self.last)

class steudent (person):
    def __init__(self,fname,lname):
        super().__init__(fname,lname)

x=steudent("maik","olsen")
x.printname()
print("************")
#2
class person:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def printname(self):
        print(self.first, self.last)


class steudent(person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)
        self.graduationyear=2019

x = steudent("maik", "olsen")
print(x.graduationyear)
print("************")
#3
class person:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def printname(self):
        print(self.first, self.last)


class steudent(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear=year

x = steudent("maik", "olsen",2019)
print(x.graduationyear)
print("************")
#4
class person:
    def __init__(self, fname, lname):
        self.first = fname
        self.last = lname

    def printname(self):
        print(self.first, self.last)


class steudent(person):
    def __init__(self, fname, lname,year):
        super().__init__(fname, lname)
        self.graduationyear=year
    def welcome(self):
         print("welcome",self.first,self.last,"to the class",self.graduationyear)
x = steudent("maik", "olsen",2019)
x.welcome()
