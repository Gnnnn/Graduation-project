from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Droid Sans Fallback'] 
#设置中文字体
plt.rcParams['axes.unicode_minus']=False 
#正确显示负号
def file2matrix(filename):    
	fr = open(filename)    
	numberOfLines = len(fr.readlines())         
	#get the number of lines in the file    
	returnMat = zeros((numberOfLines,3))        
	#prepare matrix to return    
	classLabelVector = []                       
	#prepare labels return    
	fr = open(filename)    
	index = 0    
	for line in fr.readlines():        
		line = line.strip()        
		listFromLine = line.split('\t')        
		returnMat[index,:] = listFromLine[0:3]        
		classLabelVector.append(int(listFromLine[-1]))        
		index += 1    
		return returnMat,classLabelVector
	dating_x1 = []
	dating_y1 = []
	dating_x2 = []
	dating_y2 = []
	dating_x3 = []
	dating_y3 = []
	datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
	fig = plt.figure()
	ax = fig.add_subplot(111)
	i = 0
	for labels in datingLabels:    
		if labels == 1:        
			dating_x1.append(datingDataMat[i,0])        
			dating_y1.append(datingDataMat[i,1])        
			i = i+1    
		if labels == 2:        
			dating_x2.append(datingDataMat[i,0])        
			dating_y2.append(datingDataMat[i,1])        
			i = i+1    
		if labels == 3:        
			dating_x3.append(datingDataMat[i,0])        
			dating_y3.append(datingDataMat[i,1])        
			i = i+1
	ax.scatter(dating_x1,dating_y1,s=5,label='不喜欢')
	ax.scatter(dating_x2,dating_y2,s=10,label='魅力一般')
	ax.scatter(dating_x3,dating_y3,s=15,label='极具魅力')
	plt.legend(loc='best')
	plt.xlabel('每年获取的飞行常客里程数')
	plt.ylabel('玩视频游戏所耗时间百分比')
	plt.xlim(-100,100000)
	plt.ylim(-2,25)
	plt.show()

file2matrix(filename)