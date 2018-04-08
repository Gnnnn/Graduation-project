# -*- coding: utf8 -*-

import xlrd

def excel(fileName):
    bk = xlrd.open_workbook(fileName)
    shxrange = range(bk.nsheets)
    try:
        sh = bk.sheet_by_name("sheet1")
    except:
    	print("no sheet in file named Sheet1")

    nrows = sh.nrows
    ncols = sh.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    dataList = []
    for i in range(0,nrows):
    	dataList.append(sh.row_values(i))

    attrList = dataList[0]
    while '' in attrList:
    	attrList.remove('')

    oldNumList = dataList[1]
    while '' in oldNumList:
    	oldNumList.remove('')
    numList = list(set(oldNumList))
    numList.sort(key=oldNumList.index)

    print("attrList: ")
    print(attrList)
    print("numList: ")
    print(numList)
    print(dataList)
    return dataList,attrList,numList


#def database():
	


if __name__ == '__main__':
	fileName = '泡面品评version2.xls'
	excel(fileName)


# import pymssql
# import config

# print("start")
# print(config.DatabaseInfo['DatabaseUrl'])

# conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database'],charset="UTF-8") 
# print('ok')
# conn.close()