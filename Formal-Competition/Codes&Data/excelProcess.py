import pandas as pd
df_is=pd.read_excel('.\\data\\evaluate.xlsx')
matrix=[[df_is['ind'][i],df_is['stf'][i],i+1] for i in df_is.index]
print(matrix)
dfw=pd.DataFrame(matrix,columns=['供应商ID','综合评分','排名'])
dfw.to_csv('.\\data\\evaluate.csv',index=False)