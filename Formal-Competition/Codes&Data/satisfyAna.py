import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df_order=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='企业的订货量（m³）')
df_supply=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='供应商的供货量（m³）')
df_ap=pd.read_csv('.\\data\\afterProcess.csv')

mulMonth_o=[]
for i in df_order.index:
    monthSum_o=[sum([df_order['W' + (3 - len(str((j-1)*4+k))) * str(0) + str((j-1)*4+k)][i] for k in range(1,5)]) for j in range(1, 61)]
    mulMonth_o.append(monthSum_o)
mulMonth_s=[]
for i in df_supply.index:
    monthSum_s=[sum([df_supply['W' + (3 - len(str((j-1)*4+k))) * str(0) + str((j-1)*4+k)][i] for k in range(1,5)]) for j in range(1, 61)]
    mulMonth_s.append(monthSum_s)
mulMonth_rate=[]
matrix=[['S'+(3-len(str(j+1)))*str(0)+str(j+1),df_ap['订单满足率'][j],0,0] for j in range(0,402)]
for i in range(0,402):
    rate=[mulMonth_s[i][j]/mulMonth_o[i][j] for j in range(0,60) if mulMonth_o[i][j]!=0]
    rateweek=[df_supply['W'+(3-len(str(j)))*str(0)+str(j)][i]/df_order['W'+(3-len(str(j)))*str(0)+str(j)][i] for j in range(1,241) if df_order['W'+(3-len(str(j)))*str(0)+str(j)][i]!=0]
    #print(rate)
    print(sum(rate)/len(rate))
    matrix[i][2]=sum(rate)/len(rate)
    matrix[i][3] = sum(rateweek) / len(rateweek)

    #plt.subplot(6,6,i+1)
    #plt.hist(np.array(rate),bins=20)
    #pd.Series(rate).plot(kind='hist', bins=20, color='steelblue', edgecolor='black', density=True, label='直方图')
    #pd.Series(rate).plot(kind = 'kde', color = 'red', label = '核密度图')

plt.show()

dfw=pd.DataFrame(matrix,columns=['供应商ID','年平均满足率','月平均满足率','周平均满足率'])
dfw.to_csv('.\\data\\satisfy.csv',index=False)
#dfw=pd.DataFrame(matrix,index=df_supply['供应商ID'],columns=['年平均供货量','供货稳定性系数','订单满足率','交易频率','订单增长系数'])
#dfw.to_csv('.\\data\\afterProcess.csv')
'''
print(matrix)
list2=[]
for i in range(len(matrix)):
    list2.append(matrix[i][1])
print(list2)
sns.displot(list2,bins=50,kde=True)
'''

#plt.plot(list(range(1,403)),[i[0] for i in matrix])
#sns.displot([i[2] for i in matrix],bins=50,kde=True)

#plt.plot(list(range(1,403)),[i[1] for i in matrix])
#sns.displot([i[1] for i in matrix])
plt.show()

for j in range(1,241):
    column='W'+(3-len(str(j)))*str(0)+str(j)
    output=0
    df=df_supply
    for i in df.index:
        if df['材料分类'][i]=='A':
            output+=df[column][i]/0.6
        if df['材料分类'][i]=='B':
            output+=df[column][i]/0.66
        if df['材料分类'][i]=='C':
            output+=df[column][i]/0.72
    #print(output)

