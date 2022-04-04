import matplotlib.pyplot as plt
import matplotlib
import pandas as pd
import json
import numpy as np
import seaborn as sns
from scipy.stats import spearmanr, pearsonr

#数据读取
df_xinfo=pd.read_excel(".\\data\\附件2：302家无信贷记录企业的相关数据.xls",sheet_name='销项发票信息')
df_jinfo=pd.read_excel(".\\data\\附件2：302家无信贷记录企业的相关数据.xls",sheet_name='进项发票信息')

'''
(1)   企业实力
年销售额
根据销项发票确定
(2)   盈利能力
年净利润
根据销项发票、进项发票共同确定
(3)   供销关系
供给侧和销售侧的稳定程度 熵
(4)   经营稳定性
票据有效率
(5)   发展潜力
年利润增长率'''

entro_id_x=df_xinfo['企业代号']
invoi_date_x=df_xinfo['开票日期']
custom_id_x=df_xinfo['购方单位代号']
money_x=df_xinfo['金额']
tax_x=df_xinfo['税额']
total_x=df_xinfo['价税合计']
invoice_state_x=df_jinfo['发票状态']

entro_id_j=df_jinfo['企业代号']
invoi_date_j=df_jinfo['开票日期']
custom_id_j=df_jinfo['销方单位代号']
money_j=df_jinfo['金额']
tax_j=df_jinfo['税额']
total_j=df_jinfo['价税合计']
invoice_state_j=df_jinfo['发票状态']

#1企业实力
print(1,'企业实力')
power=dict()

for i in df_xinfo.index:
    if (entro_id_x[i] not in power.keys())and(invoice_state_x[i]=='有效发票'):
        power[entro_id_x[i]]=total_x[i]
    else:
        if invoice_state_x[i]=='有效发票':
            power[entro_id_x[i]]+=total_x[i]

for key in power:
    print(key,power[key])

print('------')

#2盈利能力
print(2,'盈利能力')
earn=dict()
for key in power.keys():
    earn[key]=power[key]

for i in df_jinfo.index:
    if (entro_id_j[i] not in earn.keys())and(invoice_state_j[i]=='有效发票'):
        earn[entro_id_j[i]]=total_j[i]
    else:
        if invoice_state_j[i]=='有效发票':
            earn[entro_id_j[i]]-=total_j[i]

for key in earn:
    print(key,earn[key])

# 3供销关系
# 上下游稳定性
print(3,'供销关系')
sup_sell=dict()
for i in df_jinfo.index:
    if entro_id_j[i] not in sup_sell.keys():    # 初始化
        if str(invoi_date_j[i]).split('-')[0]=='2018'and invoice_state_j[i]=='有效发票':  # valid ?
            sup_sell[entro_id_j[i]]=[[[custom_id_j[i]],[]],  [[],[]]]
        elif str(invoi_date_j[i]).split('-')[0] == '2019'and invoice_state_j[i]=='有效发票':
            sup_sell[entro_id_j[i]] = [[[], [custom_id_j[i]]],  [[], []]]   # error
    else:
        if str(invoi_date_j[i]).split('-')[0]=='2018'and invoice_state_j[i]=='有效发票':
            sup_sell[entro_id_j[i]][0][0].append(custom_id_j[i])
        elif str(invoi_date_j[i]).split('-')[0] == '2019'and invoice_state_j[i]=='有效发票':
            sup_sell[entro_id_j[i]][0][1].append(custom_id_j[i])
for key in sup_sell:
    a=sup_sell[key][0][0]
    b=sup_sell[key][0][1]
    jsim=len(set(a)&set(b))/len(set(a)|set(b))
    sup_sell[key][0]=jsim
for i in df_xinfo.index:
    if entro_id_x[i] not in sup_sell.keys():
        if str(invoi_date_x[i]).split('-')[0]=='2018'and invoice_state_x[i]=='有效发票':
            sup_sell[entro_id_x[i]]=[[[],[]],[[custom_id_x[i]],[]]]
        elif str(invoi_date_x[i]).split('-')[0] == '2019'and invoice_state_x[i]=='有效发票':
            sup_sell[entro_id_x[i]] = [[], [[]], [[], [custom_id_x[i]]]]
    else:
        if str(invoi_date_x[i]).split('-')[0]=='2018'and invoice_state_x[i]=='有效发票':
            sup_sell[entro_id_x[i]][1][0].append(custom_id_x[i])
        elif str(invoi_date_x[i]).split('-')[0] == '2019'and invoice_state_x[i]=='有效发票':
            sup_sell[entro_id_x[i]][1][1].append(custom_id_x[i])
for key in sup_sell:
    a=sup_sell[key][1][0]
    b=sup_sell[key][1][1]
    xsim=len(set(a)&set(b))/len(set(a)|set(b))
    sup_sell[key][1] = xsim
for key in sup_sell:
    sup_sell[key]=0.7*sup_sell[key][0]+0.3*sup_sell[key][1]
    print(key,sup_sell[key])

#4经营稳定性
print(4,'经营稳定性')
stability=dict()
for i in df_xinfo.index:
    if entro_id_x[i] not in stability.keys():
        if invoice_state_x[i] == '有效发票':
            stability[entro_id_x[i]] = [1, 1]
        else:
            stability[entro_id_x[i]] = [0, 1]
    else:
        if invoice_state_x[i]=='有效发票':
            stability[entro_id_x[i]][0] += 1
            stability[entro_id_x[i]][1] += 1
        else:
            stability[entro_id_x[i]][1] += 1

for key in stability:
    stability[key]=stability[key][0]/stability[key][1]
    print(key,stability[key])

#5发展潜力
print(5,'发展潜力')
potential=dict()
for i in df_xinfo.index:
    if entro_id_x[i] not in potential.keys():
        if str(invoi_date_x[i]).split('-')[0]=='2018' and invoice_state_x[i]=='有效发票':
            potential[entro_id_x[i]]=[total_x[i],0]
        elif str(invoi_date_x[i]).split('-')[0] == '2019' and invoice_state_x[i]=='有效发票':
            potential[entro_id_x[i]] = [0,total_x[i]]
    else:
        if str(invoi_date_x[i]).split('-')[0]=='2018' and invoice_state_x[i]=='有效发票':
            potential[entro_id_x[i]][0]+=total_x[i]
        elif str(invoi_date_x[i]).split('-')[0] == '2019' and invoice_state_x[i]=='有效发票':
            potential[entro_id_x[i]][1]+=total_x[i]
for key in potential:
    a=potential[key][0]
    b=potential[key][1]
    potential[key]=(b-a)/a
    print(key,potential[key])

for i in [power,earn,sup_sell,stability,potential]:
    print(i)

key=list(power.keys())
dwf=pd.DataFrame([[i[k] for i in [power,earn,sup_sell,stability,potential]] for k in key],index=key,columns=['企业实力','盈利能力','供销关系','经营稳定性','发展潜力'])
dwf.to_csv('.\\data\\afterPreProcesss2.csv')