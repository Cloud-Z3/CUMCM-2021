import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr, pearsonr

from math import *
def f(x):
    if x>0.4 and x<0.6:
        return 4*x-1.5
    if x<=0.4:
        return x/4
    if x>=0.6:
        return x/4+0.9-0.6/4
def topsis(weight):
    df_ap=pd.read_csv('.\\data\\afterPreProcesss.csv')
    df_info=pd.read_excel(".\\data\\附件1：123家有信贷记录企业的相关数据.xls",sheet_name='企业信息')
    colum=['企业实力','盈利能力','供销关系','经营稳定性','发展潜力']
    ind=[5,1/5,1,1,5]


    for k in range(len(colum)):
        c=colum[k]
        minimum=min(df_ap[c])
        maxmum=max(df_ap[c])
        for i in df_ap.index:
            if k==1:
                df_ap[c][i]=f((maxmum-df_ap[c][i])/(maxmum-minimum))
            else:
                df_ap[c][i]=((maxmum-df_ap[c][i])/(maxmum-minimum))**ind[k]

    '''
    for k in range(len(colum)):
        c=colum[k]
        minimum=min(df_ap[c])
        maxmum=max(df_ap[c])
        for i in df_ap.index:
            df_ap[c][i]=(maxmum-df_ap[c][i])/(maxmum-minimum)
    '''

    for k in range(len(colum)):
        c=colum[k]
        s=sqrt(sum(i**2 for i in df_ap[c]))
        for i in df_ap.index:
            df_ap[c][i]=df_ap[c][i]/s


    dcba=[24,34,38,27]
    ass=['D','C','B','A']

    optimal=[max(df_ap[c]) for c in colum]
    unoptimal=[min(df_ap[c]) for c in colum]
    sort1=dict()
    sort2=dict()
    sort=dict()

    for i in df_ap.index:
        sort1[i]=sqrt(sum([((optimal[k]-df_ap[colum[k]][i])**2)*weight[k] for k in range(5)]))
        sort2[i] = sqrt(sum([((unoptimal[k] - df_ap[colum[k]][i]) ** 2) * weight[k] for k in range(5)]))
        sort[i]=sort2[i]/(sort1[i]+sort2[i])
    out=sorted(sort.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
    print(out)
    assign=[0 for i in range(123)]
    counter=0
    index=0
    index2=0
    while(index<4):
        bounder=dcba[index]
        while(counter<bounder):
            assign[out[index2][0]]=ass[index]
            counter+=1
            index2+=1
        index+=1
        counter=0
    credit=df_info['信誉评级']
    count=0

    for i in range(123):
        if(credit[i]==assign[i]):count+=1
        print('E'+str(i+1),'\t','%.6f'%sort[i],'\t',assign[i])
    dfw=pd.DataFrame([['E'+str(i+1),'%.6f'%sort[i],assign[i]] for i in range(123)],columns=['企业代号','风险量化','风险评级'])
    dfw.to_csv('.\\data\\风险量化与评级.csv',index=False)
    for i in range(123):
        credit[i] = ord(credit[i]) - ord('A') + 1
        assign[i] = ord(assign[i]) - ord('A') + 1
        print(credit[i],'\t',assign[i])
    print(spearmanr(credit,assign))
    matrix=[[0 for i in range(4)] for i in range(4)]


    for i in range(123):
        matrix[assign[i]-1][credit[i]-1]+=1
    for i in matrix:
        print(i)
    mat=pd.DataFrame(data=matrix)
    for i in range(4):
        a=sum(matrix[i])
        for j in range(4):
            matrix[i][j]=matrix[i][j]/a
    for i in matrix:
        print(i)
    sns.heatmap(mat, square=True, linewidths=0.02, annot=True)
    plt.show()
    return count/123,spearmanr(credit,assign)

if __name__=="__main__":
    print(topsis([0.7,0.3,0,0,0]))