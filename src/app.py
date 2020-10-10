import csv
import unittest
import os
import sys
import time
from src.constants import PEOPLE_FILEPATH, DRINKS_FILEPATH
from src.core.persistence.data_persistence import save_data
from src.core.formatting.formatting_funcs import menu_text,get_table_width,print_header,print_line,create_table,clear_and_show_logo
from src.core.formatting.ascii_greeter import maingreeter, greeting_ascii_art
from src.models.Round import Round
from src.mysql_db import connect, read_drinks_from_db, read_people_from_db, read_prefs_from_db 
from src.mysql_db import input_add_to_drinks , input_add_to_people , write_person_to_db, DRINKS_DATA
from src.mysql_db import PEOPLE_DATA, PREFS_DATA, db_data_in_str, db_prefs_in_str, faves_write_fave_to_db

preferences = {}

def menu():
    '''# Base menu that displays on program start'''
    os.system("clear")
    greeting_ascii_art()
    menu_text()
    try:
        answer = int(input("\nEnter your selection: "))
    except:
        menu()
    time.sleep(.500)
    menu_response_handler(answer)
    
def menu_response_handler(answer):
    '''# Process the users response'''
    print("")
    CREATE_ROUND = 1
    PRINT_PEOPLE = 2
    PRINT_DRINKS = 3
    ADD_PERSON   = 4
    ADD_DRINK    = 5
    SET_DRINK_PREF = 6
    PRINT_DRINK_PREFS  = 7
    SAVE_AND_EXIT_APP = 8 

    try:
        if answer == CREATE_ROUND:
            round_confirmation()

        if answer == PRINT_PEOPLE:   
            read_people_from_db() # asks db for an updated list of people incase this has changed.
            create_table("people", db_data_in_str(PEOPLE_DATA))
            run_again()

        elif answer == PRINT_DRINKS:
            read_drinks_from_db()
            create_table("drinks", db_data_in_str(DRINKS_DATA))
            run_again()

        elif answer == ADD_PERSON: 
            input_add_to_people()
            run_again()

        elif answer == ADD_DRINK: 
            input_add_to_drinks()
            run_again()

        elif answer == SET_DRINK_PREF:
            faves_set_drink_prefs()
            print("\nFavourite has been set.")

        elif answer == PRINT_DRINK_PREFS: 
            read_prefs_from_db()
            create_table("drink preferences", db_prefs_in_str(PREFS_DATA))
            run_again()

        elif answer == SAVE_AND_EXIT_APP:
            #save_data(PEOPLE_FILEPATH, people)
            #save_data(DRINKS_FILEPATH, drinks)
            quit()

        elif answer == "" or " ":
            os.system("clear")
            menu()

        else:
            print("I'm sorry, I didn't understand that response, please try again.\n")
            run_again()

    except Exception as e:
        print(f"Exception raised with the following error:\n {e}\n")
        run_again()

# Round stuff

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
    ADD_AN_ORDER_TO_ROUND = 1
    PRINT_CURRENT_ROUND_DETAILS = 2
    FINALISE_ORDER_PRINT_RECEIPT = 3
    CANCEL_ROUND_EXIT_TO_MENU = 4

    print("\nEnter your selection: ")
    answer = input(">>> ")

    try: 
        if answer == ADD_AN_ORDER_TO_ROUND: 
            name = input("Enter a name:\n>>> ")
            drink - input("What drink:\n>>> ")
        elif answer == PRINT_CURRENT_ROUND_DETAILS:
            pass
        elif answer == FINALISE_ORDER_PRINT_RECEIPT: 
            pass
        elif answer == CANCEL_ROUND_EXIT_TO_MENU: 
            menu()
        else:
            unrecognised_command()

    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")
        run_again()

# favourites_handling_funcs

def faves_set_drink_prefs():
    read_people_from_db()
    read_drinks_from_db()

    try:
        create_table("people", db_data_in_str(PEOPLE_DATA))
        person_id = input("\nPlease enter the ID of the user you wish to set drink preferences for:\n>>> ")
        faves_check_person_id_valid(int(person_id))

        create_table("drinks", db_data_in_str(DRINKS_DATA))
        drink_id = input("\nPlease enter the ID of your preferred drink.\n>>> ")
        faves_check_drink_id_valid(int(drink_id))
        
        faves_write_fave_to_db(person_id, drink_id)

    except Exception as e:
        print(f"ERROR:\n{e}")
    
    finally:
        pass

def faves_check_person_id_valid(person_id):
    if person_id not in PEOPLE_DATA.keys():
        print("I'm sorry, that ID was not recognised. Please enter a valid ID.\n>>> ")
        person_id = input(">>> ")
    return person_id

def faves_check_drink_id_valid(drink_id):
    if drink_id not in DRINKS_DATA.keys():
        print("I'm sorry, that ID was not recognised. Please enter a valid ID.\n>>> ")
        drink_id = input(">>> ")
    return drink_id


# App UX helper funcs

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
        read_drinks_from_db() #now load drinks from db
        read_people_from_db() 
        read_prefs_from_db()
        #maingreeter()       # display ASCII greeter, waits for any input
        os.system("clear")  # clear screen to refine display
        menu()              # call menu, ASCII replaced by identical art, menu displays underneath
        
if __name__ == "__main__":
    start()