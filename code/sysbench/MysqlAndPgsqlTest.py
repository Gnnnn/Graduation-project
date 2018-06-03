# -*- coding: utf-8 -*-  
import os,re
#,commands
import numpy as np  
import matplotlib.pyplot as plt 


def mysqltestWrite(msyqltestThreadNumList):
	for threadNum in msyqltestThreadNumList:
		osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --mysql-table-engine=innodb --mysql-host=18.218.125.105 --mysql-db=xiaoke --oltp-table-size=10000 --mysql-user=root --mysql-password=test prepare"%threadNum
		os.system(osshell)
		osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --mysql-table-engine=innodb --mysql-host=18.218.125.105 --mysql-db=xiaoke --oltp-table-size=10000 --mysql-user=root --mysql-password=test run"%threadNum
		string1 = os.system(osshell)
		string1 = commands.getstatusoutput(osshell)
		osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --mysql-table-engine=innodb --mysql-host=18.218.125.105 --mysql-db=xiaoke --oltp-table-size=10000 --mysql-user=root --mysql-password=test run"%threadNum
		os.system(osshell)
		fileName = 'mysqlSysbench%s.txt'%threadNum
		file_object = open(fileName, 'w')
		string1 = string1[1]
		file_object.write(string1)
		file_object.close( )
		return 

def mysqltestRead(msyqltestThreadNumList):
	mysqlSysbenches = []
	for threadNum in msyqltestThreadNumList:
		mysqlSys = {}
		fileName = 'mysqlSysbench%s.txt'%threadNum
		file_object = open(fileName)
		string1 = file_object.readlines( )
		searchObj = re.findall(r'\d+\.?\d*', string1[13])
		mysqlSys["read"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[14])
		mysqlSys["write"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[16])
		mysqlSys["total"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[19])
		mysqlSys["sqlerrors"] = int(searchObj[0])
		mysqlSysbenches.append(mysqlSys)
		print ("testData : ", mysqlSysbenches)
	return mysqlSysbenches


def pgsqltestWrite(pgsqltestThreadNumList):
	for threadNum in pgsqltestThreadNumList:
		osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-host=18.218.125.105 --pgsql-port=5432 --pgsql-user=test  --pgsql-password=test --pgsql-db=XIAOKE --oltp-table-size=10000 prepare"%threadNum
		os.system(osshell)
		osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-host=18.218.125.105 --pgsql-port=5432 --pgsql-user=test  --pgsql-password=test --pgsql-db=XIAOKE --oltp-table-size=10000 run"%threadNum
		string1 = os.system(osshell)
		string1 = commands.getstatusoutput(osshell)
		osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-host=18.218.125.105 --pgsql-port=5432 --pgsql-user=test  --pgsql-password=test --pgsql-db=XIAOKE --oltp-table-size=10000 cleanup"%threadNum
		os.system(osshell)
		fileName = 'pgsqlSysbench%s.txt'%threadNum
		file_object = open(fileName, 'w')
		string1 = string1[1]
		file_object.write(string1)
		file_object.close( )
		return 


def pgsqltestRead(pgsqltestThreadNumList):
	pgsqlSysbenches = []
	for threadNum in pgsqltestThreadNumList:
		pgsqlSys = {}
		fileName = 'pgsqlSysbench%s.txt'%threadNum
		file_object = open(fileName)
		string1 = file_object.readlines( )
		searchObj = re.findall(r'\d+\.?\d*', string1[13])
		pgsqlSys["read"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[14])
		pgsqlSys["write"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[16])
		pgsqlSys["total"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[19])
		pgsqlSys["sqlerrors"] = int(searchObj[0])
		pgsqlSysbenches.append(pgsqlSys)
		print ("testData : ", pgsqlSysbenches)
	return pgsqlSysbenches

def pic(syslist,titleName):
	valueList = []
	for eachList in syslist:
	    keys = []
	    values = []
	    for key in eachList:
	        keys.append(key)
	        values.append(eachList[key])
	    valueList.append(values)
	print (keys)

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


def main():
	msyqltestThreadNumList = [1,5]
	#mysqlSysbenches = mysqltestWrite(msyqltestThreadNumList)
	mysqlSysbenches = mysqltestRead(msyqltestThreadNumList)
	pgsqltestThreadNumList = [1,5]
	#pgsqlSysbenches = pgsqltestWrite(pgsqltestThreadNumList)
	pgsqlSysbenches = pgsqltestRead(pgsqltestThreadNumList)
	titleName = "mysql"
	pic(mysqlSysbenches,titleName)
	titleName = "pgsql"
	pic(pgsqlSysbenches,titleName)
	titleName = "mysql&pgsql"
	mypg = []
	mypg.append(mysqlSysbenches[0])
	mypg.append(pgsqlSysbenches[0])
	print(mypg)
	pic(mypg,titleName)

if __name__ == '__main__':
	main()