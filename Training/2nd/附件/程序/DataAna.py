import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
import seaborn as sns
from scipy.stats import spearmanr, pearsonr

def printline(df,i):
    row=[col[i] for col in [df[key] for key in df]]
    return row


#数据读取
df_movies=pd.read_csv(".\\data\\tmdb_5000_movies.csv")
df_credits=pd.read_csv(".\\data\\tmdb_5000_credits.csv")

#数据描述
'''
df_movies.info()

dmd=df_movies.describe()

for i in df_movies:
    print(i)
    if i in dmd.keys():
        print(dmd[i])
'''
df_budget_zero = df_movies.query('status == \'Released\'')
print(len(df_budget_zero))
print(df_budget_zero)
#df_credits=pd.read_csv(".\\data\\tmdb_5000_credits.csv")

#列数据
popularity=df_movies['popularity']
vote_average=df_movies['vote_average']
genres=df_movies['genres']
key_word=df_movies['keywords']
revenue=df_movies['revenue']
status=df_movies['status']
length=len(genres)
threshold=7

#类型
type_num=dict()
for i in range(length):
    if vote_average[i]>threshold:
        for j in json.loads(genres[i]):
            if j["name"] not in type_num.keys():
                type_num[j["name"]] = 1
            else:
                type_num[j["name"]] += 1
stn=sorted(type_num.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in stn:
    print(i[0],i[1])

print("————————————————")

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

#评分的分布
sns.displot(vote_average)
plt.show()




#打印一行
print(printline(df_movies,0))
print(spearmanr(revenue,vote_average))
print(set(status))