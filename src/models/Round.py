class Round():
    """Round class to ensure all round instances have identical template"""
    #round_directory = []

    def __init__(self, title, bill_payer):
        self.bill_payer = bill_payer
        self.title = title
        self.orders = {}
        #Round.round_directory.append(self)
        #print(round_directory)
     
    def add_to_round(self, name, drink):
        # prompt for input (select name, drink by their ID)
        # add name : drink to self.orders dict
        self.orders[name] = drink
        return

    def delete_round_choice(self):
        self.show_current_round()
        user_in_current_round = None
        user_in_current_round = input("Enter name of person to remove the order of:\n>>> ")

        if user_in_current_round in self.orders.keys():
            pass

        while user_in_current_round not in self.orders.keys(): 
            user_in_current_round = input("User not recognised. Please re-enter a valid name:\n>>> ")

    def cancel_round(self):
        #round_directory.remove(self)
        # not implemented atm due to round not being stored in db.
        pass

    def print_round_receipt(self):
        # self-explanatory, maybe involve tabulation in this module?
        print('''
                     __    _            __                   __         __
          ___  ___  / /_  (_)_ _  ___  / /__ __ _  ___ ___  / /____ ___/ /
         / _ \/ _ \/ __/ / /  ' \/ _ \/ / -_)  ' \/ -_) _ \/ __/ -_) _  / 
        /_//_/\___/\__/ /_/_/_/_/ .__/_/\__/_/_/_/\__/_//_/\__/\__/\_,_/  
                               /_/                                        
                        ''')
        return
        
    
