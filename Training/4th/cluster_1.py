from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
# 构造数据样本点集X，并计算K-means聚类
df_ap=pd.read_csv('.\\data\\风险量化与评级.csv')
risk=list(df_ap['风险量化'])    # 123家企业的风险量化risk
print('risk',risk)  # 各企业风险量化值列表
#读取

X = np.array([[risk[i],0] for i in range(len(risk))])
print('X',X)    # risk变为二维平面内的线X  # kmeans前数据预处理
kmeans = KMeans(n_clusters=29, random_state=0).fit(X)
print('kmeans.labels_',kmeans.labels_)   # 簇列表
# kmeans

dp_ratio=pd.read_excel('.\\data\\附件3：银行贷款年利率与客户流失率关系的统计数据.xls')
ratio=list(dp_ratio['贷款年利率'])
print('ratio',ratio)    # 贷款利率列表
#读取

point=[[] for i in range(29)]
for i in range(len(risk)):
    point[kmeans.labels_[i]].append(i)  # kmeans.labels_为簇列表
print('point',point)  # 向簇容器中添加点  # 簇容器point

for i in range(len(point)):
    for j in range(len(point[i])):
        point[i][j]=risk[point[i][j]]
    point[i]=(sum(point[i]))/len(point[i])
point1=point
print('point1',point1)  # point与point1顺序相关   # 平均风险量化值列表
point=[[3], [36, 42, 49, 54, 56, 60], [9], [5, 14], [18, 21], [1, 2], [65, 78, 79, 88, 90, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122], [10, 27, 33], [0, 17], [7], [13], [24, 28, 31, 37, 47], [6], [35, 39, 40, 45, 57, 62], [82], [11], [44, 59, 63, 69, 72, 77], [8], [16, 19], [25, 26, 34, 43, 50, 51, 52, 55, 58, 61], [20, 32, 38, 53], [4], [15], [64, 66, 67, 68, 70, 71, 73, 74, 75, 76, 80, 81, 83, 84, 85, 86, 87, 89, 91, 94], [30], [12], [22, 29], [23], [41, 46, 48]]
out=[14, 6, 23, 16, 19, 1, 28, 13, 20, 11, 24, 7, 26, 21, 4, 18, 27, 8, 10, 15, 25, 3, 22, 9, 17, 2, 12, 5, 0]
# 重命名与备份

cluster=dict()
for i in range(29):
    for j in point[i]:
        cluster[j]=point1[i]
print('cluster',cluster)  # 序号-平均利率字典等价表

point2=sorted(point1,reverse=False)
print('point2',point2)  # 风险量化平均值降序，用于分配利率，值越大越好，分配的利率越低

point2_ratio=[]
for i in range(29):
    point2_ratio.append((point2[i],ratio[i]))
point2_ratio=dict(point2_ratio)
print('point2_ratio',point2_ratio)     # 风险量化平均值与利率等价表

dfw=pd.DataFrame([['E' + str(i + 1),'%.6f' % risk[i],point2_ratio[point1[kmeans.labels_[i]]]]for i in range(123)],columns=['企业代号', '风险量化', '贷款利率'])
dfw.to_csv('.\\data\\风险量化与贷款利率test.csv', index=False)
#写入