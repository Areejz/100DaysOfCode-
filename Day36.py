#1
def myfunc(n):
    return lambda a:a*n
mydoubler=myfunc(2)
print(mydoubler(11))
print("**********")
#2
def myfunc(n):
    return lambda a:a*n
mytripler=myfunc(3)
print(mytripler(11))
print("**********")
def myfunc(n):
    return lambda a:a*n
mytripler=myfunc(3)
mydoubler=myfunc(2)
print(mytripler(11))
print(mydoubler(11))
print("**********")