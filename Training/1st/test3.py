from matplotlib import pyplot as plt
from math import *
def DisCal(a,b):
    return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2+(a[2]-b[2])**2)
def confliDetec(tspan, road1, road2, rnode, id_cor):
    #tspan 轨迹二滞后轨迹一的时间
    state1=[]
    state2=[]
    if tspan<0:
        for i in range(abs(tspan)):
            state1.append([-1, -1])
    else:
        for i in range(abs(tspan)):
            state2.append([-1, -1])
    for i in range(len(road1)-1):
        time=int(DisCal(id_cor[rnode[road1[i]]],id_cor[rnode[road1[i+1]]]))
        for j in range(time):
            state1.append([road1[i],road1[i+1]])
    for i in range(len(road2)-1):
        time=int(DisCal(id_cor[rnode[road2[i]]],id_cor[rnode[road2[i+1]]]))
        for j in range(time):
            state2.append([road2[i],road2[i+1]])
    judge = False
    print(state1)
    print(state2)
    for i in range(min(len(state1),len(state2))):
        s1=state1[i]
        s2=state2[i]
        if s1[0]==s2[1] and s1[1]==s2[0]:
            p = 0
            k=state1[i]
            print(k)
            print(1212)
            for j in range(i,min(len(state1),len(state2))):
                if state1[j]==k:
                    print(state1[j])
                    p+=1
                else:
                    break
            judge=True
            break
    if judge==False:
        return judge
    else:
        return judge,p
f=open('node4.txt')
id_cor=dict()
cor_id=dict()
id_m=dict()
for line in f:
    ele=[]
    num=[]
    for letter in line:
        if letter!=' ':
            num.append(letter)
        if letter==' ' and num!=[]:
            ele.append(int(''.join(num)))
            num=[]
    if num!=[]:
        ele.append(int(''.join(num)))
    id_cor[ele[0]]=ele[1:4]
rnode=[100001, 100003, 1001, 1004, 1007, 1008, 1017, 1018, 1027, 1028, 1024, 1031, 1513, 1501, 101001, 2001, 2004, 2007, 2008, 2017, 2018, 2027, 2028, 2024, 2031, 2513, 100004, 2501, 101004, 3001, 3004, 3007, 3008, 3017, 3018, 3027, 3028, 3024, 3031, 3513, 100007, 3501, 101007, 100009, 100010, 4001, 4004, 4007, 4008, 4017, 4018, 4027, 4028, 4024, 4031, 4513, 4501, 101010, 101002, 101003, 101005, 101006, 101008, 101009, 1005, 1006, 1009, 1010, 1011, 1014, 1015, 1016, 1019, 1020, 1021, 1025, 1026, 1029, 1030, 2005, 2006, 2009, 2010, 2011, 2014, 2015, 2016, 2019, 2020, 2021, 2025, 2026, 2029, 2030, 3005, 3006, 3009, 3010, 3011, 3014, 3015, 3016, 3019, 3020, 3021, 3025, 3026, 3029, 3030, 4005, 4006, 4009, 4010, 4011, 4014, 4015, 4016, 4019, 4020, 4021, 4025, 4026, 4029, 4030, 1505, 1509, 2505, 2509, 3505, 3509, 4505, 4509, 100006]
#定义坐标轴
fig = plt.figure()
ax1 = plt.axes(projection='3d')
#ax = fig.add_subplot(111,projection='3d')  #这种方法也可以画多个子图
i=[0, 1, 26, 15, 16, 79, 80]
for j in range(len(i)-1):
    cor1=id_cor[rnode[i[j]]]
    cor2=id_cor[rnode[i[j+1]]]
    x1=[cor1[0],cor2[0]]
    y1=[cor1[1],cor2[1]]
    z1=[cor1[2],cor2[2]]
    ax1.plot3D(x1,y1,z1,'gray')    #绘制空间曲线
#plt.show()
print(confliDetec(-37,[40, 29, 30, 94, 95, 31, 32, 96, 97],[97,96,32,31,95,94,30,29,40],rnode,id_cor))

