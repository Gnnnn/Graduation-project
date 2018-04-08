import pymssql
import json
import config

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

# #用于将sql查出的不同格式的数据格式化为[[str],[str],[str],[str]],
# def checkdata(data): 
#     j = 0 
#     datas = []    
#     while j < len(data): 
#         if isinstance(data[j],unicode):
#             items = data[j].encode('unicode-escape')
#             datas.append(items) 
#             j += 1 
#         elif isinstance(data[j],(float,bool)) or data[j] is None: 
#             item = str(data[j]) 
#             datas.append(item) 
#             j += 1 
#         else: 
#             item = str(data[j]) 
#             datas.append(item) 
#             j += 1 
#     return datas


if __name__ == '__main__':
    #conn = pymssql.connect(server=config.DatabaseInfo['DatabaseUrl']) 
    conn = pymssql.connect(config.DatabaseInfo['DatabaseUrl'],config.DatabaseInfo['UserName'],config.DatabaseInfo['Password'],config.DatabaseInfo['Database'],charset="UTF-8") 
    sql = 'select * from GraduationPro.dbo.test'
    database(conn,sql)
    conn.close()