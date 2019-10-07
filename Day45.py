#1
mytuple=('apple','banana','cherry')
myit=iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
print("*************")
#2
mystr="banana"
myit=iter(mystr)
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print("*************")
#3
mytuple=('apple','banana','cherry')
for x in mytuple:
        print(x)
print("*************")
#4
mystr=("banana")
for x in mystr:
    print(x)
print("*************")
class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        x=self.a
        self.a+=1
        return x
myclass=mynumber()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print("*************")
#5
class mynumber:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        if self.a <=20:
          x=self.a
          self.a+=1
          return x
        else:
            raise StopIteration
myclass=mynumber()
myiter=iter(myclass)
for x in myiter:
     print(x)