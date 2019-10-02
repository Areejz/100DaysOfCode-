#1
thislist=("A","B","c","D","E","F")
print(len(thislist))
#2
thislist=["A","B","c","D","E","F"]
thislist.insert(1,"U")
print(thislist)
#3
thislist = ["A","B","c","D","E","F"]
thislist.append("Y")
print(thislist)

#4

thislist=["A","B","c","D","E","F"]
thislist.remove("E")
print(thislist)

#5
thislist=["A","B","c","D","E","F"]
thislist.pop()
print(thislist)
#6
thislist=["A","B","c","D","E","F"]
thislist.clear()
print(thislist)
#7
thislist=["A","B","c","D","E","F"]
mythislist=thislist.copy()
print(mythislist)

#8
thislist=list(("A","B","c","D","E","F"))
print(thislist)