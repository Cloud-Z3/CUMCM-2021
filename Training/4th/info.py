import pandas as pd
df_info=pd.read_excel(".\\data\\附件1：123家有信贷记录企业的相关数据.xls",sheet_name='企业信息')
breach=dict()
credit=df_info['信誉评级']
bre=df_info['是否违约']
for i in df_info.index:
    if credit[i] not in breach.keys():
        if bre[i]=='是':
            breach[credit[i]]=[1,1]
        else:
            breach[credit[i]] = [0, 1]
    else:
        breach[credit[i]][1]+=1
        if bre[i]=='是':breach[credit[i]][0]+=1
for key in breach.keys():
    breach[key]=breach[key][0]/breach[key][1]
    print(key,breach[key])
