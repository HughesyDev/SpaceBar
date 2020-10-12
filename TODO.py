# Upload Prezi slide to LinkedIn ?

#~~~~~~~~~~ MUST: 
''' DONE: Reimplement people retrieval/adding via db'''
''' DONE: Reimplement drinks retrieval/adding via db'''
''' DONE: Add prefs column to people which is FK to drink_id''' # My GOD this took ages
''' DONE: Reimplement pref adding via db'''
''' DONE: Allow user to set their drink preference by name_id & drink_id'''
''' DONE: Amend people table to accept firstname and surname.'''
''' DONE: Add validation for adding people/drinks to catch empty strings.'''
''' DONE: First Draft of JDE CV -  look through CherryTree notes'''
''' DONE: BRANCH: Add an actual proper list of drinks (Coke, Lemonade, Water)'''
# TODO: Try to look for places where you can make the code more readable / "read like a story"

#~~~~~~~~~~ SHOULD:
''' DONE: Reimplement Round class setup (without db interaction)'''
# TODO BRANCH: Round: add receipt output

''' DONE: Fix formatting to take in two columns of data for prefs/orders.'''

#~~~~~~~~~~ COULD:
''' DONE: Allowing user to update their drink preference'''
''' DONE: Stop user from adding duplicate entries to people'''
''' DONE: Stop user from adding duplicate entries to drinks'''
# TODO: Ensure named placeholders used for all db-write functions.

# TODO BRANCH: Persist Round information in the db (
        # Round table
        # Give each instance of Round a UniqueID ("bill_payer" + datetime of instance initialisation)
        # Then add the roundID, name, drink to table
        # Keep track of each unique instance ID

# TODO BRANCH: Unit testing / Pytest
# TODO: Change "Add drink" to "check if a drink you like is in stock."
        # Check what user added against a SET of many more drinks. If in stock: return it, add to db, load from db.
# TODO BRANCH: Round: set drink_pref as default drink choice?
# TODO BRANCH: Refactor menu_response code from if block to dict?
# TODO BRANCH: Make intro words write onto the screen instead of appearing (so char by char display like they're typed)
# TODO BRANCH: create a function that rips down db tables and recreates to make dev easier

# TODO: Implement Drinks class. 
        # Subclass for hot drinks / cold drinks
        # Add column for hot/cold drinks in drinks table
        # Add column (bool) for alcoholic/not
        # Ask user if they want to see hot drinks or cold drinks table.
        # Hot drinks also have additional properties: milk, sugar, complementary biscuit.

# TODO BRANCH: ETL stuff (import from CSV into file in correct format)
# TODO: If table empty (i.e. all items deleted), then recreate table so all new items start index at 1 from the new table



# ~~~~~~~~~~ 

# Look into UUID? Unique Identifier (low collision chance of hash thing?)

# - Testing Suite
# - Use more OOP
# - Generate Unique ID for their order
# - Print a receipt.

# EXTRA FEATURES
# - Leaderboards
# - Brew stats: most popular brew, brews per round etc.
# - A Slack bot