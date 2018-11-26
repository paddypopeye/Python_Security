#!/usr/bin/pyhton3
import sqlite3
import mysql
from mysql.connector import MySQLConnection, Error

class MySQLConnection:
	"""docstring for MySQLConnection"""
	def __init__(self,db=sqlite3.connect('test.db')):
		self.db = db
		db.row_factory = sqlite3.Row
		print("Connected to the test DB")

	def Retrieve(self):
		print("Retrieving values from the test database")

		read = self.db.execute('SELECT * FROM test1 ORDER BY i1')

		for row in read:
			print(row['t1'])


class MySQLiteConnection(object):
	"""docstring for MySQLiteConnection"""
	def __init__(self, kwargs = dict(host='localhost',\
		database='testdb',user='root',password='pass')):
		try:
			self.kwargs = kwargs
			conn = mysql.connector.connect(**kwargs)

			if conn.is_connected():
				print ("Connected to the DB successfully")

		except Error as e:
			print(e)

		finally:
			conn.close()

	def Retrieve(self):
		print("Fetching results from the database")
		try:
			conn = MySQLConnection(**self.kwargs)
			cursor = conn.cursor()
			cursor.execute('SELECT * FROM EMPLOYEE')
			rows = cursor.fetchall()
			print('Total Row(s):', cursor.rowcount)
			for row in rows:
				print("First Name: ", row[0])
				print("Last Name: ", row[1])
				print("Sex: ", row[2])
				print("Age: ", row[3])
				print("Salary: ", row[4])

		except Error as e:
			print(e)

		finally: 
			cursor.close()
			conn.close()


def main():
	ConnectToMySQL = MySQLConnection()
	ConnectToMySQL.Retrieve()
	ConnectToMySQLite3 = MySQLiteConnection()
	ConnectToMySQLite3.Retrieve()


if __name__ == '__main__':
	main()