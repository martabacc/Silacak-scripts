import pymssql
from env import *


cnxn = pymssql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,database=DB_DATABASE)
cursor = cnxn.cursor()

# SET NOCOUNT ON should be added to prevent errors thrown by cursor

sql = 'select pub_judul from '+ DB_TABLE_NAME

cursor.execute(sql)
print cursor.fetchone()
