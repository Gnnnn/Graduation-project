import time
import datetime
from py2neo import Graph,Node,Relationship
# import cmdb.py2neo_function as neofunction

# g=neo4j.GraphDatabaseService('http://18.218.125.105:7474/db/data')
g = Graph(host = "18.218.125.105",http_port = 7474,user = "neo4j",password = "test")
# data initialize
#storage
def create_ci(total_ci):
    print ('%dX6CIs' % total_ci)
       
    print (time.ctime())
    for i in range(total_ci):
        storage_name='storage_%d' % i
        small_server_name='aix_%d' % i
        lpar_name='lpar_%d' % i
        db_name='db_%d' % i
        was_name='was_%d' % i
        app_name='app_%d' % i
        g.create(Node(ci_class='storage',city='Shanghai',district='PuDong',name=storage_name,rack=1,capacity=300),
                 Node(ci_class='small_server',city='Shanghai',district='PuDong',name=small_server_name,cpu_count=16,mem_GB=64),
                 Node(ci_class='lpar',city='Shanghai',district='PuDong',name=lpar_name,cpu_count=1,mem_GB=2),
                 Node(ci_class='db_instance',name=db_name,type='db2',version='9.1'),
                 Node(ci_class='was_Node',name=was_name,version='6.1'),
                 Node(ci_class='application',name=app_name)
                 )
           
    print (time.ctime())


create_ci(20)

def create_relationship(total_ci):
    #get the Nodes
    #get all storeage Nodes
    print ('get all storage Nodes, count number about %d' % total_ci)
    print (datetime.datetime.now())
    storage_list=neofunction.SearchNodes(g,'ci_class','storage')
    print (datetime.datetime.now())
       
    #get all small_server Nodes
    small_server_list=neofunction.SearchNodes(g,'ci_class','small_server')
       
    g.create((small_server_list[0],'depend_on',storage_list[0]))
       
    #get all lpar Nodes
    lpar_list=neofunction.SearchNodes(g,'ci_class','small_server')
       
    #get all was Nodes
    was_list=neofunction.SearchNodes(g,'ci_class','was_Node')
       
    #get all db_instance Nodes
    dbi_list=neofunction.SearchNodes(g,'ci_class','db_instance')
       
    #get all app Nodes
    app_list=neofunction.SearchNodes(g,'ci_class','application')
       
    print (time.ctime())
    for i in range(total_ci):
        g.create((lpar_list[i],'depend_on',small_server_list[i]))
        g.create((dbi_list[i],'running_on',lpar_list[i]))
        g.create((was_list[i],'running_on',lpar_list[i]))
        g.create((app_list[i],'depend_on',dbi_list[i]))
        g.create((app_list[i],'depend_on',was_list[i]))
       
    print (time.ctime())