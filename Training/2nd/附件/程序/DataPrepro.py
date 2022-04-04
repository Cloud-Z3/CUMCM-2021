import matplotlib.pyplot as plt
import pandas as pd
import json
import numpy as np
import seaborn as sns
from scipy.stats import spearmanr, pearsonr

def printline(df,i):
    row=[col[i] for col in [df[key] for key in df]]
    return row
def deleteRow(df,attribute):
    df_att=df[attribute]
    l=len(df_att)
    dellist=[]
    for i in df.index:
        if df_att[i]==0 or df_att[i]=='NaN':
            dellist.append(i)
    df.drop(dellist,axis=0,inplace=True)
def jsonPro(df,attribute,key):
    df_att=df[attribute]
    for i in df.index:
        s=','.join([j[key] for j in json.loads(df_att[i])])
        if s=='':
            df.drop([i], axis=0, inplace=True)
        else:
            df.loc[i,attribute]=s
def isadapted(string):
    if 'adapted' in string or 'based on' in string:
        return True
    return False




#数据读取
df_mc=pd.read_csv(".\\data\\tmdb_5000_movies&credits.csv")
df_mc['adapted']=0
for i in df_mc.index:
    if isadapted(df_mc.loc[i,'keywords']) or isadapted(str(df_mc.loc[i,'overview'])) or isadapted(str(df_mc.loc[i,'tagline'])):
        df_mc.loc[i, 'adapted']=1
print(df_mc)

df_budget_zero = df_mc.query('budget == 0 or budget == \'NaN\'')
col_list=['budget','popularity','release_date','revenue','runtime','vote_average','vote_count']
for col in col_list:
    print(col)
    deleteRow(df_mc,col)
print(df_mc)

jsonPro(df_mc,'genres','name')
print(1)

jsonPro(df_mc,'keywords','name')
print(2)

jsonPro(df_mc,'cast','character')
print(3)

df_att = df_mc['crew']
for i in df_mc.index:
    s = ','.join([j['name'] for j in json.loads(df_att[i]) if j['job']=='Director'])
    if s == '':
        df_mc.drop([i], axis=0, inplace=True)
    else:
        df_mc.loc[i, 'crew'] = s
print(4)
print(df_mc)
''''''
df_mc.drop('overview',axis=1,inplace=True)
df_mc.drop('tagline',axis=1,inplace=True)
df_mc.drop('status',axis=1,inplace=True)
df_mc.drop('id',axis=1,inplace=True)
df_mc.to_csv(".\\data\\tmdb_5000_movies&credits_ap.csv",index=False,header=True)
#数据描述
'''
df_movies.info()

dmd=df_movies.describe()

for i in df_movies:
    print(i)
    if i in dmd.keys():
        print(dmd[i])
'''
'''

df_budget_zero = df_mc.query('budget == 0 or budget == NaN')
print(len(df_budget_zero))
print(df_budget_zero)
#df_credits=pd.read_csv(".\\data\\tmdb_5000_credits.csv")

#列数据
popularity=df_mc['popularity']
vote_average=df_mc['vote_average']
genres=df_mc['genres']
key_word=df_mc['keywords']

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
'''

#打印一行
#print(printline(df_mc,0))
