import pymysql



def main2(): # Writing into table in testdb
    connection = pymysql.connect(host="192.168.99.100", 
                                port=33066,
                                user="root",
                                password="password",
                                db="SpaceBar")

    
    try:
        with connection.cursor() as cursor:
            cursor.execute("INSERT INTO drink_test (drink_name, alcoholic, price) VALUES ('coke', 0, 02.20)")
            connection.commit()
        cursor.close()
    finally:
        connection.close()

def main(): # reading from two tables in test db
    connection = pymysql.connect(host="192.168.99.100", 
                                port=33066,
                                user="root",
                                password="password",
                                db="SpaceBar")

    try:
        test1 = 'test1'
        test2 = 0
        test3 = 01.00
        with connection.cursor() as cursor:
            
            cursor.execute("INSERT INTO drink_test (drink_name, alcoholic, price) VALUES ({}, {}, {})".format(test1, test2, test3))
            connection.commit()
        cursor.close()
    finally:
        connection.close()

main()


'''import pymysql as sql

def connect_database():
    connection = sql.connect(host = "localhost", port = 33066, user = "root", passwd = "password", db = "TonicDB")
    cursor = connection.cursor()
    #cursor.execute("SELECT drinkID FROM Drinks")
    cursor.execute('SELECT IF(500<1000, "TRUE", "FALSE")')
    connection.commit()
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    
    for row in rows:
        print(row)

    print("rows")
    return'''

'''drink_name = 'Test Diet Coke'
alcoholic = False
price = 01.30

try:
    with connection.cursor() as cursor:
        sql = f"INSERT INTO 'drink_test' ('drink_name', 'alcoholic', 'price') VALUES ({drink_name}, {alcoholic}, {price})"
        cursor.execute(sql, ('Diet Coke', False, 1.40))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()'''

'''def main():
connection = pymysql.connect(
    host="192.168.99.100:8080/",
    port=33066
    user="root",
    passwd="password",
    database="SpaceBar"
)

cursor = connection.cursor()
args = (123, "americano", "coffee", "hot")
cursor.execute("INSERT INTO drink (id, name, type, temp) VALUES (%s, %s, %s, %s)", args)
connection.commit()
cursor.close()
connection.close()'''
