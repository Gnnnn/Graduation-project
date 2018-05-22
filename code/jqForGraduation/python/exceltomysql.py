# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import pymysql.cursors
import types,time
def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))


#根据名称获取Excel表格中的数据   参数:file：Excel文件路径 by_name：Sheet名称
def excel_table_byname(file,by_name):
    colnameindex=0
    data = open_excel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows #行数 
    colnames =  table.row_values(colnameindex) #某一行数据 
    list =[]
    for rownum in range(1,nrows):
         row = table.row_values(rownum)
         if row:
             app = {}
             for i in range(len(colnames)):
                app[colnames[i]] = row[i]
             list.append(app)
    return list

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



def main(file,sheet):
    # conn = pymysql.connect(host='18.218.245.165',user='root',passwd='test',db='Gra') 
    # Connect to the database
    conn = pymysql.connect(host='18.218.245.165',
                             user='root',
                             password='test',
                             db='Gra',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
    tables = excel_table_byname(file,sheet)
    #create table
    sql = arraydictToMysql(file,tables)
    databasesql(conn,sql)
    for row in tables:
        Attrlen = len(row);
        sql = "INSERT INTO `'"+ file +"'` values ("
        for key in row:
            value = row[key]
            sql = sql+"'"+str(value)+"',"
        sql = DelLastChar(sql)
        sql = sql +");"
        print(sql)
        databasesql(conn,sql)
    conn.close()
    print("finished!")

if __name__=="__main__":
    # file = sys.argv[1]
    # sheet = "Sheet1"
    file = 'InstantNoodlesAttr.xlsx'
    sheet = "Sheet1"
    main(file,sheet)
