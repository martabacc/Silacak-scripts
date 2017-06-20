
# connecting to database
import _mssql
from env import *
from log import *


# SET NOCOUNT ON should be added to prevent errors thrown by cursor
 
cursor = _mssql.connect(server=DB_HOST, user=DB_USER, password=DB_PASSWORD, database=DB_DATABASE)

initData = []

def deleteQ(arrayOfIds):

	deleteQ = "Delete from publikasi_dosen where pub_id in ("
	# passing ids of data rows to ask

	lenArr = len(arrayOfIds)-1
	if lenArr > 0 :
		for index,row in enumerate(arrayOfIds) :
			pub_id = row[0]
			
			deleteQ = deleteQ + " " + str(pub_id)
			if lenArr-index :
				deleteQ = deleteQ + ", "

		deleteQ = deleteQ + ' )'
		# logging

		loginfo("Query to Execute : "+ deleteQ)
		loginfo("Row counts : "+ len(arrayOfIds))

		# finish appending to deleteQ
		# now execute
		try :
			cursor.execute_non_query(deleteQ)
			time.sleep(2)
			logsuccess("deleteQ")
		except :
			logfailed("deleteQ")
		# print updateQuery


def closeConn() :
	cursor.close()
	logfinished()

def fetchInitData():
	loginfo("Fetching data started")
	fetchQ = "select pub_judul, pub_detilkodepub, count(*) as jumlah,  pub_keterangan, pub_tahun, pub_url_scholar from " + DB_TABLE_NAME + " group by pub_judul, pub_detilkodepub, pub_keterangan, pub_tahun, pub_url_scholar order by jumlah desc "
	cursor.execute_query(fetchQ)
	
	for row in cursor : 
		initData.append(row)
	loginfo("Success fetching data from database")
	loginfo("Total data : " + str(len(initData)))
	loginfo("Initiating data finished")

def fetchSpecificRows(data):
	# consists of an aray
	# with this indexes
	# pub_judul, pub_detilkodepub, pub_keterangan, pub_tahun, pub_url_scholar

	# print(data)
	loginfo("Fetching specific row for " + data['pub_judul'] + " started")
	fetchQ = " Select pub_id, count(*) as jumlah_anggota "+ " from " + DB_TABLE_NAME + " left join " + DB_ANGGOTA_TABLE + ' on ' + DB_TABLE_NAME + '.' + DB_PUB_PK + ' = ' + DB_ANGGOTA_TABLE + '.'  + DB_FK_ANGGOTA_PUB + " where pub_judul = '" + data[0] + "'"

	# if data[3]:
	# 	fetchQ = fetchQ +" and pub_keterangan = '" + data[3] + "'"
	# if data["pub_tahun"]:
	# 	fetchQ = fetchQ +" and pub_tahun = " + str(data["pub_tahun"])
	# if data[5]:
	# 	fetchQ = fetchQ +" and pub_url_scholar = '" + data[5]+ "'"
	
	fetchQ = fetchQ +" group by pub_id order by jumlah_anggota desc"

	loginfo(fetchQ)

	try :
		cursor.execute_query(fetchQ)
		result = []
		for row in cursor :
			result.append(row)

		logsuccess(" fetchSpecificRows" )
		return result
	except : 
		logfailed(" fetchSpecificRows" )


def processEachRow(data):
	# passed an element fetchInitData()
	anggotaToPub = fetchSpecificRows(data)
	loginfo("Processing publikasi dengan judul " + data["pub_judul"])

	# deleting the firstOne
	if anggotaToPub:
		loginfo("Found duplicate rows : " + len(anggotaToPub) -1 + "rows")	
		
		del(anggotaToPub[0])
		loginfo("Proceeds to delete")	
		deleteQ(anggotaToPub)
		# 


if __name__ == "__main__":
	logstarted()

	fetchInitData()
	for duplicatedRows in initData:
		processEachRow(duplicatedRows)

	closeConn()

