import os,re,commands

def mysqltest():
	for threadNum in [1,10]:
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

	mysqlSysbenches = []
	for threadNum in [1,10]:
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
		mysqlSys["errors"] = int(searchObj[0])
		mysqlSysbenches.append(mysqlSys)
		print ("ignored errors : ", mysqlSysbenches)


def pgsqltest():
	for threadNum in [1,10]:
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

	mysqlSysbenches = []
	for threadNum in [1,10]:
		mysqlSys = {}
		fileName = 'pgsqlSysbench%s.txt'%threadNum
		file_object = open(fileName)
		string1 = file_object.readlines( )
		searchObj = re.findall(r'\d+\.?\d*', string1[13])
		mysqlSys["read"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[14])
		mysqlSys["write"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[16])
		mysqlSys["total"] = int(searchObj[0])
		searchObj = re.findall(r'\d+\.?\d*', string1[19])
		mysqlSys["errors"] = int(searchObj[0])
		mysqlSysbenches.append(mysqlSys)
		print ("ignored errors : ", mysqlSysbenches)
# while threadNum <= 20:
# 	osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-host=18.218.125.105 --pgsql-port=5432 --pgsql-user=test  --pgsql-password=test --pgsql-db=XIAOKE --oltp-table-size=10000 prepare"%threadNum
# 	os.system(osshell)
# 	osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-host=18.218.125.105 --pgsql-port=5432 --pgsql-user=test  --pgsql-password=test --pgsql-db=XIAOKE --oltp-table-size=10000 run"%threadNum
# 	pgsqlre.append(os.system(osshell))
# 	osshell = "sysbench --threads=%s --events=10000  /root/sysbench-1.0/tests/include/oltp_legacy/oltp.lua --db-driver=pgsql --pgsql-host=18.218.125.105 --pgsql-port=5432 --pgsql-user=test  --pgsql-password=test --pgsql-db=XIAOKE --oltp-table-size=10000 cleanup"%threadNum
# 	os.system(osshell)
# 	threadNum = threadNum +5
# print (pgsqlre)

