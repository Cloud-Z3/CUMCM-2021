import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
import seaborn as sns
from scipy.stats import spearmanr, pearsonr
sns.set(style='whitegrid')
def printline(df,i):
    row=[col[i] for col in [df[key] for key in df]]
    return row


#数据读取
df_mcap=pd.read_csv(".\\data\\tmdb_5000_movies&credits_ap.csv")

#数据描述

df_mcap.info()

dmd=df_mcap.describe()
for i in df_mcap:
    print(i)
    if i in dmd.keys():
        print(dmd[i])

#df_budget_zero = df_mcap.query('status == \'Released\'')

#df_credits=pd.read_csv(".\\data\\tmdb_5000_credits.csv")

#列数据
budget=df_mcap['budget']
popularity=df_mcap['popularity']
revenue=df_mcap['revenue']
runtime=df_mcap['runtime']
vote_average=df_mcap['vote_average']
vote_count=df_mcap['vote_count']
genres=df_mcap['genres']
adapted=df_mcap['adapted']
key_word=df_mcap['keywords']
crew=df_mcap['crew']
'''
print("budget",spearmanr(budget,revenue))
print("budget",pearsonr(budget,revenue))
print("popularity",spearmanr(popularity,revenue))
print("runtime",spearmanr(runtime,revenue))
print("vote_average",spearmanr(vote_average,revenue))
print("vote_count",spearmanr(vote_count,revenue))
print("adapted",spearmanr(adapted,revenue))
'''
'''
sns.jointplot(x='budget', y='revenue', data=df_mcap)
plt.show()
sns.jointplot(x='popularity', y='revenue', data=df_mcap)
plt.show()
sns.jointplot(x='vote_average',y='revenue', data=df_mcap)
plt.show()
sns.jointplot(x='runtime', y='revenue', data=df_mcap)
plt.show()
sns.jointplot(x='vote_count', y='revenue', data=df_mcap)
plt.show()
sns.jointplot(x='adapted', y='revenue', data=df_mcap)
plt.show()'''
#评分分布
sns.displot(revenue,kde=True,bins=40)
plt.show()

length=len(genres)
threshold=6.78

#导演type
#评分
'''
type_num=dict()
for i in range(length):
    for j in crew[i].split(','):
        if j not in type_num.keys():
            type_num[j] = [vote_average[i]]
        else:
            type_num[j].append(vote_average[i])
type_num2=dict()
for key in type_num.keys():
    if len(type_num[key])>=7:
        type_num2[key] = sum(type_num[key]) / len(type_num[key])

stn2=sorted(type_num2.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in stn2:
    print(i[0],'\t',i[1])
'''

print("————————————————")
#票房
type_num=dict()
for i in range(length):
    for j in crew[i].split(','):
        if j not in type_num.keys():
            type_num[j] = [revenue[i]]
        else:
            type_num[j].append(revenue[i])
type_num2=dict()
for key in type_num.keys():
    if len(type_num[key])>=7:
        type_num2[key] = sum(type_num[key]) / len(type_num[key])

stn2=sorted(type_num2.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in stn2:
    print(i[0])
print("————————————————")
'''
#主题关键词
style_num=dict()
for i in range(length):
    for j in key_word[i].split(','):
        if j not in style_num.keys():
            style_num[j] = [0,1]
            if vote_average[i] > threshold:
                style_num[j][0]+=1
        else:
            style_num[j][1] += 1
            if vote_average[i] > threshold:
                style_num[j][0]+=1
style_ratio=dict()
for key in style_num.keys():
    style_ratio[key]=style_num[key][0]/style_num[key][1]
stn1=sorted(style_ratio.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in stn1:
    print(i[0],i[1])
stn2=sorted(style_num.items(), key = lambda kv:(kv[1][0], kv[0]),reverse=True)
for i in stn2:
    print(i[0],i[1])
print(sum([j[0] for j in style_num.values()])/sum([j[1] for j in style_num.values()]))
'''
'''
#主题关键词
topic_num=dict()
for i in range(length):
    if vote_average[i]>threshold:
        for j in json.loads(key_word[i]):
            if j["name"] not in topic_num.keys():
                topic_num[j["name"]] = 1
            else:
                topic_num[j["name"]] += 1
stopcn=sorted(topic_num.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in stopcn:
    print(i[0],i[1])
'''
#评分的分布




#打印一行
print(printline(df_mcap,0))
