# -*- coding: utf-8 -*-  
import numpy as np  
import matplotlib.pyplot as plt  


lists = [{'read': 12152, 'write': 3472, 'total': 17360, 'errors': 0}, {'read': 35168, 'write': 9920, 'total': 50065, 'errors': 47}]
valueList = []
for eachList in lists:
    keys = []
    values = []
    for key in eachList:
        keys.append(key)
        values.append(eachList[key])
    valueList.append(values)
print (keys)

titleName = "sysbench" 
plt.figure(figsize=(8,4)) #创建绘图对象  
plt.xticks(range(len(keys)),keys)
print(len(valueList))
i = 0
while i < len(valueList):
    plt.plot(valueList[i],"x--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度） 
    i = i +1
plt.xlabel("Attr") #X轴标签  
plt.ylabel("Time(s)")  #Y轴标签 
plt.title(titleName) #图标题  
plt.show()  #显示图 
picPath = "%s.jpg"%titleName
plt.savefig(picPath)  #显示图 
