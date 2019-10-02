#1

def power(x,y):
    if y==1:
        return x
    else:
        return x*power(x,y-1)
print(power(5,3))
print("************")
#2
n_list=[-4,-6,-5,-1,2,3,7,9,88]
x=list(filter(lambda z: z > 0,  n_list))
print(x)



