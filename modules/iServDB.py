import psycopg2

class iServDB:
    def __init__(self, dbname, user, pwd):
        self.dbname = dbname
        self.user = user
        self.pwd = pwd

    def query(self, query):
        conn= psycopg2.connect('host=iServDB.cloudopenlab.org.tw port=5432 dbname='+self.dbname+' user='+self.user+' password='+self.pwd)
        cur = conn.cursor()
        cur.execute(query)
        rows = cur.fetchall()
        return rows
