#! /usr/bin/python3
from dataGen import *
import mysql.connector
import os
from mysql.connector import Error
def mainMigration(ip, dbName, tableName, user, passwd, migrationData):
    print("Wa are in mainMigration")


def mainMigration(ip, dbName, tableName, user, passwd, peopleList, peopleOutList):
    try:
        mydb = mysql.connector.connect(
        host=ip,
        user=user,
        passwd=passwd,
        database=dbName
            host=ip,
            user=user,
            passwd=passwd,
            database=dbName
        )
        mycursor = mydb.cursor()
        print("connection to db")
        if mydb.is_connected():
            print ("Ok")
            print(ip, dbName, tableName, user, passwd)
            sql = "INSERT INTO people (ID, NAME, LASTNAME, FATHERNAME, EMAIL, AGE, PHONE, SALARY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            for i in migrationData:
                i = '{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(i["ID"], i["NAME"], i["LASTNAME"], i["FATERNAME"], i["EMAIL"], i["AGE"], i["PHONE"], i["SALARY"])
                listOfPeople = i.split(",")
                val = [listOfPeople]
                print (val)
                mycursor.executemany(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
        table = "CREATE TABLE IF NOT EXISTS {} (ID INT, LASTNAME VARCHAR(15), NAME VARCHAR(15), FATHERNAME VARCHAR(20), EMAIL VARCHAR(20), AGE INT, PHONE VARCHAR(15), SALARY INT)".format(
            tableName)
        mycursor.execute(table)
        sql = "INSERT INTO {} (ID, LASTNAME, NAME, FATHERNAME, EMAIL, AGE, PHONE, SALARY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(
            tableName)
        migrationData = mainGen(peopleList, peopleOutList)
        for i in migrationData:
            list1 = [i]
            list = list1[0]
            val = [(list.get('ID'), list.get('LASTNAME'), list.get('NAME'), list.get(
                'FATHERNAME'), list.get('EMAIL'), list.get('AGE'), list.get('PHONE'), list.get('SALARY'))]
            mycursor.executemany(sql, val)
        mydb.commit()
        print(mycursor.rowcount, "record inserted.")
    except Error as e:
        print("Error while connecting to MySQL", e)

def mainCreate(dataBaseName, tableName, user, passwd, ip):

def writeDB(ip, dbName, tableName, user, passwd, id, lastname, name, fathername, email, age, phone, salary):
    mydb = mysql.connector.connect(
        host=ip,
        user=user,
        passwd=passwd,
        database=dbName
    )
    mycursor = mydb.cursor()
    table = "CREATE TABLE IF NOT EXISTS {} (ID INT, LASTNAME VARCHAR(15), NAME VARCHAR(15), FATHERNAME VARCHAR(20), EMAIL VARCHAR(20), AGE INT, PHONE VARCHAR(15), SALARY INT)".format(
        tableName)
    mycursor.execute(table)
    sql = "INSERT INTO {} (ID, LASTNAME, NAME, FATHERNAME, EMAIL, AGE, PHONE, SALARY) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)".format(
        tableName)
    val = [(id, lastname, name, fathername, email, age, phone, salary)]
    mycursor.executemany(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def create(ip, dbName, tableName, user, passwd):
    midle = '{print "SET foreign_key_checks = 0; ALTER TABLE", $1, "CONVERT TO CHARACTER SET utf8 COLLATE utf8_general_ci; SET foreign_key_checks = 1; "}'
    code = "mysql --database={0} -B -N -e \"SHOW TABLES\" | awk '{1}' | mysql --database={0}".format(
        dbName, midle)
    createUser = 'mysql -u root -p=1 -e "DROP USER \'{0}\'@\'{1}\';flush privileges; CREATE USER \'{0}\'@\'{1}\' IDENTIFIED BY \'{2}\'; grant all privileges on *.* to \'{0}\'@\'{1}\';"'.format(
        user, ip, passwd)
    os.system(createUser)
    mydb = mysql.connector.connect(
    host=ip,
    user=user,
    passwd=passwd
        host=ip,
        user=user,
        passwd=passwd
    )
    mycursor = mydb.cursor()
    newDB = "CREATE DATABASE IF NOT EXISTS {}".format(dbName)
    mycursor.execute(newDB)
    os.system(code)
    useDB = "USE {}".format(dbName)
    mycursor.execute(useDB)
    newTable = "CREATE TABLE IF NOT EXISTS {} (ID INT, LASTNAME VARCHAR(15), NAME VARCHAR(15), FATHERNAME VARCHAR(20), EMAIL VARCHAR(20), AGE INT, PHONE VARCHAR(15), SALARY INT)".format(
        tableName)
    mycursor.execute(newTable)
    os.system(code)


def dropTable(ip, dbName, tableName, user, passwd):
    mydb = mysql.connector.connect(
        host=ip,
        user=user,
        passwd=passwd,
        database=dbName
    )
    mycursor = mydb.cursor()
    drop = "DROP TABLE {}".format(tableName)
    mycursor.execute(drop)


def dropDB(ip, dbName, user, passwd):
    mydb = mysql.connector.connect(
        host=ip,
        user=user,
        passwd=passwd,
    )
    mycursor = mydb.cursor()
    a = ("CREATE DATABASE IF NOT EXISTS {}").format(dataBaseName)
    mycursor.execute(a)
    c = ("Use {}").format(dataBaseName)
    mycursor.execute(c)
    b = ("CREATE TABLE IF NOT EXISTS {} (ID INT, NAME VARCHAR(15), LASTNAME VARCHAR(15), FATHERNAME VARCHAR(20), EMAIL VARCHAR(20), AGE INT, PHONE VARCHAR(20), SALARY INT)").format(tableName)
    mycursor.execute(b) 
    drop = "DROP DATABASE {}".format(dbName)
    mycursor.execute(drop)

