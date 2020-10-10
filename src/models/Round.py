class Round():
    def __init__(self, bill_payer):
        self.bill_payer = bill_payer
        self.orders = {}
     
    def add_to_round(self):
        # prompt for input (select name, drink by their ID)
        # add name : drink to self.orders dict
        pass

    def show_current_round(self):
        # show what each person has selected so far show table with: "name" : "drink"
        # DON'T show names of people who haven't ordered anything (like you do with prefs: none)
        pass

    def amend_round_choice(self):
        # prints current round, you select person by ID and change their drink to another ID
        pass

    def print_round_receipt(self):
        # self-explanatory, maybe involve tabulation in this module?
        pass
    
