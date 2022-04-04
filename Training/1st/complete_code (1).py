#!/usr/bin/env python
# coding: utf-8

# In[12]:


#1.只用数据集test
#连接数据文档和python，将数据导入变量中
import json
path = "./test.json"
dict_raw = json.load(open(path,'r',encoding='utf-8'))


# In[10]:


#2.为每个食材标号
ingreds={}
ingreds_size=0
for i in range(len(dict_raw)):
    per_size=len(dict_raw[i]['ingredients'])
    for j in range(per_size):
        if dict_raw[i]['ingredients'][j] not in ingreds:
            name=dict_raw[i]['ingredients'][j]
            ingreds[name]=ingreds_size
            ingreds_size=ingreds_size+1
print(ingreds)


# In[11]:


#3.创建邻接矩阵
adj_matrix=[[0 for i in range(4484)] for i in range(4484)]
for i in range(4484):
    per_size=len(dict_raw[i]['ingredients'])
    for j in range(per_size):
        name=dict_raw[i]['ingredients'][j]
        num1=ingreds[name]
        for k in range(j+1,per_size):
            name=dict_raw[i]['ingredients'][k]
            num2=ingreds[name]
            adj_matrix[num1][num2]+=1
            adj_matrix[num2][num1]+=1


# In[15]:


#4.输出无权图和有权图的边集
nodes_count=4484
threshold = 2
with open("./unweighted.txt","wt",encoding='utf-8') as f:
    for i in range(nodes_count):
        for j in range(nodes_count):
            #两个原料在同一个菜肴里出现的次数大于等于2的话就建立连边
            if adj_matrix[i][j]>=threshold :
                print(i,j,file=f)
with open("./weighted.txt","wt",encoding='utf-8') as f:
    for i in range(nodes_count):
        for j in range(nodes_count):
            if adj_matrix[i][j]>0 :
                #输出文本的前两列为相连的结点（表示边），第三列为边的权重
                print(i,j,adj_matrix[i][j],file=f)


# In[16]:


#5.通过边集分别建立无权图和有权图
import networkx as nx
G_unweighted = nx.read_edgelist("./unweighted.txt")
G_weighted = nx.read_edgelist("./weighted.txt",data=[("weight", int)])


# In[18]:


#6.louvain算法分别计算无权图和有权图并输出分组
import community.community_louvain as community_louvain
louvain_unweighted_partition=community_louvain.best_partition(G_unweighted)
louvain_weighted_partition=community_louvain.best_partition(G_weighted)
print(louvain_unweighted_partition)
print()
print(louvain_weighted_partition)


# In[ ]:


#7.Girvan-Newman算法计算无权图并输出分组
comp=nx.algorithms.community.centrality.girvan_newman(G_unweighted)
print(tuple(sorted(c) for c in next(comp)))


# In[11]:


#8.Markov Clustering算法计算无权图和有权图并输出分组
import markov_clustering as mc
matrix1 = nx.to_scipy_sparse_matrix(G_unweighted)
result1 = mc.run_mcl(matrix1)           
clusters1 = mc.get_clusters(result1)
print(clusters1)
print()
matrix2 = nx.to_scipy_sparse_matrix(G_weighted)
result2 = mc.run_mcl(matrix2)           
clusters2 = mc.get_clusters(result2)
print(clusters2)


# In[ ]:




