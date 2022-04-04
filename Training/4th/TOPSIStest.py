from TOPSIS import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
'''
x=[]
y=[]
for a in range(50):
    x.append(a*0.2)
    y.append(topsis([a*0.2,0.5,0.5,0.5,0.5]))
    print(x[-1],y[-1])
data=pd.DataFrame({'x':x,'y':y})
sns.pointplot(x='x',y='y',data=data)
plt.show()'''
'''from TOPSIS import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

x=[]
y=[]
for a in range(50):
    x.append(a*0.2)
    y.append(topsis([a*0.2,0.5,0.5,0.5,0.5]))
    print(x[-1],y[-1])
sns.pointplot(x,y)
plt.show()'''
def place(a,b,k):
    ans=[]
    for i in range(k-1):
        ans.append(b)
    ans.append(a)
    for i in range(k,5):
        ans.append(b)
    return ans
from TOPSIS import *
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
for k in range(1,6):
    x=[]
    y=[]
    for a in range(0,51):
        x.append(a/50)
        b=(1-x[-1])/4
        y.append(topsis(place(a/50,b,k)))
        print(x[-1],y[-1])
    data=pd.DataFrame({'x':x,'y':y})
    plt.plot(x,y)
    plt.show()
'''
x1=[]
x2=[]
y1=[]#正确率
y2=[]#Spearman指数，越大越好
for a in range(0,101):
    x1.append(a/100)
    x2.append(1-x1[-1])
    y1.append(topsis([x1[-1],x2[-1],0,0,0])[0])
    y2.append(topsis([x1[-1],x2[-1],0,0,0])[1][0])
    print(x1[-1],x2[-1],y1[-1],y2[-1])
#data=pd.DataFrame({'x':x,'y':y})
plt.plot(x1,y2)
plt.show()
plt.plot(x1,y1)
plt.show()
