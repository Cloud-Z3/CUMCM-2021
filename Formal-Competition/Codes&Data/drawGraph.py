#供应量矩阵
#满足率矩阵

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#sns.set(style='whitegrid')
import matplotlib
import numpy as np
matplotlib.rcParams['font.sans-serif']=['simsun'] #显示中文标签
#matplotlib.rcParams['font.sans-serif']=['Times New Roman'] #显示中文标签
matplotlib.rcParams['axes.unicode_minus']=False
df_order=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='企业的订货量（m³）')
df_supply=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='供应商的供货量（m³）')
sort=[140,229,361,108,340,282,131,374,352,275,329,308,268,306,139,356,194,330,247,143,31,365,284,266,40,364,294,218,80,367,123,346,7,244,55,151,307,126,37,3,5,189,273,114,292,338,78,291,154,221]
matrix_supply=[[0 for i in range(24)] for j in range(402)]
matrix_satisfy=[[0 for i in range(24)] for j in range(402)]

for i in range(402):
    doi = [df_order['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1, 241)]#供应量
    dsi = [df_supply['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1, 241)]  # 供应量
    rate= [df_order['W' + (3 - len(str(j))) * str(0) + str(j)][i]/df_supply['W' + (3 - len(str(j))) * str(0) + str(j)][i]  if df_supply['W' + (3 - len(str(j))) * str(0) + str(j)][i]!=0 else 0 for j in range(1, 241)]
    for j in range(24):
        doij=[doi[k] for k in range(len(doi)) if (k-j)%24==0]
        rateij=[rate[k] for k in range(len(rate)) if (k-j)%24==0]
        msu=sum(doij)/len(doij)
        msa=sum(rateij)/len(rateij)
        matrix_supply[i][j]=msu
        matrix_satisfy[i][j] = msa
    '''
    if i==139:
        plt.subplot(4,1,1)
        plt.bar(list(range(1, 241)), doi)
        #plt.xlabel('周数', fontsize=16)
        plt.ylabel('S140',fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.axis([0,241,0,max(doi)])
        #plt.plot(list(range(1, 241)), dsi,'--.',label='供货量')
    if i==228:
        plt.subplot(4,1,2)
        plt.bar(list(range(1, 241)), doi)
        #plt.xlabel('周数', fontsize=16)
        plt.ylabel('S229',fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.axis([0, 241,0,max(doi)])
    if i==360:
        plt.subplot(4,1,3)
        plt.bar(list(range(1, 241)), doi)
        #plt.xlabel('周数', fontsize=16)
        plt.ylabel('S361',fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.axis([0, 241,0,max(doi)])
    if i==107:
        plt.subplot(4,1,4)
        plt.bar(list(range(1, 241)), doi)
        #plt.xlabel('周数', fontsize=16)
        plt.ylabel('S108',fontsize=16)
        plt.xticks(fontsize=14)
        plt.yticks(fontsize=14)
        plt.axis([0, 241,0,max(doi)])
    '''
    '''
    for j in range(len(sort)):
        if i+1==sort[j]:
            plt.subplot(10, 5, j+1)
            plt.bar(list(range(1, 241)), doi)
            # plt.xlabel('周数', fontsize=16)
            plt.title('S'+(3-len(str(i+1)))*str(0)+str(i+1),horizontalalignment='left')
            plt.ylabel('供应量', fontsize=13)
            plt.xticks(fontsize=10)
            plt.yticks(fontsize=10)
            plt.axis([0, 241, 0, max(doi)])
    '''
    for j in range(len(sort[:])):
        if i+1==sort[j]:
            plt.subplot(13, 4, j+1)
            plt.bar(list(range(1, 241)), doi)
            # plt.xlabel('周数', fontsize=16)
            plt.title('S'+(3-len(str(i+1)))*str(0)+str(i+1), fontsize=16)
            plt.xlabel('周数', fontsize=14,labelpad=0)
            plt.ylabel('供货量', fontsize=14)
            plt.xticks(np.arange(0, 241, 20),fontsize=14)
            plt.yticks(fontsize=14)
            plt.axis([-1, 242, 0, max(doi)])
            #matplotlib.pyplot.xlabel(xlabel, fontdict=None, labelpad=None, *, loc=None, **kwargs)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=None, hspace=1.5)
#plt.savefig('.\\picture\\supply3.jpg',dpi=600)
plt.show()


