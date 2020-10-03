import pymysql
import time

DRINKS_DATA = {}
PEOPLE_DATA = {}

def connect():
    db = pymysql.connect(host="localhost", 
                            port=33066,
                            db="SpaceBar",
                            user="root",
                            password="password",
                            autocommit=True
                            )
    cursor = db.cursor()
    return db, cursor

### DRINKS

def read_drinks_from_db():  
    db, cursor = connect()
    global DRINKS_DATA
    RETRIEVE_DRINKS_QUERY = 'SELECT * FROM drinks'

    try:
        with cursor:
            cursor.execute(RETRIEVE_DRINKS_QUERY)
            drinks_dump = cursor.fetchall()

    except error as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()
    
    # Dump db drink data into the empty dict
    for id, drink in drinks_dump:
        DRINKS_DATA[id] = drink

def input_add_to_drinks():
    print("What drink do you want to add?")
    drink_to_be_added = input(">>> ").strip() #remove whitespace before/after
    write_to_db(drink_to_be_added)

def write_drinks_to_db(drink_to_be_added):
    db, cursor = connect()
    # The query we send to the db
    sql = 'INSERT INTO drinks (drink_name) VALUES (%s)'
    val = drink_to_be_added

    try:
        with cursor:
            cursor.execute(sql, val)
    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()


### PEOPLE

def read_people_from_db():  
    db, cursor = connect()
    global PEOPLE_DATA
    RETRIEVE_PEOPLE_QUERY = 'SELECT * FROM people'

    try:
        with cursor:
            cursor.execute(RETRIEVE_PEOPLE_QUERY)
            people_dump = cursor.fetchall()

    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()
    
    # Dump db drink data into empty PEOPLE_DATA dict
    for id, first_name, last_name in people_dump:
        first_name = str(first_name)
        last_name = str(last_name)
        PEOPLE_DATA[id] = first_name + " " + last_name

def input_add_to_people():
    print("Who do you want to add?")
    try:
        first_name = input("\nFirst name:\n>>> ").strip() #remove whitespace before/after
        last_name = input("\nLast name:\n>>> ").strip()

        full_name = first_name + " " + last_name

        if dupe_checker(full_name):
            return

        else:
            return write_person_to_db(first_name, last_name)

    except Exception as e:
        print(f"ERROR:\n{e}")
        pass

    finally:
        return
def dupe_checker(full_name):
    if full_name in PEOPLE_DATA.values():
        print(f"{full_name} is a duplicate name and cannot be added again.")
        time.sleep(1)
        return True

def write_person_to_db(first_name, last_name):
    db, cursor = connect()

    # The query we send to the db
    sql = 'INSERT INTO people (first_name, last_name) VALUES (%s, %s)'
    val = first_name, last_name

    try:
        with cursor:
            cursor.execute(sql, val)
    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()


#### 

def db_data_in_str(data): # reformats db data dump from dict into string to print on menu
    data_list = []
    for id, name in data.items():
        data_list.append(f"{id} | {name}")
    return data_list