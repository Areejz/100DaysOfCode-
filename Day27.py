#1
a= 23
b=200
if b>a:
    print("b is greater  than a")
print("*********")
#2
a=33
b=33
if a<b:
    print("a is greater than b")
elif a==b:
    print("a and b are equal")
print("*********")
#3
a=200
b=33
if a<b:
    print("b is greater than a")
elif a==b:
    print("a and b are equal")
else:
    print("a is greater than b")
print("*********")
#4
a=200
b=33
if a<b:
    print("b is greater than a")
else:
    print("b is  not greater than a")
print("*********")
#5
a=200
b=33
if a>b: print("a is greater than b")
print("*********")

#6
a=200
b=33
print("a") if a>b else print("b")
print("*********")
#7
a=330
b=330
print("a") if a>b else print("=") if a==b  else print("b")
print("*********")
#8
a=200
b=33
c=500
if a>b and c>a:
    print("both condition are true")
print("*********")
#9
a=200
b=33
c=500
if a>b or a>c:
    print("At least one of the  condition is true")
print("*********")
#10
x=44

if x>10:
    print("Above ten,")
if x>20:
    print("and also above 20!")
else:
    print("but not above 20.")