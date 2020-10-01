import pymysql

# create func that loads people from db into an empty
# ### loading from db into a class (?) or just into a list? Or a dict?
# Dict comprehension feasibility?
# List comprehension?


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
    drinks_from_db = [] # init empty list to dump db data into

    # The thing we say to the db
    test_query = 'SELECT * FROM drinks'

    try:
        #print("Begin executing the cursor thing")
        cursor.execute(test_query)

        #print("Fetch all should be next")
        drinks_from_db = cursor.fetchall()

    except error as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()
        #print("The connection has closed")
        #print("Printing drinks_from_db")
        print(drinks_from_db)

#read_drinks_from_db()

def input_add_to_drinks():
    print("What drink do you want to add?\n")
    capture = input(">>> ")
    drink_to_be_added = str(capture)
    write_to_db(drink_to_be_added)

input_add_to_drinks()

def write_to_db(drink_to_be_added):
    # The thing we say to the db
    query = str(f'INSERT INTO drinks (drink_name) VALUES ('{drink_to_be_added}'))
    try:
        print("Begin executing the cursor thing")
        cursor.execute(query)
        
        # connection is not autocommit by default. So you must commit to save
        # your changes.
        print("\nCommit the thing (by default now)")
        #db.commit()
    except error as err:
        print(f"ERROR with:\n{err}")

    finally:
        cursor.close()
        db.close()
        print("\nThe connection has closed")

write_to_db()
