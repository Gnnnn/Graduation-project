import pymssql
import json

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
    print results
    while i < len(results): 
        i = i+1 
        result = results[i-1] 
        result = checkdata(result) 
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


if __name__ == '__main__':
	conn = pymssql.connect(server='localhost') 
	#sql = 'select * from school.dbo.studyroom'
    sql = ''
	database(conn,sql)
    conn.close()
