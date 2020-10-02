import pymysql

'''DONE: Is there a separate python module / package for the app's data persistence?	YES	NO'''
'''TODO: Can the app read people drinks and preferences from a mysql database?	YES	NO	'''
'''TODO: Can the app save people drinks and preferences to a mysql database?	YES	NO	'''
'''TODO: Does the people table include first and last names, and drink preference?	YES	NO	'''
'''TODO: Does the drink table hold extra drink information such as temperature, milk percentage and quantity?	YES	NO'''	
'''TODO: Does your app prevent duplicate people or drinks being entered into the database?	YES	NO'''

# What you did
# What challenges you faced.
# Prezi for presenting it - create small demo presentation / or Google Slides
# DEMO IS A WEEK ON TUESDAY to people from other cohort, Infinity Works people.

# REMEMBER: each bit of work in feature branch is its own commit, when finished, MERGE.

 # new person = provide name, then they're created on the db, 
 # then pull the id down as the name of the instance?
 # Person will have fave attrib, but that's set separately from db

# How menu will work with DBs
# DB auto loads into data structs
# When person/drink is added, connect to db, add, then pull new db info into data structs.

# Fetch drink data into data dump
# loop through data dump creating instances of drink classes out of each one
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



def read_drinks_from_db():  
    db, cursor = connect()
    DRINKS_DATA = {}
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
    
    for id, drink in DRINKS_DATA.items():
        print(f"[{id}] - {drink}")

## Add to DB funcs

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