from math import*
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from random import choice
import seaborn as sns
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

#设速度为1dm/s
#根据邻接矩阵生成距离矩阵
def disMatGet(matrix):
    distmat=deepcopy(matrix)
    l = len(distmat)
    road = dict()
    for i in range(l):
        print(i)
        roadi = dijkstra(distmat, i)
        for key in roadi.keys():
            if i == key:
                continue
            road[str(i)+','+str(key)] = roadi[key]
    return road
def find_all_path(distmat, visited, start, end):
    if start==end:
        return [[end]]
    newvisi=deepcopy(visited)
    newvisi.append(start)
    all_path=[]
    nextn=[]
    l=len(distmat)
    for i in range(l):
        if distmat[start][i]!=10000 and distmat[start][i]!=0 and (i not in newvisi):
            nextn.append(i)
    for i in nextn:
        newpath=find_all_path(distmat, newvisi, i, end)
        for i in newpath:
            path = [start]
            for j in i:
                path.append(j)
            if len(path)!=1:
                all_path.append(path)
    return all_path
#以numbda的强度产生时长t内发生的任务
def missionGen(Sites_id,nambda,time):
    n = np.random.poisson(nambda * time)
    # 生成n个[0, T]均匀分布随机数并排序
    t = [int(i) for i in np.sort(np.random.random(n) * time)]
    mission=[]
    for i in range(len(t)):
        s=choice(Sites_id)
        e=choice(Sites_id)
        while s==e:
            e=choice(Sites_id)
        mission.append([t[i],s,e])
    return mission
#侦测冲突
def confliDetec(tspan, road1, road2, rnode, id_cor):
    #tspan 轨迹二滞后轨迹一的时间
    state1=[]
    state2=[]
    if tspan<0:
        for i in range(abs(tspan)):
            state1.append([-1, -1])
    else:
        for i in range(abs(tspan)):
            state2.append([-1, -1])
    for i in range(len(road1)-1):
        time=int(DisCal(id_cor[rnode[road1[i]]],id_cor[rnode[road1[i+1]]]))
        for j in range(time):
            state1.append([road1[i],road1[i+1]])
    for i in range(len(road2)-1):
        time=int(DisCal(id_cor[rnode[road2[i]]],id_cor[rnode[road2[i+1]]]))
        for j in range(time):
            state2.append([road2[i],road2[i+1]])
    judge = False
    for i in range(min(len(state1),len(state2))):
        s1=state1[i]
        s2=state2[i]
        if s1[0]==s2[1] and s1[1]==s2[0]:
            st=s2[0]
            p = 0
            k=state1[i]
            for j in range(i,min(len(state1),len(state2))):
                if state1[j]==k:
                    print(state1[j])
                    p+=1
                else:
                    break
            judge=True
            break
    if judge==False:
        return [judge]
    else:
        return [judge,p,st]
#模拟，形成最佳路径
def pathdis(path,distmat):
    pathd=0
    for i in range(len(path)-1):
        pathd+=distmat[path[i]][path[i+1]]
    return pathd
def pathPlan(misAgoing,matrix,a,b):
    road_ab=dijkstra2(matrix,a,b)
    mintime=int(road_ab/10)
    for i in misAgoing:
        if confliDetec(t,i,road_ab)==True:
            find()
            Matrix=deepcopy(matrix)
            pathPlan()
def simulation(mission,distmat,time,rnode,id_cor):
    misAgoing = []
    avalable = [1]
    for i in range(time):
        for misa in misAgoing:
            misa[-2]+=10
            misa[-1]-=10
            if misa[-1]<=0:
                misAgoing.remove(misa)
        print(i+1)
        print(misAgoing)
        for mis in mission:
            if mis[0]==i:
                paths=find_all_path(distmat,[],mis[1],mis[2])
                print('path searched.')
                pathd=[pathdis(path,distmat) for path in paths]
                for j in range(len(paths)):
                    path=paths[j]
                    minextra=10000000
                    for misa in misAgoing:
                        cd=confliDetec(misa[-2],misa[1],path,rnode,id_cor)
                        if len(cd)==1:
                            continue
                        else:
                            print('conflict searched.')
                            if minextra>min(minextra,cd[1]):
                                st=cd[2]
                                minextra=min(minextra,cd[1])
                    if minextra==10000000:
                        continue
                    else:
                        paths[j].append([st,minextra])
                        pathd[j]+=minextra
                minl=10000000
                idex=0
                for j in range(len(pathd)):
                    if pathd[j]<minl:
                        minl=pathd[j]
                        idex=j
                p=paths[idex]
                if isinstance(p[-1],list):
                    mis.insert(1,p[0:-1])
                else:
                    mis.insert(1, p)
                del mis[2:4]
                mis.append(0)
                mis.append(pathd[idex]-0)
                misAgoing.append(mis)


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
Sites_id=[id_m[cor_id[cor2str(i)]] for i in Sites]

mission=missionGen(Sites_id,0.2,500)
for i in mission:
    print(i)

simulation(mission,matrix,500,rnode,id_cor)