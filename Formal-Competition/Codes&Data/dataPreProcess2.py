import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df_lossrate=pd.read_excel('.\\data\\附件2 近5年8家转运商的相关数据.xlsx')
df_rank=pd.read_csv('.\\data\\quantization .csv')
df_ap=pd.read_csv('.\\data\\afterProcess.csv')
print(df_rank)
rank=list(df_rank['rank'])
for i in range(len(rank)):
    rank[i]='S'+(3-len(str(rank[i])))*str(0)+str(rank[i])
aveSupply=dict()
satisfy=dict()
for i in df_ap.index:
    aveSupply[df_ap['供应商ID'][i]]=df_ap['年平均供货量'][i]/48
    satisfy[df_ap['供应商ID'][i]] = df_ap['订单满足率'][i]
print(aveSupply)
print(satisfy)
sort=[[] for i in range(len(rank))]
for i in df_ap.index:
    sort[i].append(rank[i])
    sort[i].append(i+1)
    sort[i].append(aveSupply[rank[i]])
    sort[i].append(satisfy[rank[i]])
dfw=pd.DataFrame(sort,columns=['供应商ID','排名','周最大供货量','满足率'])
dfw.to_csv('.\\data\\quantization.csv',index=False)
'''
ave=[[] for i in range(8)]
for i in range(8):
    plt.subplot(3,3,i+1)
    #print([df_order['W'+(3-len(str(j)))*str(0)+str(j)] for j in range(1,241)])
    plt.plot(list(range(1,241)),np.array([df_lossrate['W'+(3-len(str(j)))*str(0)+str(j)][i] for j in range(1,241)])) #weekg
    #yearsum=[sum([df_lossrate['W' + (3 - len(str((j-1)*48+k))) * str(0) + str((j-1)*48+k)][i] for k in range(1,49)]) for j in range(1, 6)]
    #plt.plot(list(range(1, 6)),yearsum)  #year
    a=[df_lossrate['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1, 241)]
    for j in a:
        if j!=0:
            ave[i].append(j)
    ave[i]=sum(ave[i])/len(ave[i])

plt.show()
print(ave)
matrix=[[0,0,0,0,0] for i in range(len(df_supply.index))]
for i in df_supply.index:
    x=list(range(1,6))
    yearsum_o = [sum(
        [df_order['W' + (3 - len(str((j - 1) * 48 + k))) * str(0) + str((j - 1) * 48 + k)][i] for k in range(1, 49)])
               for j in range(1, 6)]
    yearsum_s = [sum(
        [df_supply['W' + (3 - len(str((j - 1) * 48 + k))) * str(0) + str((j - 1) * 48 + k)][i] for k in range(1, 49)])
        for j in range(1, 6)]
    i_o_data = [df_order['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1 ,241)]
    i_s_data = [df_supply['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1, 241)]
    matrix[i][0]=np.average(yearsum_o) #年平均订货量
    matrix[i][1] = np.var(np.array([i_s_data[j]-i_o_data[j] for j in range(0,240)]))  #供货量-订货量的方差
    matrix[i][2]=sum(yearsum_s)/sum(yearsum_o) #满足率
    matrix[i][3]=sum([1 for j in range(0,240) if (i_s_data[j]>5 and i_o_data!=0)])/240 #交易频率
    matrix[i][4]=(5*sum([x[k]*yearsum_o[k] for k in range(0,5)])-sum(x)*sum(yearsum_o))/(5*sum([k*k for k in x])-sum(x)**2)#订货量增长率 回归

dfw=pd.DataFrame(matrix,index=df_supply['供应商ID'],columns=['年平均订货量','供货量减订货量的方差','满足率','交易频率','订单量增长趋势'])
dfw.to_csv('.\\data\\afterProcess.csv')

#plt.plot(list(range(1,403)),[i[0] for i in matrix])
sns.displot([i[1] for i in matrix],bins=50,kde=True)

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
    print(output)
'''
