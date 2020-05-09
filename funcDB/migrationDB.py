import mysql.connector
from mysql.connector import Error
def mainMigration(ip, dbName, tableName, user, passwd, migrationData):
    print("Wa are in mainMigration")
    try:
        mydb = mysql.connector.connect(
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
    except Error as e:
        print("Error while connecting to MySQL", e)

def mainCreate(dataBaseName, tableName, user, passwd, ip):
    mydb = mysql.connector.connect(
    host=ip,
    user=user,
    passwd=passwd
    )
    mycursor = mydb.cursor()
    a = ("CREATE DATABASE IF NOT EXISTS {}").format(dataBaseName)
    mycursor.execute(a)
    c = ("Use {}").format(dataBaseName)
    mycursor.execute(c)
    b = ("CREATE TABLE IF NOT EXISTS {} (ID INT, NAME VARCHAR(15), LASTNAME VARCHAR(15), FATHERNAME VARCHAR(20), EMAIL VARCHAR(20), AGE INT, PHONE VARCHAR(20), SALARY INT)").format(tableName)
    mycursor.execute(b)

