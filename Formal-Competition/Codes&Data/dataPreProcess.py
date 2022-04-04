import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
df_order=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='企业的订货量（m³）')
df_supply=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='供应商的供货量（m³）')
for i in range(5):
    #plt.subplot(3,3,i+1)
    #print([df_order['W'+(3-len(str(j)))*str(0)+str(j)] for j in range(1,241)])
    #plt.plot(list(range(1,241)),np.array([df_order['W'+(3-len(str(j)))*str(0)+str(j)][i] for j in range(1,241)])) #weekg
    yearsum=[sum([df_order['W' + (3 - len(str((j-1)*48+k))) * str(0) + str((j-1)*48+k)][i] for k in range(1,49)]) for j in range(1, 6)]
    #plt.plot(list(range(1, 6)),yearsum)  #year
    print(i)
matrix=[[0,0,0,0,0,0] for i in range(len(df_supply.index))]
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
    matrix[i][1] = np.average(yearsum_s)  # 年平均供货量
    matrix[i][2] = np.var(np.array([i_s_data[j]-i_o_data[j] for j in range(0,240)]))  #供货量-订货量的方差
    matrix[i][3]=sum(yearsum_s)/sum(yearsum_o) #满足率
    matrix[i][4]=sum([1 for j in range(0,240) if (i_s_data[j]>5 and i_o_data!=0)])/240 #交易频率
    matrix[i][5]=(5*sum([x[k]*yearsum_o[k] for k in range(0,5)])-sum(x)*sum(yearsum_o))/(5*sum([k*k for k in x])-sum(x)**2)#订货量增长率 回归

dfw=pd.DataFrame(matrix,index=df_supply['供应商ID'],columns=['年平均订货量','年平均供货量','供货稳定性系数','订单满足率','交易频率','订单增长系数'])
dfw.to_csv('.\\data\\afterProcess.csv')

#plt.plot(list(range(1,403)),[i[0] for i in matrix])
sns.displot([i[1] for i in matrix],bins=50,kde=True)

#plt.plot(list(range(1,403)),[i[1] for i in matrix])
#sns.displot([i[1] for i in matrix])
plt.show()
s=0
output1=[]
output2=[]
for j in range(1,241):
    column='W'+(3-len(str(j)))*str(0)+str(j)
    o1=0
    o2=0
    for i in df_supply.index:
        if df_supply['材料分类'][i]=='A':
            o1+=df_supply[column][i]/0.6
        if df_supply['材料分类'][i]=='B':
            o1+=df_supply[column][i]/0.66
        if df_supply['材料分类'][i]=='C':
            o1+=df_supply[column][i]/0.72
        if df_order['材料分类'][i]=='A':
            o2+=df_order[column][i]/0.6
        if df_order['材料分类'][i]=='B':
            o2+=df_order[column][i]/0.66
        if df_order['材料分类'][i]=='C':
            o2+=df_order[column][i]/0.72
    output1.append(o1)
    s+=output1[-1]
    output2.append(o2)
print('ave',s/240)
print(len(list(range(1,241))))
print(len(output1))
plt.plot(list(range(1,241)),list(output1),list(range(1,241)),list(output2))
plt.show()

