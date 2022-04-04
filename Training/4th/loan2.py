import pandas as pd

df_info=pd.read_excel(".\\data\\附件2：302家无信贷记录企业的相关数据.xls",sheet_name='企业信息')
df_rate=pd.read_csv(".\\data\\风险量化与贷款利率2.csv")
df_assess=pd.read_csv(".\\data\\风险量化与评级2.csv")
df_info3=pd.read_excel(".\\data\\附件3：银行贷款年利率与客户流失率关系的统计数据.xls")

p=dict()
ass_bre=dict()
ass_bre['A']=0
ass_bre['B']=0.00263
ass_bre['C']=0.05882
ass_bre['D']=1
assess=df_assess['风险评级']
r=dict()
l=dict()
for i in df_info.index:
    p[i]=ass_bre[assess[i]]
for i in df_rate.index:
    r[i]=df_rate['贷款利率'][i]
year=df_info3['贷款年利率']
A=df_info3['信誉评级A']
B=df_info3['信誉评级B']
C=df_info3['信誉评级C']
for i in df_rate.index:
    index = 0
    for j in range(len(year)):
        if year[j] == r[i]:
            index = j
    if assess[i]=='A':
        l[i]=A[index]
    if assess[i]=='B':
        l[i]=B[index]
    if assess[i]=='C':
        l[i]=C[index]
state=dict()
for i in df_rate.index:
    if assess[i]=='D':
        state[i]='no loan'
    else:
        state[i] = 0
join=[]
print(state)
for i in df_rate.index:
    if state[i]!='no loan':
        join.append(i)
alpha=dict()
for i in join:
    alpha[i]=r[i]*(1-l[i])-0.038-(1+r[i])*p[i]
print(alpha)
limit=dict()
for i in df_rate.index:
    limit[i]=100*(1-p[i])
out=sorted(alpha.items(), key = lambda kv:(kv[1], kv[0]),reverse=True)
acc_loan=0
for i in out:
    if state[i[0]]!='no loan' and acc_loan<10000:
        state[i[0]]=limit[i[0]]
        acc_loan+=limit[i[0]]

for i in range(302):
    print('E'+str(i+1),'\t',assess[i],'\t',state[i],'\t',r[i])
dfw=pd.DataFrame([['E'+str(i+1),assess[i],'是' if state[i]!='no loan' and state[i]!=0 else '否',state[i] if state[i]!='no loan' else '-',
                   r[i] if state[i]!='no loan' else '-'] for i in range(302)],columns=['企业代号','计算信用评级','是否贷款','贷款金额','贷款利率'])
dfw.to_csv('.\\data\\问题二求解结果.csv',index=False)