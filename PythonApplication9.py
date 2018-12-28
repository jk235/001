s=str(input())
k=s.split(" ")
k.append("end of text")
u=set(k)
print(k)
print(u)

def occ(x):
    count=0
    ocs=[]
    for element in x:
        for member in k:
            if member==element:
                count=count+1
        ocs.append([element,count])
        count=0
    return ocs





def next(x):
    nxts=[]
    p=-1
    for element in k:
        p=p+1
        if element == x:
            nxts.append(k[p+1])
    return nxts

print(next("f"))
print(occ(next("f")))
