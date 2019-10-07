#1
class Libarary:
    def __init__(self,book,shelf):
        self.xbook=book
        self.yshelf=shelf

p1=Libarary(300,45)
print(p1.xbook)
print(p1.yshelf)
print("**********")
#2

class seince_section(Libarary):
    def __init__(self,book,shelf):
        super().__init__(book,shelf)
        self.name =' physics book'

    def printname(self):
        print(self.xbook,self.yshelf,self.name)

x= seince_section(300,45)
x.printname()
print("**********")
x.xbook=25
x.yshelf=4
x.printname()


