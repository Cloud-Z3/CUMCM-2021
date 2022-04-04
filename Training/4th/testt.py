import pandas as pd
from random import*
def kmeans(aList,k):
    o=[i for i in range(len(aList))]
    shuffle(o)
    center=[aList[o[i]] for i in range(k)]
    print(center)
    point=[[] for i in range(k)]
    for i in aList:
        point[findNear(i,center)].append(i)
    print(point)
    newcenter=[sum(i)/len(i) for i in point]
    while(newcenter!=center):
        print(center)
        print(newcenter)
        center=newcenter
        point = [[] for i in range(k)]
        newcenter = [sum(i) / len(i) for i in point]
    return center
def findNear(a,center):
    index=0
    distance=abs(center[index]-a)
    for i in range(len(center)):
        if abs(center[i]-a)<distance:
            index=i
            distance=abs(center[index]-a)
    return index
a=0
while(a==0):
    try:
        a=kmeans([1,2,3,4,5,6,7],2)
    except:
        a=0
        print('error')
print(a)