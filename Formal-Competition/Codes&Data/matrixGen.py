#供应量矩阵
#满足率矩阵
#损耗率矩阵
import pandas as pd
df_order=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='企业的订货量（m³）')
df_supply=pd.read_excel('.\\data\\附件1 近5年402家供应商的相关数据.xlsx',sheet_name='供应商的供货量（m³）')
df_ls=pd.read_excel('.\\data\\附件2 近5年8家转运商的相关数据.xlsx')
matrix_supply=[[0 for i in range(24)] for j in range(402)]
matrix_satisfy=[[0 for i in range(24)] for j in range(402)]
matrix_loss=[[0 for i in range(24)] for j in range(8)]
for i in range(402):
    doi = [df_order['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1, 241)]#供应量
    rate= [df_order['W' + (3 - len(str(j))) * str(0) + str(j)][i]/df_supply['W' + (3 - len(str(j))) * str(0) + str(j)][i]  if df_supply['W' + (3 - len(str(j))) * str(0) + str(j)][i]!=0 else 0 for j in range(1, 241)]
    for j in range(24):
        doij=[doi[k] for k in range(len(doi)) if (k-j)%24==0]
        rateij=[rate[k] for k in range(len(rate)) if (k-j)%24==0]
        msu=sum(doij)/len(doij)
        msa=sum(rateij)/len(rateij)
        matrix_supply[i][j]=msu
        matrix_satisfy[i][j] = msa
for i in range(8):
    lsi = [df_ls['W' + (3 - len(str(j))) * str(0) + str(j)][i] for j in range(1, 241)]  # 供应量
    for j in range(24):
        lsij=[lsi[k] for k in range(len(lsi)) if (k-j)%24==0]
        ls=sum(lsij)/len(lsij)
        matrix_loss[i][j] = ls
dfw_su=pd.DataFrame(matrix_supply,columns=['W' + (3 - len(str(j))) * str(0) + str(j) for j in range(1, 25)],index=df_order['供应商ID'])
dfw_sa=pd.DataFrame(matrix_satisfy,columns=['W' + (3 - len(str(j))) * str(0) + str(j) for j in range(1, 25)],index=df_order['供应商ID'])
dfw_ls=pd.DataFrame(matrix_loss,columns=['W' + (3 - len(str(j))) * str(0) + str(j) for j in range(1, 25)],index=df_ls['转运商ID'])
dfw_su.to_csv('.\\data\\matrix\\supplyForecast.csv')
dfw_sa.to_csv('.\\data\\matrix\\satisfyForecast.csv')
dfw_ls.to_csv('.\\data\\matrix\\lossForecast.csv')