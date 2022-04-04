import pandas as pd
from random import*
def kmeans(aList,k):
    o=[i for i in range(len(aList))]
    shuffle(o)
    center=[aList[o[i]] for i in range(k)]
    point=[[] for i in range(len(aList))]
    for i in aList:
        point[findNear(i,center)].append(i)
    newcenter=[sum(i)/len(i) for i in point]
    while(newcenter!=center):
        center=newcenter
        point = [[] for i in range(len(aList))]
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
df_ap=pd.read_csv('.\\data\\风险量化与评级.csv')
risk=list(df_ap['风险量化'])
print(risk)
