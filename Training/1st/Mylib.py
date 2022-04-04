from math import*
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from copy import *
def DisCal(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def add(a,b):
    return [a[i]+b[i] for i in range(3)]
def cor2str(cor):
    return str(cor[0])+','+str(cor[1])+','+str(cor[2])
def dijkstra(distmat,a):
    distMat=deepcopy(distmat)
    maxdis = max([max(b) for b in distMat])
    road=dict()
    l=len(distMat)
    visit=set()
    visit.add(a)
    unvisit=set()
    for i in range(l):
        if distMat[a][i]==0:
            road[i]=[i]
            continue
        if distMat[a][i]!=maxdis:
            road[i]=[a,i]
    for i in range(l):
        if i==a:
            continue
        unvisit.add(i)
    while len(unvisit)!=0:
        uv=list(unvisit)
        id=uv[0]
        minimum=distMat[a][id]
        for i in uv:
            if distMat[a][i]<minimum:
                minimum=distMat[a][i]
                id=i
        visit.add(id)
        unvisit.remove(id)
        uv=list(unvisit)
        for i in uv:
            if distMat[a][id]+distMat[id][i]<distMat[a][i]:
                distMat[a][i] = distMat[a][id] + distMat[id][i]
                distMat[i][a] = distMat[a][id] + distMat[id][i]
                roadid=road[id].copy()
                roadid.append(i)
                road[i]=roadid
    return road
def dijkstra2(distmat,a,destination):
    distMat=deepcopy(distmat)
    maxdis = max([max(b) for b in distMat])
    road=dict()
    l=len(distMat)
    visit=set()
    visit.add(a)
    unvisit=set()
    for i in range(l):
        if distMat[a][i]==0:
            road[i]=[i]
            continue
        if distMat[a][i]!=maxdis:
            road[i]=[a,i]
    for i in range(l):
        if i==a:
            continue
        unvisit.add(i)
    id=-1
    while len(unvisit)!=0 and destination!=id:
        uv=list(unvisit)
        id=uv[0]
        minimum=distMat[a][id]
        for i in uv:
            if distMat[a][i]<minimum:
                minimum=distMat[a][i]
                id=i
        visit.add(id)
        unvisit.remove(id)
        uv=list(unvisit)
        for i in uv:
            if distMat[a][id]+distMat[id][i]<distMat[a][i]:
                distMat[a][i] = distMat[a][id] + distMat[id][i]
                distMat[i][a] = distMat[a][id] + distMat[id][i]
                roadid=road[id].copy()
                roadid.append(i)
                road[i]=roadid
    return road[destination]
f=open('node4.txt')
id_cor=dict()
cor_id=dict()
id_m=dict()
for line in f:
    ele=[]
    num=[]
    for letter in line:
        if letter!=' ':
            num.append(letter)
        if letter==' ' and num!=[]:
            ele.append(int(''.join(num)))
            num=[]
    if num!=[]:
        ele.append(int(''.join(num)))
    id_cor[ele[0]]=ele[1:4]
keys=list(id_cor.keys())
deposit=[]
for i in range(1,max(keys)):
    if len(deposit)==2:
        break
    if i not in keys:
        deposit.append(i)
print(deposit)
print('node',len(keys))
value=list(id_cor.values())

for key in keys:
    cor=id_cor[key]
    cor_id[cor2str(cor)]=key

f=open('edge4.txt')
edge=[]
for line in f:
    ele=[]
    num=[]
    for letter in line:
        if letter!=' ':
            num.append(letter)
        if letter==' ' and num!=[]:
            ele.append(int(''.join(num)))
            num=[]
    if num!=[]:
        ele.append(int(''.join(num)))
    edge.append(ele)
print('edge',len(edge))
f=open('changer4.txt')
changer=[]
for line in f:
    ele=[]
    num=[]
    for letter in line:
        if letter!=' ':
            num.append(letter)
        if letter==' ' and num!=[]:
            ele.append(int(''.join(num)))
            num=[]
    if num!=[]:
        ele.append(int(''.join(num)))
    changer.append(ele)
print('changer',len(changer))
'''
print(edge)
print(len(edge))
flag=True
numb=0
for i in range(len(edge)-1):
    if edge[i][1]!=edge[i+1][0]:
        numb+=1
        flag=False
print(flag,numb)
'''


Sites=[]
ChangerP=[]
straight=[]
nodes=[]
for i in changer:
    ChangerP.append(i[0])
    ChangerP.append((i[1]))

for i in range(len(edge)-1):
    if i==0:
        s0=edge[0]
    a = edge[i][0]
    b = edge[i][1]
    c = edge[i + 1][1]
    x1 = id_cor[b][0] - id_cor[a][0]
    x2 = id_cor[c][0] - id_cor[b][0]
    y1 = id_cor[b][1] - id_cor[a][1]
    y2 = id_cor[c][1] - id_cor[b][1]
    z1 = id_cor[b][2] - id_cor[a][2]
    z2 = id_cor[c][2] - id_cor[b][2]
    if edge[i+1][0]==edge[i][1] and x1*x2+y1*y2+z1*z2!=0:
        s0.append(edge[i+1][1])
    else:
        straight.append(s0)
        s0=edge[i+1]
straight.append(s0)
count=0

stu=[]
for i in straight:
    stu.append(i)
for i in range(len(straight)):
    s0=stu[i]
    xl=[id_cor[s0[-1]][i]-id_cor[s0[0]][i] for i in range(3)]
    dis=int(DisCal(id_cor[s0[0]],id_cor[s0[-1]]))
    if dis==600 and xl[0]!=0:
        xld3=[d//3 for d in xl]
        x1=add(id_cor[s0[0]],xld3)
        x2=add(id_cor[s0[0]],2*xld3)
        Sites.append(id_cor[s0[0]])
        Sites.append(x1)
        Sites.append(x2)
        straight.append([s0[0],s0[1]])
        straight.append([s0[1],s0[2]])
        straight.append([s0[2],s0[3]])
        straight.remove(s0)

for i in changer:
    straight.append([i[0],i[1]])

for i in Sites:
    nodes.append(i)
print('sites',len(Sites))
for i in ChangerP:
    nodes.append(id_cor[i])
stu=[]
for i in straight:
    stu.append(i)
for i in stu:
    extr=[i[0]]
    for j in range(1,len(i)-1):
        if id_cor[i[j]] in nodes:
            extr.append(i[j])
    if len(extr)!=1:
        extr.append(i[-1])
        for j in range(len(extr)-1):
            straight.append([extr[j],extr[j+1]])
        straight.remove(i)
for i in range(len(straight)):
    s0=straight[i]
    if len(s0)!=2:
        straight[i]=[s0[0],s0[-1]]
'''
while True:
    flag=0
    stn=[]
    for i in straight:
        stn.append(i)
    for i in straight:
        for j in straight:
            if i!=j and i[1]==j[0] and (id_cor[i[1]] not in nodes):
                stn.append([i[0],j[1]])
                stn.remove(i)
                stn.remove(j)
                flag=1
                break
        if flag==1:
            break
    straight=stn
    if lstr==len(stn):
        break
    else:
        lstr = len(stn)
print('lstr',lstr)
'''
dep1=deposit[0]
id_cor[dep1]=[0,0,900]
cor_id[cor2str([0,0,900])]=dep1
for i in straight:
    cor1=id_cor[i[0]]
    cor2=id_cor[i[1]]
    x1=cor1[0]-0
    y1=cor1[1]-0
    z1=cor1[2]-900
    x2=cor2[0]-0
    y2=cor2[1]-0
    z2=cor2[2]-900
    if x1*y2-x2*y1==0 and x1*z2-x2*z1==0 and y1*z2-y2*z1==0 and x1*x2+y1*y2+z1*z2<0:
        straight.append([cor_id[cor2str(cor1)],dep1])
print('new_edge',len(straight))


l=len(nodes)
print('nodes',l)

#nodes 站点+变轨器端点
#rnode 所有节点
rnode=[]
for i in straight:
    if i[0] not in rnode:
        rnode.append(i[0])
    if i[1] not in rnode:
        rnode.append(i[1])

for i in range(len(rnode)):
    id_m[rnode[i]]=i

matrix=[[10000 for i in range(len(rnode))] for i in range(len(rnode))]
for s0 in straight:
    a=s0[0]
    b=s0[1]
    cor1=id_cor[a]
    cor2=id_cor[b]
    dis=int(DisCal(cor1,cor2))
    matrix[id_m[a]][id_m[b]] = dis
    matrix[id_m[b]][id_m[a]] = dis
road=dijkstra(matrix,8)
print(road)
road=dijkstra2(matrix,8,125)
print(road)

