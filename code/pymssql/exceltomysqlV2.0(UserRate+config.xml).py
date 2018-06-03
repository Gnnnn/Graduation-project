# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import pymysql.cursors
import xml.dom.minidom

#这是第二版本，加了读取使用同名.xml配置文件自动获取字段并自动创建表的功能，可以处理行名+列名的excel

def xmlExcel(xmlname):
    #打开xml文档
    dom = xml.dom.minidom.parse(xmlname)

    #得到文档元素对象
    root = dom.documentElement
    sheetname = root.nodeName
    # print (root.nodeName)
    i = 1
    Attrdict = {}
    while i < len(root.childNodes):
        childNode = root.childNodes[i]
        # print (childNode.nodeName)
        # print (childNode.getAttribute('name'))
        Attrdict[childNode.nodeName] = childNode.getAttribute('name')
        i = i + 2
    print(Attrdict)
    return sheetname,Attrdict


def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径 by_name：Sheet名称,
# Attr:根据config.xml映射出的行列值字典
def excel_table_byname(file,sheetname,Attr):
    data = open_excel(file)
    table = data.sheet_by_name(sheetname)
    colnameindex=0
    colnames =  table.row_values(colnameindex) #第一行数据
    # print(colnames)
    columnName = Attr.get('column')
    rowName = Attr.get('row')
    dataName = Attr.get('data')
    nrows = table.nrows
    ncols = table.ncols
    # cell_value = table.cell_value(2,2)
    # print (cell_value)
    data = []
    for i in range(1,nrows):
        row_data = table.row_values(i)
        for j in range(1,ncols):
            dataDict = {}
            dataDict[columnName] = row_data[0]
            dataDict[rowName] = colnames[j]
            dataDict[dataName] = table.cell_value(i,j)
            # print (dataDict)
            data.append(dataDict)
    print(data)
    #[{InstantNoodleId:1001,UserId:1,UserRate:1},{}]
    return data

def createTableSql(tableName,data):
    for row in data:
        print(row)
        Attrlen = len(row);
        l = 0
        sqlModel = "CREATE TABLE `{}` ( "
        sqlAttrModel = "`{}` {} DEFAULT NULL"
        sqlModelEnd = " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        while l < Attrlen-1: 
            sqlModel = sqlModel + sqlAttrModel + ", "
            l = l+ 1
        sqlModel = sqlModel +sqlAttrModel + sqlModelEnd
        # print(sqlModel)
        rowType = {}
        sqlvalue = "'"+tableName+"';"
        for key in row:
            if isinstance(row[key],str):
                rowType[key] = 'varchar(30)'
            elif isinstance(row[key],(int,bool)):
                rowType[key] = 'int(100)'
            elif isinstance(row[key],float):
                rowType[key] = 'float(10,4)'
            sqlvalue = sqlvalue + key+";"+rowType[key]+";"
        sqlvalue=DelLastChar(sqlvalue)
        sqlvaluelist = sqlvalue.split(";")
        # print(sqlvaluelist)
        sql = sqlModel.format(*sqlvaluelist)
        print (sql)
        return sql

def insertSql(row):
    Attrlen = len(row);
    sql = "INSERT INTO `'"+ file +"'` values ("
    for key in row:
        value = row[key]
        sql = sql+"'"+str(value)+"',"
    sql = DelLastChar(sql)
    sql = sql +");"
    print(sql)
    return sql



#连接数据库-查询
def database(conn,sql):
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
        result = checkdata(result) 
        datas.append(result) 
    return datas 



#连接数据库-增删改
def databasesql(conn,sql):
    cursor = conn.cursor() 
    if not cursor: 
        raise Exception('数据库连接失败！') 
    cursor.execute(sql) 
    conn.commit() 
    cursor.close() 
    #conn.close() 
    return 

def DelLastChar(str):
    str_list=list(str)
    str_list.pop()
    return "".join(str_list)

def arraydictToMysql(tableName,data):
    for row in data:
        print(row)
        Attrlen = len(row);
        l = 0
        sqlModel = "CREATE TABLE `{}` ( "
        sqlAttrModel = "`{}` {} DEFAULT NULL"
        sqlModelEnd = " ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"
        while l < Attrlen-1: 
            sqlModel = sqlModel + sqlAttrModel + ", "
            l = l+ 1
        sqlModel = sqlModel +sqlAttrModel + sqlModelEnd
        print(sqlModel)

        rowType = {}
        sqlvalue = "'"+tableName+"';"
        for key in row:
            if isinstance(row[key],str):
                rowType[key] = 'varchar(30)'
            elif isinstance(row[key],(int,bool)):
                rowType[key] = 'int(100)'
            elif isinstance(row[key],float):
                rowType[key] = 'float(10,4)'
            sqlvalue = sqlvalue + key+";"+rowType[key]+";"
        sqlvalue=DelLastChar(sqlvalue)
        sqlvaluelist = sqlvalue.split(";")
        print(sqlvaluelist)
        sql = sqlModel.format(*sqlvaluelist)
        print (sql)
        return sql



def main(xmlfile,file):
    # conn = pymysql.connect(host='18.218.245.165',user='root',passwd='test',db='Gra') 
    # Connect to the database
    conn = pymysql.connect(host='18.218.125.105',
                             user='root',
                             password='test',
                             db='xiaoke',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    
    sheetname,Attr = xmlExcel(xmlname)
    data = excel_table_byname(file,sheetname,Attr)

    createsql = createTableSql(file,data)
    databasesql(conn,createsql)
    for row in data:
        insertsql = insertSql(row)
        databasesql(conn,insertsql)
    conn.close()
    print("finished!")

if __name__=="__main__":
    # file = sys.argv[1]
    # sheet = "Sheet1"
    file = '../testData/intensityTime.xlsx'
    xmlname = "../testData/intensityTime.xml"
    main(xmlname,file)

#xml格式如：
# <?xml version="1.0" encoding="utf-8"?>
# <Sheet1>
#     <row name='InstantNoodleId'>1001</row>
#     <column name='UserId'>1</column>
#     <data name='UserRate'>1</data>
# </Sheet1>