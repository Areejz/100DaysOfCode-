#1
fruits={"apple","banana","cherry"}
for x in fruits:
    print(x)
print("*************")
#2
for x in "apple":
    print(x)
print("*************")
#3
fruits=["apple","banana","cherry"]
for x in fruits:
    print(x)
    if x == "banana":
     break
print("*************")
#4
fruits=["apple","banana","cherry"]
for x in fruits:
     if x == "banana":
      break
     print(x)
print("*************")
#5
fruits=["apple","banana","cherry"]
for x in fruits:
     if x == "banana":
      continue
     print(x)

