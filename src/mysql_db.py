import pymysql

DRINKS_DATA = {}

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
    
    #for id, drink in DRINKS_DATA.items():
    #    print(f"[{id}] - {drink}")

def db_data_in_str(data): # reformats db data dump from dict into string to print on menu
    data_list = []
    for id, name in data.items():
        data_list.append(f"{id} | {name}")
    return data_list

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