# import mysql.connector

# dataBase = mysql.connector.connect(
#     host = 'localhost',
#     user = 'root',
#     passwd = 'Kryouliaris20'
# )


# #prepare a cursor object
# cursorObject = dataBase.cursor()

# #create the database
# cursorObject.execute("CREATE DATABASE firstcrm")

# print("All Done!")

import pymysql

# connect to MySQL
dataBase = pymysql.connect(
    host="localhost",
    user="root",
    password="Kryouliaris20"
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create the database
cursorObject.execute("CREATE DATABASE firstcrm")

print("All Done!")
