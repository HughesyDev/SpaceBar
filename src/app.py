import csv
import unittest
from os import system, name
from src.constants import PEOPLE_FILEPATH, DRINKS_FILEPATH
from src.core.persistence.data_persistence import save_data
from src.core.formatting.formatting_funcs import menu_text, get_table_width, print_header, print_line, menu_text, create_table
from src.models.Round import Round

# Testing that SSH Auth is working alreet

'''
 - Personalise it! SpaceBar!
 - Alcoholic, non-alc, age limit (ask for age then show either all or non-alcoholic)
 - Testing Suite
 - Use more OOP
 - Generate Unique ID for their order
 - Print a receipt.
'''

drinks = []
people = []
preferences = {}

def load_data():
    global drinks
    global people
    try:
        with open(PEOPLE_FILEPATH, "r") as people_csv: 
            people = people_csv.read().splitlines()

        with open(DRINKS_FILEPATH, "r") as drinks_csv:
            drinks = drinks_csv.read().splitlines()
    
    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")

### App logic

# TODO: rewrite test for round

def add_to_list(add_to, item_to_add):
    global drinks
    global people
    try:
        return add_to.append(item_to_add)
    except Exception as e:
        print(f"Exception occurred: {e}")
    pass

def test_add_to_drinks_list_success():
    # Arrange
    target = drinks
    drink = "Jug of Gravy"

    # Act
    add_to_list(target, drink)
    expected = drink in drinks # should return True

    # Assert
    assert expected == True

'''test_add_to_people_list_success()'''
'''test_add_to_drinks_list_success()'''

def menu():
    '''# Base menu that displays on program start'''
    menu_text()
    answer = input("\nEnter your selection: ")
    response(int(answer)) # send input to response func

def response(answer):
    '''# Process the users response'''
    global drinks
    global people

    try:
        if answer == 1:   # create Round
            round_confirmation()
        if answer == 2:   # print person
            create_table("people", people)
            run_again()
        elif answer == 3: # print drinks
            create_table("drinks", drinks)
            run_again()
        elif answer == 4: # Add person
            print("Enter a name to add: ")
            person_to_add = input(">>> ")
            add_to_list(people, person_to_add)
        elif answer == 5: # Add Drink
            print("Enter a drink to add: ")
            drink_to_add = input(">>> ")
            add_to_list(drinks, drink_to_add)
        elif answer == 6: # define favourites
            print("Please enter a name: ")
            name = input(">>> ")
            
            if name in preferences.keys():
                return f"{name} already has a favourite set."

            print("What is their preferred drink?")
            fave_drink = input(">>> ")

            define_faves(name, fave_drink)
            
            run_again()
        elif answer == 7: # print faves
            print("\n")
            print_faves()
            print("\n")
        elif answer == 8: # save and quit
            save_data(PEOPLE_FILEPATH, people)
            save_data(DRINKS_FILEPATH, drinks)
            quit()
        else:
            unrecognised_command()
    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")
        print("Returning to Menu.")
        menu()

def round_confirmation():
    print("Who is paying for this round?")
    bill_payer = input(">>> ")

    if bill_payer not in people:
            people.append(bill_payer) # bill payer just joined, therefore added to list of group
            
    current_round = Round(bill_payer)
    round_submenu()

def round_submenu():
    print("[1] Add an order to the round.")
    print("[2] Check current round information.")
    print("[3] Finalise order.")
    print("[4] Cancel round and return to menu")
    choice = int(input(">>> "))
    round_submenu_choice(choice)

def round_submenu_choice(choice):
    print("\nEnter your selection: ")
    answer = input(">>> ")

    if answer == 1: # add order to round
        name = input("Enter a name:\n>>> ")
        drink - input("What drink:\n>>> ")

    elif answer == 2: # check curr round info
        pass
    elif answer == 3: # finalise order, print receipt
        pass
    elif answer == 4: # cancel round and exit to menu
        menu()


    try:
        if answer == 1:   # Add order to round
            pass
        elif answer == 2:   # Print current round info
            pass
        elif answer == 3:   # "Finalise" order
            pass
        elif answer == 4:   # Cancel Round and exit to menu
            pass
        else:
            unrecognised_command()

    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")
        print("Returning to Menu.")
        menu()


def unrecognised_command():
    print("Unrecognised command")
    pass

def define_faves(name, fave_drink):
    global preferences
    global people
    try:
        preferences[name] = fave_drink
        print(f"\n{name}'s favourite now set to: {fave_drink}\n")
    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")
    return

def test_define_faves_success():
    # Arrange
    test_person = "TEST USER"
    test_drink = "FAVE DRINK"
    # Act
    define_faves(test_person, test_drink)
    expected_name_in_faves  = test_person in preferences.keys()
    expected_drink_in_faves = preferences[test_person] == test_drink

    # Assert
    assert expected_name_in_faves == True
    assert expected_drink_in_faves == True

'''test_define_faves_success()'''

def print_faves():
    if not preferences:
        print("\nNo favourites have been added yet.\n")
    else:
        for key, value in preferences.items():
            print(f"{str(key.title())}'s favourite: {str(value.title())}")
    run_again()

def run_again():
    '''# Prompts user to hit Enter to return to the menu'''
    while True:
        try:
            _answer = input("Press enter to return to the menu.")
            menu()
        except EOFError:
            break

def start():
    """Loads data from file into data structs, then starts the menu"""
    if __name__ == "__main__":
        load_data()
        menu()

# Entry point
start()