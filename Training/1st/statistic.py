from matplotlib import pyplot as plt
with open("./weighted.txt","r",encoding='utf-8') as f:
    line=f.readline()
    edges=[]
    while line:
        line=f.readline()
        edge=line.split()
        edge=[int(i) for i in edge]
        edges.append(edge)
del edges[-1]

vertice=dict()
for i in edges:
    if i[0] not in vertice.keys():
        vertice[i[0]]= 1
    else:
        vertice[i[0]] +=1
    if i[1] not in vertice.keys():
        vertice[i[1]]= 1
    else:
        vertice[i[1]] +=1
key=list(vertice.keys())
key.sort()

for i in key:
    print(i,':',vertice[i])
