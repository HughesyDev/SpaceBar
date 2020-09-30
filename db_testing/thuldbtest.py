import pymysql

def ReadDatabase():
	connection = pymysql.connect(
		host = "192.168.99.100", # I need to use IP instead of "localhost" due to using Docker Toolbox instead of Docker Desktop
        port = 33066,
		user = "root",
		password= "password",
		db= "SpaceBar")

    try with connection.cursor() as cursor:
        #args = (123, "americano", "coffee", "hot")
        #cursor.execute("SELECT FROM person_id, first_name, surname, age FROM Person")
        cursor.execute("SELECT person_id, first_name, surname, age FROM Person")
        rows = cursor.fetchone()

        for row in rows:
            print(row)
    finally:
        cursor.close()
        connection.close()

ReadDatabase()

#if __name__ == "__main__":
#    ReadDatabase()
            cursor.execute("INSERT INTO drink_test (drink_name, alcoholic, price) VALUES ('coke', 0, 02.20)")
            connection.commit()
        cursor.close()
    finally:
        connection.close()