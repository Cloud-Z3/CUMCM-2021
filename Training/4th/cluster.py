from sklearn.cluster import KMeans
import numpy as np
import pandas as pd
# 构造数据样本点集X，并计算K-means聚类
df_ap=pd.read_csv('.\\data\\风险量化与评级.csv')
risk=list(df_ap['风险量化'])
X = np.array([[risk[i],0] for i in range(len(risk))])
kmeans = KMeans(n_clusters=29, random_state=0).fit(X)
dp_ratio=pd.read_excel('.\\data\\附件3：银行贷款年利率与客户流失率关系的统计数据.xls')
ratio=list(dp_ratio['贷款年利率'])

print(ratio)
# 输出及聚类后的每个样本点的标签（即类别），预测新的样本点所属类别
point=[[] for i in range(29)]
for i in range(len(risk)):
    point[kmeans.labels_[i]].append(i)
print(point)
ave=[sum(i)/len(i) for i in point]
print(ave)
out=sorted(range(len(ave)), key=lambda k: ave[k])
print(out)
cluster=dict()
for o in range(len(out)):
    for i in point[o]:
        cluster[i]=o
print(cluster)
stopcn=sorted(cluster.items(), key = lambda kv:(kv[0], kv[1]),reverse=False)
print(stopcn)
for i in df_ap.index:
    print(risk[i],ratio[stopcn[i][1]])
print(kmeans.predict([[1,0],[2,0],[3,0]]))
dfw = pd.DataFrame([['E' + str(i + 1), '%.6f' % risk[i], ratio[stopcn[i][1]]] for i in range(123)],
                   columns=['企业代号', '风险量化', '贷款利率'])
dfw.to_csv('.\\data\\风险量化与贷款利率.csv', index=False)
