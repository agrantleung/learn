import pymysql.cursors

try:
    conn=pymysql.connect(host='localhost',user='root',passwd='icanfly',db='sakila',charset='utf8')
    cur=conn.cursor()
    cur.execute('select * from actor where actor_id <10')
    data=cur.fetchall()
    for d in data:
        print("ID:"+str(d[0])+" FirstName:"+str(d[1])+"   LastName:"+str(d[2])+"  LastUpdate:"+str(d[3]))
    cur.close()
    conn.close()
except Exception: print("XXX Fail XXX")
'''
import pymysql.cursors
connection = pymysql.connect(host='localhost',
                             port=3306,
                             user='root',
                             password='icanfly',
                             db='sakila',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
config = dict(host='localhost', port=3306, user='root', password='icanfly', db='sakila', charset='utf8mb4',
              cursorclass=pymysql.cursors.DictCursor)
connection = pymysql.connect(**config)

try:
    #conn=pymysql.connect(host='localhost',user='root',passwd='icanfly',db='sakila',charset='utf8')
    cur=conn.cursor()
    cur.execute('select * from actor where actor_id <10')
    data=cur.fetchall()
    for d in data:
        print("ID:"+str(d[0])+" FirstName:"+str(d[1])+"   LastName:"+str(d[2])+"  LastUpdate:"+str(d[3]))
    cur.close()
    conn.close()
except Exception: print("XXX Fail XXX")
'''
