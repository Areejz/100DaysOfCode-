#1
thistuple=("apple","bnana","apple red")
print(thistuple)
#2
thistuple=()
print(thistuple)
#3
thistuple=(3,)
print(thistuple)
#4
thistuple=(4,8.7,9.0,5)
print(thistuple)
#5
thistuple=(4,6.7,"بايثون")
print(thistuple)
#6
thistuple=("apple","bnana","apple red")
print(thistuple[1])
#7
thistuple=("apple","bnana","apple red")
for x in thistuple:
  print(x)

#8
thistuple=["apple","bnana","apple red"]
thistuple[1]="orang"
print(thistuple)
print("**********")


#9
thistuple=["apple","bnana","apple red"]
del thistuple
print(thistuple)
print("**********")

#10
thistuple=["apple","bnana","apple red","orange"]

print(thistuple [0:3])