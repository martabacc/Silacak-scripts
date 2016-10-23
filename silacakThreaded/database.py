from pymssql import *
from env import *
from Init_Function import *
from main import workQueue


# SET NOCOUNT ON should be added to prevent errors thrown by cursor

sql = 'select pub_judul from '+ DB_TABLE_NAME

cursor.execute(sql)
print cursor.fetchone()

class DB():

    def __init__(self):
        self.conn = pymssql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,database=DB_DATABASE)

    def updateRow(self, index, classifiedValue):
        cursor = self.conn.cursor()
        updateQuery = "update "+ DB_TABLE_NAME + " set " + DB_ROW_NAME + " = " + classifiedValue + " where pub_id= " + str(bigArray[index][0])
        cursor.execute()

    def closeCon(self): self.conn.close()




