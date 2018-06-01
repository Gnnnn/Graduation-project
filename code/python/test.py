# -*- coding: utf-8 -*-  
import numpy as np  
import matplotlib.pyplot as plt  
#X轴，Y轴数据  
x = ["0000","1","2","3","4","5","6"]  
y = [0.3,0.4,2,5,3,4.5,4]  
y1 = [0.5,0.4,2,5,3,4.5,9] 
plt.figure(figsize=(8,4)) #创建绘图对象  
plt.plot(x,y,"b--",linewidth=1)   #在当前绘图对象绘图（X轴，Y轴，蓝色虚线，线宽度） 
plt.plot(x,y1,"x-",linewidth=1)
plt.xlabel("Time(s)") #X轴标签  
plt.ylabel("Volt")  #Y轴标签  
plt.title("Line plot") #图标题  
plt.show()  #显示图  