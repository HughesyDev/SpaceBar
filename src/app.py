import csv
import unittest
import os, sys
import time
from src.constants import PEOPLE_FILEPATH, DRINKS_FILEPATH
from src.core.persistence.data_persistence import save_data
from src.core.formatting.formatting_funcs import menu_text, get_table_width, print_header, print_line, menu_text, create_table, clear_and_show_logo
from src.core.formatting.ascii_greeter import maingreeter, greeting_ascii_art
from src.models.Round import Round

drinks = []
people = []
preferences = {}

# Prepare data, display menu, prompt for menu selection

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

def menu():
    '''# Base menu that displays on program start'''
    os.system("clear")
    greeting_ascii_art()
    menu_text()
    try:
        answer = int(input("\nEnter your selection: "))
    except:
        menu()
    print("")
    time.sleep(.500)
    response(answer)
    
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
            print(f"{item_to_add} has been added.")
            time.sleep(1)

        elif answer == 5: # Add Drink
            print("Enter a drink to add: ")
            drink_to_add = input(">>> ")
            add_to_list(drinks, drink_to_add)

        elif answer == 6: # define favourites
            faves_handler()

        elif answer == 7: # print faves
            print_faves()
        elif answer == 8: # save and quit
            save_data(PEOPLE_FILEPATH, people)
            save_data(DRINKS_FILEPATH, drinks)
            quit()
        elif answer == "" or " ":
            menu()
        else:
            os.system("clear")
            greeting_ascii_art()
            menu_text()
            print("I'm sorry, I didn't understand that response, please try again.\n")
            answer = int(input("\nEnter your selection: "))
            response(answer)
            os.system("clear")
            menu()
    except Exception as e:
        os.system("clear")
        print(f"Exception raised with the following error:\n {e}\n")
        print("Returning to Menu.")
        os.system("clear")
        menu()

# Menu selection leads to the below

def add_to_list(add_to, item_to_add):
    global drinks
    global people
    try:
        return add_to.append(item_to_add)
    except Exception as e:
        print(f"Exception occurred:\n\n {e}")
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

# favourites_handling_funcs

def faves_handler_check_validity(name):
    if name not in people:
        print(f"{name} is not recognised as a valid member of your party")
        print("Do you want to add them to your party? [Y/n]")

        try:
            answer = input(">>> ")
            if answer.lower() == "y" or "yes":
                people.append(name)
            else:
                print("Returning to menu.")
                time.sleep(1)
                return menu()
        except:
            return menu()

def faves_handler():
    print("Please enter a name: ")
    name = input(">>> ")

    faves_handler_check_validity(name)

    if name in preferences.keys():
        return f"{name} already has a favourite set."

    print("What is their preferred drink?")
    fave_drink = input(">>> ")

    define_faves(name, fave_drink)
    run_again()

def define_faves(name, fave_drink):
    global preferences
    global people

    try:
        preferences[name] = fave_drink
        print(f"\n{name}'s favourite now set to: {fave_drink}\n")
    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")
    return

def print_faves():
    if not preferences:
        print("\nNo favourites have been added yet.\n")
    else:
        for key, value in preferences.items():
            print(f"{str(key.title())}'s favourite: {str(value.title())}")
    run_again()

# App helper runcs

def run_again():
    '''# Prompts user to hit Enter to return to the menu'''
    while True:
        try:
            _answer = input("\nPress enter to return to the menu.")
            menu()
        except EOFError:
            break

# Entry point / funcs

def start():
        load_data()         # load data from file into people, drinks list.
        maingreeter()       # display ASCII greeter, waits for any input
        os.system("clear")  # clear screen to refine display
        menu()              # call menu, ASCII replaced by identical art, menu displays underneath
        
if __name__ == "__main__":
    start()