#1
thisdict={
    "brand":"ford",
     "model": "mustang",
     "year": 1989
}
mydict=thisdict.copy()
print(mydict)
print("*******")
#2
thisdict={
    "brand":"ford",
     "model": "mustang",
     "year": 1989
}
mydict=dict(thisdict)
print(mydict)
print("*******")
#3
myfaimly={
 "child1":{
  "name":"areej",
   "year": 2019},

 "child2":{
"name":"nor",
"year": 2020},

"child3":{
"name":"bassma",
"year": 2018}

}
print(myfaimly)
print("*******")
#4
child1={
  "name":"areej",
   "year": 2019}

child2={
"name":"nor",
"year": 2020}

child3={
"name":"bassma",
"year": 2018}
myfaimly={
    "child1":child1,
     "child2":child2,
     "child3":child3

}
print(myfaimly)
print("*******")
#5
thisdict=dict(brand="ford",model="mustang",year=1989)
print(thisdict)