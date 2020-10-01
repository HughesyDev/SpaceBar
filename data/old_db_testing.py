import pymysql

'''DONE: Is there a separate python module / package for the app's data persistence?	YES	NO'''
'''TODO: Can the app read people drinks and preferences from a mysql database?	YES	NO	'''
'''TODO: Can the app save people drinks and preferences to a mysql database?	YES	NO	'''
'''TODO: Does the people table include first and last names, and drink preference?	YES	NO	'''
'''TODO: Does the drink table hold extra drink information such as temperature, milk percentage and quantity?	YES	NO'''	
'''TODO: Does your app prevent duplicate people or drinks being entered into the database?	YES	NO'''

# create func that loads people from db into an empty
# ### loading from db into a class (?) or just into a list? Or a dict?
# Dict comprehension feasibility?
# List comprehension?

# RE classes
# both person and drink class should have attrib, ID, NAME, FAVE(?)

# PULL DATA FROM DB DOWN INTO LIST as set of tuples
# For row in list of people:
# id = name of instance of person class
# person.id
# person.name
# person.fave (not from db (yet) ) 

# How menu will work with DBs
# DB auto loads into data structs
# When person/drink is added, connect to db, add, then pull new db info into data structs.

# db testing

 # id (autoincremented) and drink_name
people_from_db = [] # id (autoincremented) and person_name


# db is the connectio nto
db = pymysql.connect(host="localhost", 
                    port=33066,
                    db="SpaceBar",
                    user="root",
                    password="password",
                    autocommit=True
                    )

# Cursor object that interacts with the db
cursor = db.cursor()

# Putting it all together
def read_drinks_from_db():   

    # The thing we say to the db
    test_query = 'SELECT * FROM drinks'

    try:
        #print("\nBegin executing the cursor against the db")
        cursor.execute(test_query)

        #print("\nFetch all should be next")
        drinks_dump = cursor.fetchall()

    except error as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()

    #print("\nThe connection has closed")
    #print("\nPrinting drinks_from_db")

    for id, drink in drinks_dump:
        print(f"[{index}] - {drink}")
    
    for id, drink in drinks_dump:



read_drinks_from_db()

def input_add_to_drinks():
    print("What drink do you want to add?")
    drink_to_be_added = input(">>> ").strip() #remove whitespace before/after
    write_to_db(drink_to_be_added)

def write_to_db(drink_to_be_added):
    # The query we send to the db
    sql = 'INSERT INTO drinks (drink_name) VALUES (%s)'
    val = drink_to_be_added

    try:
        print("\nBegin executing the cursor thing")
        cursor.execute(sql, val)
        
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        print("\nCommit the thing (by default now)")
        #db.commit()
    except Exception as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()
        print("\nThe connection has closed")

# input_add_to_drinks()