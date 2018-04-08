# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import pymssql
import json
import config

# def open_excel(file):
#     try:
#         data = xlrd.open_workbook(file)
#         return data
#     except Exception as e:
#         print(str(e))


# def excel_table_byindex(file,colnameindex,by_index):
#     data = open_excel(file)
#     table = data.sheets()[by_index]
#     nrows = table.nrows #行数
#     ncols = table.ncols #列数
#     colnames =  table.row_values(colnameindex) #某一行数据 
#     list =[]
#     for rownum in range(1,nrows):
#          row = table.row_values(rownum)
#          if row:
#              app = {}
#              for i in range(len(colnames)):
#                 app[colnames[i]] = row[i] 
#              list.append(app)
#     return list

# #根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
# def excel_table_byname(file,colnameindex,by_name):
#     data = open_excel(file)
#     table = data.sheet_by_name(by_name)
#     nrows = table.nrows #行数 
#     colnames =  table.row_values(colnameindex) #某一行数据 
#     list =[]
#     for rownum in range(1,nrows):
#          row = table.row_values(rownum)
#          if row:
#              app = {}
#              for i in range(len(colnames)):
#                 app[colnames[i]] = row[i]
#              list.append(app)
#     return list

#连接数据库-查询
def database(conn,sql):
    #conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database']) ,
    #conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database'],charset="UTF-8") 
    cursor = conn.cursor() 
    if not cursor: 
        raise Exception('数据库连接失败！') 
    cursor.execute(sql) 
    results = cursor.fetchall() 
    cursor.close() 
    #conn.close() 
    i = 0 
    datas = [] 
    print(results)
    while i < len(results): 
        i = i+1 
        result = results[i-1] 
        #result = checkdata(result) 
        datas.append(result) 
    return datas 



#连接数据库-增删改
def databasesql(conn,sql):
    #conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database']) ,
    #conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database'],charset="UTF-8") 
    cursor = conn.cursor() 
    if not cursor: 
        raise Exception('数据库连接失败！') 
    cursor.execute(sql) 
    conn.commit() 
    cursor.close() 
    #conn.close() 
    return

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



def main():
    excel(file)
    
    conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database'],charset="UTF-8")  
    sql = 'select * from GraduationPro.dbo.test'
    database(conn,sql)
    conn.close()

    file = '泡面品评version2.xls'
    # colnameindex = 0
    # by_name = u'sheet1'
    # by_index = 0
    # tables = excel_table_byindex(file,colnameindex,by_index)
    # for row in tables:
    #     print(row)

    # tables = excel_table_byname(file,colnameindex,by_name)
    # for row in tables:
    #     print(row)

    

if __name__=="__main__":
    main()