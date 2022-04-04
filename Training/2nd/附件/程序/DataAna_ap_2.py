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

#df_mcap.info()

'''
df_mcap.set_index('adapted', inplace=True)
df_mcap.plot(kind = 'pie', # 选择图形类型
        autopct='%.1f%%', # 饼图中添加数值标签
        radius = 1.1, # 设置饼图的半径
        counterclock = False, # 将饼图的顺序设置为顺时针方向
        title = '刑事案由分布图', # 为饼图添加标题
        wedgeprops = {'linewidth': 1.5, 'edgecolor':'green'}, # 设置饼图内外边界的属性值
        textprops = {'fontsize':5, 'color':'black'},# 设置文本标签的属性值
        subplots=True)
plt.show()'''
'''
dmd=df_mcap.describe()
for i in df_mcap:
    print(i)
    if i in dmd.keys():
        print(dmd[i])
'''
#df_budget_zero = df_mcap.query('status == \'Released\'')

#df_credits=pd.read_csv(".\\data\\tmdb_5000_credits.csv")

#列数据
genres=df_mcap['genres']
release_date=df_mcap['release_date']
'''
print("budget",spearmanr(budget,revenue))
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
#sns.displot(vote_average,kde=True,bins=20)
#plt.show()

length=len(genres)
threshold=6.78

print("————————————————")

#类型

'''
style_num=dict()
for i in range(length):
    for j in genres[i].split(','):
        if j not in style_num.keys():
            style_num[j] = 1
        else:
            style_num[j] += 1
stn=sorted(style_num.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
for i in stn:
    print(i[0])
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
style=['Drama','Comedy',
'Thriller',
'Action',
'Adventure',
'Romance',
'Crime',
'Science Fiction',
'Family',
'Fantasy',
'Horror',
'Mystery',
'Animation',
'History',
'War',
'Music',
'Western',
'Documentary',
'Foreign',
]
att=len(style)
year_style_num=dict()
year=set()
for date in release_date:
    y=date.split('/')[0]
    if y not in year:
        year.add(y)
for y in year:
    year_style_num[y]=[0 for i in range(att)]
for i in df_mcap.index:
    y=release_date[i].split('/')[0]
    g=genres[i].split(',')
    for s in range(att):
        if style[s] in g:
            year_style_num[y][s]+=1
out=sorted(year_style_num.items(), key = lambda kv:(int(kv[0]), kv[1]),reverse=False)
print(out)


df=pd.DataFrame([i[1] for i in out],index=[i[0] for i in out],columns=style)
df.to_csv(".\\data\\tmdb_5000_stylewithtime.csv",index=True,header=True)
df_st=pd.read_csv(".\\data\\tmdb_5000_stylewithtime.csv")
'''
sns.pointplot(x='year',y='',hue=style,data=df_st)
'''
plotdf12=df.loc[[i[0] for i in out],style[8:16]]
plotdf12.plot(figsize=(15,15),style='-o',grid=True)
plt.show()

print(release_date[2].split('/')[0])
#打印一行
#print(printline(df_mcap,0))
