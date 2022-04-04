# 模拟,检验，库存量曲线
# 订货量已确定

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from random import *
sns.set(style='whitegrid')
import matplotlib
import numpy as np
matplotlib.rcParams['font.sans-serif']=['simsun'] #显示中文标签
#matplotlib.rcParams['font.sans-serif']=['Times New Roman'] #显示中文标签
matplotlib.rcParams['axes.unicode_minus']=False

def simulation(k):
    #print('我们选择了%d家供应商,他们分别是\n'%k)
    sas=0
    '''
    for i in range(k):
        r=rank[i] #供应商
        #print(i+1,r,aveSupply[r],satisfy[r])
        
        if kind[r]=='A':
            sas+=aveSupply[rank[i]]*satisfy[rank[i]]/0.6
        if kind[r]=='B':
            sas+=aveSupply[rank[i]]*satisfy[rank[i]]/0.66
        if kind[r]=='C':
            sas+=aveSupply[rank[i]]*satisfy[rank[i]]/0.72
        '''
    total=28200
    s_index=0
    s=2*28200
    for week in range(24):
        for ID in range(402):
            a=df_sO.values[ID][week+1]
            b=satisfy[ID][week]+uniform(-satisfy[ID][week]/2,satisfy[ID][week]/2)
            #print(ID,week)
            c0=loss[df_OT.values[ID][week+1]][week]
            c=c0+uniform(-c0/2,c0/2)
            #print(a,b,c)
            beta=1
            r=df_OT['供应商ID'][ID]
            if kind[r]=='A':
                #total-=aveOrder[sindex][week] * satisfy[sindex][week]/0.6*beta*loss[lindex][week]
                # total -= aveOrder[sindex][week] * satisfy[sindex][week] / 0.6 * beta * 0.95
                s+= a * b / 0.6 * beta * c
                total -= a * b / 0.6 * beta * c
            if kind[r]=='B':
                #total-=aveOrder[sindex][week] * satisfy[sindex][week]/0.66*beta*loss[lindex][week]
                #total -= aveOrder[sindex][week] * satisfy[sindex][week] / 0.66 * beta * 0.95
                s+= a * b / 0.66 * beta * c
                total -= a * b / 0.66 * beta * c
            if kind[r]=='C':
                #total-=aveOrder[sindex][week] * satisfy[sindex][week]/0.72*beta*loss[lindex][week]
                #total -= aveOrder[sindex][week] * satisfy[sindex][week] / 0.72 * beta * 0.95
                s+= a * b / 0.72 * beta * c
                total -= a * b / 0.72 * beta * c

        s-=28200
        total+=28200
        print(total)
        storage.append(3*28200-total)
    print(storage)
    '''
    for i in range(24):
        for j in range(8):
            for ID in range(402):
                Tleftall[j][i]-=df_sT.values[ID][i*8+j+1]
        print([s[i] for s in Tleftall])
    '''
    return 'True'



df_rank=pd.read_csv('.\\data\\quantization(rank only).csv')
df_ap=pd.read_csv('.\\data\\afterProcess.csv')
df_order=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='企业的订货量（m³）')
df_supply=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='供应商的供货量（m³）')
df_ls=pd.read_excel('.\\data\\附件2 近5年8家转运商的相关数据.xlsx')
df_st=pd.read_csv('.\\data\\satisfy.csv')
df_et=pd.read_csv('.\\data\\evaluateTransfer.csv')
df_es=pd.read_csv('.\\data\\evaluateSupply.csv')
df_saf=pd.read_csv('.\\data\\matrix\\satisfyForecast.csv')
df_lf=pd.read_csv('.\\data\\matrix\\lossForecast.csv')
df_sO=pd.read_csv('.\\data\\simulation&check(p4)\\simulationOrder.csv')
df_sT=pd.read_csv('.\\data\\simulation&check(p4)\\simulationTransfer.csv')
df_OT=pd.read_csv('.\\data\\simulation&check(p4)\\simulationOrderTransfer.csv')
rank=list(df_rank['rank'])
for i in range(len(rank)):
    rank[i]='S'+(3-len(str(rank[i])))*str(0)+str(rank[i])
aveOrder=[[0 for i in range(24)] for j in range(402)]    # 周平均订货量
satisfy=[[0 for i in range(24)] for j in range(402)]     # 订单满足率
kind=dict()     # 材料分类
supply=[[0 for i in range(24)] for j in range(402)]        #供应限制
loss=[[0 for i in range(24)] for j in range(8)]        #供应限制
Tleftall = [[6000 for i in range(24)] for j in range(8)] #剩余容量
'''
for i in df_ap.index:
    aveOrder[df_ap['供应商ID'][i]]=df_ap['年平均订货量'][i]/48
    satisfy[df_st['供应商ID'][i]] = df_st['周平均满足率'][i]'''
for i in df_order.index:
    kind[df_order['供应商ID'][i]]=df_order['材料分类'][i]
for i in range(402):

    sai=df_st['周平均满足率'][i]
    satisfy[i]=[sai for j in range(24)]
    sui=df_ap['年平均供货量'][i]/48
    supply[i]=[sui for j in range(24)]
    avo=df_ap['年平均订货量'][i]/48
    aveOrder[i] = [avo for j in range(24)]
    #aveOrder[i]=[np.average([df_order['W' + (3 - len(str(k*24+j+1))) * str(0) + str(k*24+j+1)][i] for k in range(0,10)]) for j in range(24)]
print(len(aveOrder),len(aveOrder[0]))
print(aveOrder[0])

    #print(ls)

    #print(loss[i])
for i in range(8):
    loss[i] = [df_et['评分'][i]/100 for j in range(24)]

#print('supply',supply)
#print('loss',loss)
#print('satisfy',satisfy)

for k in range(401,402):
    success=0
    storage=[28200*2]
    notice=simulation(k)
    print(notice)
        #plt.plot(list(range(len(storage))), storage)
    #percentage.append(success/count)
    #plt.show()

plt.plot(list(range(0,25)),storage)
plt.plot([0,25],[28200*2,28200*2])
plt.axis([-1,25,min(storage)-1000,max(storage)+1000])
#plt.title('库存量变化图', fontsize=16)
plt.xticks(np.arange(0, 26, 5),fontsize=14)
plt.xlabel('周数', fontsize=14, labelpad=0)
plt.ylabel('库存量', fontsize=14)
plt.show()
#print(satisfy[0])
#print(aveOrder[0])
#print(loss[0])

#s=sum([aveOrder[rank[index]]*satisfy[rank[index]] for index in df_ap.index])
#print(28200/s)
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
