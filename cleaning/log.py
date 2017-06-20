
import time
import StringIO
import csv
import time
import datetime
import logging

def initLogging():
	logging.basicConfig( filename='cleaning.log',level=logging.DEBUG)
	# logging.debug('This message should go to the log file')
	# logging.info('So should this')
	# logging.warning('And this, too')

def loginfo(string):
	logging.info(string)
	# print(string)

def logsuccess():
	loginfo("Status : SUCCESS at function " + string)
	# print("Status : SUCCESS")


def logwarn(string):
	logging.info(string)
	# print(string)

def logfailed(string):
	logging.warning("Status : Failed at function " + string)
	# print(string)

def logdebug(string):
	logging.debug(string)
	# print(string)

def logstarted():
	logging.info("Program started. Good luck have fun!")
	# print(string)

def logfinished():
	logging.info("Program finished. Thank you!")
	# print(string)