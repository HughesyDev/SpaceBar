Steps to take:

Goal of the refactor: simplify behaviour, make app easier to understand.
use TDD to guide the refactor

- [ ] Create Customer Class
- [ ] Create Drinks Class
- [ ] Create Tabulation Class
- [ ] 
- [ ] 
- [ ] 
- [ ] Implement CI with automate tests at commit to improve the feedback loop.
- [ ] set up Continuous Integration with GitHub Actions
- [ ] set up automated test suite with GitHub Actions
- [ ] set up prod-like test environment with a Docker vers. of things
- [ ] set up automated IaC to build test env, perform Acceptance Tests
- [ ] Add logging
- [ ] Capture Documentation with Sphinx?
- [ ] Use professional linters? 
- [ ] Get familiar with PDB or PUDB debuggers
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 
- [ ] 


Look up Agile / Extreme Programming methods



The BrewApp Could be something requiring further data cleaning, i.e.
- you have members of a department and list of unnecessary data. We scrub out what we don't want and feed it through a method on Person class which cleans it to retrieve only the data we want.

- [ ] Linting / Debugging etc. More professional stuff.
- [ ] More complex DB stuff - STAR schema - udemy Data Warehousing course

Create a Deployment Pipeline for one SLICE of the project functionality. Then fold other functionality into that pipeline.

Repackage the code to use as a desktop app etc.?


MINIMUM VIABLE PRODUCT
- TEST THE INTENDED BEHAVIOUR OF THE PERSON CLASS
- First you have the Person Class
- Person class can order a drink
- TEST IT WORKS

Then TDD - create a test for a Drinks Class, creating a drink
hen make a drink class
- properties
	- name
	- price
	- quantity
- methods
	- add drink

subclass HotDrink
	- milk
	- sugars
	- complementary biscuits
subclass ColdDrink
	- 


End-goal -- you have a tabulated Round receipt with pricing on it

Overview:
- There is a group of people.
- There is a person designated "brewer"
- There is one round per brewer, though new rounds can have favourited drinks or 

Reduce complexity - no alcoholic -- pretend it's a work environment.

### MUST: 
- [ ] Be able to create an instance of person
- [ ] 

TODO (ongoing): Look for places in the code where you can make the code more readable / "read like a story"

### SHOULD:


### COULD:
- fake data generator
        - we create fake people to add to a fake party, who make fake orders
        - realtime analytics / visualisation on that data?

###### TODO: Create new branch and refactor menu_response function into a dictionary of text:function pairs?

###### TODO: reimplement Drinks as a Drinks Class.
        # Ask user if they want to see hot drinks or cold drinks table.
        # Hot drinks also have additional properties: milk, sugar, complementary biscuit.

###### TODO BRANCH: Persist Round information in the db (
        # Round table
        # Give each instance of Round a UniqueID ("bill_payer" + datetime of instance initialisation)
        # Then add the roundID, name, drink to table
        # Keep track of each unique instance ID

###### TODO: Round: set drink_pref as default drink choice?

###### TODO: Round: add receipt output

###### TODO: Unit testing / Pytest

###### TODO: Change "Add drink" to "check if a drink you like is in stock."
        # Check what user added against a SET of many more drinks. If in stock: return it, add to db, load from db.
        # Store "drink stock" in the built-in Python db? Or use CSV / JSON?

###### TODO: Make intro words write onto the screen character-by-character as though they were typed.