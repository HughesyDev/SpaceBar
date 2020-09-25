class Round():
    number_of_rounds = 1

    def __init__(self, bill_payer):
        self.bill_payer = bill_payer
        self.orders = {}
        self.roundnum = f"{Round.number_of_rounds}"
        self.number_of_rounds += 1
        print(f"Round number: {self.roundnum}. Bill-payer: {self.bill_payer}")

    @staticmethod
    def print_round_total():
        print(f"Total number of rounds created is {Round.number_of_rounds}")

    def add_to_order(self):
        # TODO: Select name BY ID from list of names 
        # TODO: Select drink by ID from list of drinks
        name = input("Name: ")

        if name not in people:
            people.append(name)

        drink = input("Drink: ")

        if drink not in drinks:
            drinks.append(drink)

        self.order_details[name] = drink
    
    def print_order(self):
        for name, drink in self.order_details.items():
            print(f"| {name} --> {drink}")
        return


"""class Round():
    total_rounds = 0
    
    @staticmethod
    def print_round_total():
        print(f"Total number of rounds created is {Round.total_rounds}")

    def __init__(self, bill_payer):
        self.bill_payer = bill_payer
        self.order_details = {} # name : drink
        Round.total_rounds += 1
    
    def add_to_order(self):
        # TODO: Select name from list of names instead.
        # TODO: implement validation - name not valid name, ask if they want to add name to their group
        # TODO: Select drink from list of valid drinks
        name = input("Name: ")
        drink = input("Drink: ")
        self.order_details[name] = drink"""