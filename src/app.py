import csv
import unittest
import os
import sys
import time
from datetime import datetime
from src.constants import PEOPLE_FILEPATH, DRINKS_FILEPATH
from src.core.persistence.data_persistence import save_data
from src.core.formatting.formatting_funcs import menu_text,get_table_width,print_header,print_line,create_table,clear_and_show_logo, new_table
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
    CREATE_ROUND     = 1
    PRINT_PEOPLE     = 2
    PRINT_DRINKS     = 3
    ADD_PERSON       = 4
    ADD_DRINK        = 5
    SET_PREFS        = 6
    PRINT_PREFS      = 7
    EXIT_APP         = 8

    try:
        if answer == CREATE_ROUND:
            round_initialisation()

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

        elif answer == SET_PREFS:
            faves_set_drink_prefs()
            print("\nFavourite has been set.")

        elif answer == PRINT_PREFS: 
            read_prefs_from_db()
            create_table("drink preferences", db_prefs_in_str(PREFS_DATA))
            run_again()

        elif answer == EXIT_APP or "exit" or "quit":
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

# Round handler functions

def round_submenu_text(round):
    os.system("clear")
    greeting_ascii_art()
    print(f"Your round ID: '{round.title}'")
    print(f"Bill-payer for this round: {round.bill_payer}\n")

    print("  1 | Add an order to the round.")
    print("  2 | Print round details.")
    print("  3 | Complete your order.")
    print("  4 | Cancel and return to menu")

def round_initialisation():
    read_people_from_db() # asks db for an updated list of people incase this has changed.
    read_drinks_from_db()

    try:
        create_table("people", db_data_in_str(PEOPLE_DATA))
        bill_payer = input("\nPlease enter the ID of the bill payer for this round:\n>>> ")

        while len(bill_payer) == 0:
            bill_payer = input(("Bill payer cannot be empty. Please re-enter a valid ID:\n>>> "))
        
        bill_payer = int(bill_payer)


        if bill_payer not in PEOPLE_DATA.keys():
            print("This user is not recognised")
            run_again()
        
        bill_payer = PEOPLE_DATA[bill_payer] # transform ID into the respective name for person/drink
        bill_payer = bill_payer.replace(" ", "_").lower() # tidy up display

        # Generate unique-ish, but meaningful title for the round.
        round_title = f"{bill_payer}_{current_time()}" # example "[ID][HH:MM:SS]" --> angelica_23:27:16
        round_title = Round(round_title, bill_payer) # initialise the round, set title and bill-payer

        round_submenu_handler(round_title) # send the initialised round obj to handler to further modify

    except Exception as e: 
        print(f"round_initialisation ERROR with:\n>>>{e}")
        run_again()

def round_submenu_handler(round):
    ADD_AN_ORDER_TO_ROUND = 1
    PRINT_CURRENT_ROUND_DETAILS = 2
    FINALISE_ORDER = 3
    CANCEL_ROUND_EXIT_TO_MENU = 4

    round_submenu_text(round)
    

    try: 
        submenu_selection = input("\nEnter menu selection:\n>>> ")
        
        while True:
            if len(submenu_selection) == 0:
                submenu_selection = input("Invalid input. Please try again:\n>>> ")
            
            elif submenu_selection.isnumeric():
                break
            else:
                submenu_selection = input("Invalid input. Please try again:\n>>> ")

        submenu_selection = int(submenu_selection)

        if submenu_selection == ADD_AN_ORDER_TO_ROUND: 
            round_submenu_text(round)
            print("")
            create_table("people", db_data_in_str(PEOPLE_DATA))
            person_id = int(input("\nChoose person by their ID number:\n>>> "))

            round_submenu_text(round)
            print("")
            create_table("drinks", db_data_in_str(DRINKS_DATA))
            drink_id = int(input("\nChoose drink by its ID number:\n>>> "))



            person_name = PEOPLE_DATA[person_id] # transform ID into the respective name
            drink_name  = DRINKS_DATA[drink_id]

            round.add_to_round(person_name, drink_name)
            print(f"\nOrder added to round.")
            round_run_again(round)

        elif submenu_selection == PRINT_CURRENT_ROUND_DETAILS:
            print("")
            new_table("Round Details", round.orders)
            round_run_again(round)

        elif submenu_selection == FINALISE_ORDER: 
            print("")
            output = [
                    "Sending your order to bar staff...",
                    "Order received...",
                    "Your drinks will be with you shortly.",
                    "...",
                    "Receipt formatting not yet implemented <3"]

            for item in output:
                print(item, flush=True)
                time.sleep(2)

            run_again()

        elif submenu_selection == CANCEL_ROUND_EXIT_TO_MENU: 
            menu()

        else:
            unrecognised_command()

    except Exception as e:
        print(f"Exception raised with the following error:\n {e}")
        round_run_again(round)

def round_run_again(round):
    '''# Prompts user to hit Enter to return to the round submenu'''
    while True:
        try:
            _answer = input("\nPress enter to return to the round submenu.")
            round_submenu_handler(round)
        except Exception:
            break
    


# drink-preferences handler functions

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
        except Exception:
            break

def current_time():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time

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