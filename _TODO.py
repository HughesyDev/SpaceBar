# DEMO:
# 1. PRESENTATION
#     - What challenges you faced
#     - What you would develop if you had more time?
#     - What 
# 2. DEMO APP
#     - Make sure it actually works beforehand, TEST that anything taking input accepts the correct input and handles invalid input.

# # DEMO IS A WEEK ON TUESDAY to people from other cohort, Infinity Works people.

# Look into UUID? Unique Identifier (low collision chance of hash thing?)


''' "SPECIAL SAUCE"
 Cheryse's had nice printout of rounds, it had age/alcoholic drinks etc.
 # What can you do for yours?
'''

# TODO: Change "Add drink" to "check if a drink you like is in stock."
# TODO: Check what user added against a SET of many more drinks. If in stock: return it, add to db, load from db.

# TODO: Add column for hot/cold drinks
# TODO: Ask user if they want to see hot drinks or cold drinks table.
# TODO: Hot drinks also have additional properties: milk, sugar, complementary biscuit.

# TODO: Create Drinks class? Subclass for hot / cold? (STRETCH goal)

# TODO: ##### Add an actual proper list of drinks.

# MUST: 
''' DONE: Reimplement people retrieval/adding via db'''
''' DONE: Reimplement drinks retrieval/adding via db'''
''' DONE: Add prefs column to people which is FK to drink_id''' # My GOD this took ages
''' DONE: Reimplement pref adding via db'''
''' DONE: Allow user to set their drink preference by name_id & drink_id'''
''' DONE: Amend people table to accept firstname and surname.'''
# TODO BRANCH: Add validation for adding people/drinks to catch empty strings.
''' DONE: First Draft of JDE CV -  look through CherryTree notes'''



# -----------------------

# SHOULD:
# TODO BRANCH: Complete Round class setup (without db interaction)

# -----------------------

# COULD:
''' DONE: Allowing user to update their drink preference'''
''' DONE: Stop user from adding duplicate entries to people'''
''' DONE: Stop user from adding duplicate entries to drinks'''
# TODO BRANCH: Persist Round information in the db (if not exists, create new table for each round with nameid, drinkid, save it)
# TODO BRANCH: Unit testing 
# TODO BRANCH: Make intro words write onto the screen instead of appearing (so char by char display like they're typed)
# TODO: Make Python --m Unittest.py or something work. Test Suite
# TODO: Does the drink table hold extra drink information such as temperature, milk percentage and quantity?	YES	NO'''	


# TODO BRANCH: ETL stuff (import from CSV into file in correct format)
# TODO: If table empty (i.e. all items deleted), then recreate table so all new items start index at 1 from the new table


# - Testing Suite
# - Use more OOP
# - Generate Unique ID for their order
# - Print a receipt.

# EXTRA FEATURES
# - Leaderboards
# - Brew stats: most popular brew, brews per round etc.
# - A Slack bot