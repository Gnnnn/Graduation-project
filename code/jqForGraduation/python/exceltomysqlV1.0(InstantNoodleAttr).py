# -*- coding: utf-8 -*- 
import  xdrlib ,sys
import xlrd
import pymysql.cursors

#这是最初的版本，没有config配置文件识别，字段是代码写的，针对的也是最简单的二维表格式的方便面属性。

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
    for row in tables:
        INid = str(row['id']).encode('utf-8')
        sampleId = str(row['sampleId'])
        name = row['name']
        manufacturer = row['manufacturer']
        specification = row['specification']
        if_widen = row['if_widen']
        if if_widen == "":
            if_widen = ''
        else:
            if_widen = row['if_widen']
        sql = "INSERT INTO InstantNoodles set id = '"+INid.decode('utf-8')+"',sampleId = '"+sampleId+"',name = '"+name+"',manufacturer='"+manufacturer+"',specification='"+specification+"',if_widen='"+if_widen+"';"
        databasesql(conn,sql)
    conn.close()

if __name__=="__main__":
    # file = sys.argv[1]
    # sheet = sys.argv[2]
    file = 'testData.xlsx'
    sheet = "方便面属性"
    main(file,sheet)

