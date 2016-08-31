import pymysql
try:
    conn=pymysql.connect(host='localhost',user='root',passwd='icanfly',db='sakila')
    cur=conn.cursor()
    cur.execute('select * from actor where actor_id <20')
    data=cur.fetchall()
    for d in data:
        print("ID:"+str(d[0])+"FirstName:"+str(d[1])+"LastName:"+str(d[2])+"LastUpdate:"+str(d[3]))
    cur.close()
    conn.close()
except Exception: print("XXX Fail XXX")