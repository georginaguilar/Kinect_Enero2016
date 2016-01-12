#!/usr/bin/python
 # -*- coding: latin-1 -*-

import MySQLdb

#db = MySQLdb.connect(host=MY_HOST, user=MY_USER, passwd=MY_PASS, db=MY_DB)
db = MySQLdb.connect(host='localhost', user='root', passwd='1234', db='kf_json')

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM data_capturev4 WHERE Happy='Yes' AND Engage='Yes' AND  WearingGlasses='Yes'")

# print all the first cell of all the rows
for row in cur.fetchall():
    print row
    row=cur.fetchall()

    # Close all cursors
cur.close()
# Close all databases
db.close()