thistuple=("A","B","C","D","E","F")
if "A" in  thistuple:
     print("yes is a in the list")


#2
thistuple=("بايثون",)*3
print(thistuple)
#3

thistuple1=(1,3,4,5,6)
thistuple2=(8,5,9,0)
thistuple3=thistuple1+thistuple2
print(thistuple3)

#4
x=(4,5,3,1)
x=x+(4,5,3)
print(x)

#5
thistuple=("A","B","C","D","E","F")
print(len(thistuple))

#6
thistuple=tuple(("A","B","C","D","E","F"))
print(thistuple)
#7
thislist=[3,6,7,'A','y']
thistuple=tuple(thislist)
print(thistuple)