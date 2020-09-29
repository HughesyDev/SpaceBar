import pymysql
import pymysql.cursors

connection = pymysql.connect(host='192.168.99.100',
                            port=33066,
                            user='root',
                            password='password',
                            db='SpaceBar',
                            )

drink_name = 'Test Diet Coke'
alcoholic = False
price = 01.30

try:
    with connection.cursor() as cursor:
        
        sql = f"INSERT INTO 'drinks' ('drink_name', 'alcoholic', 'price') VALUES (, {alcoholic}, {price})"
        cursor.execute(sql, ('Diet Coke', False, 1.40))
    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()

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