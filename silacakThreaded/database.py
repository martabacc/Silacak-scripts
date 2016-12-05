import _mssql
from env import *


# SET NOCOUNT ON should be added to prevent errors thrown by cursor

cursor = _mssql.connect(server=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)

def updateRow(index, classifiedValue):

    try :
        updateQuery = "UPDATE "+ DB_TABLE_NAME + " set " + DB_ROW_NAME + " = " + str(classifiedValue) + " where pub_id= " + str(index)
    except :
        print "Updating " + str(index) + " to value " + str(classifiedValue) + "failed"
    # print updateQuery
    cursor.execute_non_query(updateQuery)

def closeConn() :
    cursor.close()

def getAllRow():
    selectQ = "select pub_id, pub_keterangan from " + DB_TABLE_NAME
    result = []
    cursor.execute_query(selectQ)
    for row in cursor :
        result.append(row)

    return result

def getIssnRow():
    selectQ = "select * from " + DB_ISSN_TABLE
    result = []
    cursor.execute_query(selectQ)
    for row in cursor :
        result.append(row)

    return result
