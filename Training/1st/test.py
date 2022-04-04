import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
lam = 0.5
T = 10
n = np.random.poisson(lam * T)
# 生成n个[0, T]均匀分布随机数并排序
t = np.hstack([[0], np.sort(np.random.random(n) * T)])
for i in t:
    print(i)
    print(round(i))
print(t)
for i in range(n):
    plt.plot((t[i], t[i+1]), (i, i), c='r')
plt.plot((t[i+1], T), (n, n), c='r')
plt.xlim([0, T])
plt.ylim([0, n])
sns.despine()
plt.show()