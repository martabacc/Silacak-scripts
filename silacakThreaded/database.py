import _mssql
from env import *


# SET NOCOUNT ON should be added to prevent errors thrown by cursor

cursor = _mssql.connect(server=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)

def updateRow(index, classifiedValue):

    updateQuery = "UPDATE "+ DB_TABLE_NAME + " set " + DB_ROW_NAME + " = " + str(classifiedValue) + " where pub_id= " + str(index)
    print updateQuery
    # cursor.execute_non_query(updateQuery)

def closeConn() : cursor.close()


