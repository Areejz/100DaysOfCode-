#1
thisset={1,3,5,7,8}
print(thisset)
print("********")
thisset={1,3,5,7,8}
thisset.update([4,8,12])
print(thisset)
print("********")
thisset={1,3,5,7,8}
thisset.remove(8)
print(thisset)
print("********")
thisset={1,3,5,7,8}
thisset.clear()
print(thisset)
print("********")

#2
thisdict={
    "name":"pigeon",
    "type": "bird",
     "skin cover":"feathers"
}
print(thisdict)
print("********")
thisdict={
    "name":"pigeon",
    "type": "bird",
     "skin cover":"feathers"
}
x=thisdict["type"]
print(x)
print("********")
thisdict={
    "name":"pigeon",
    "type": "bird",
     "skin cover":"feathers"
}
x=thisdict["skin cover"]= "ward"
print(thisdict)