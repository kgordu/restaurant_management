class Restaurant:
    def __init__(self, menu_items, tables, customer_orders, customer_budget):
        self.menu_items = menu_items
        self.tables = tables
        self.customer_orders = customer_orders
        self.customer_budget = customer_budget

#Print the dishes in the menu with their prices
    def print_menu(self):
        column_width = 5
        print(f'The current menu is:\n')
        for dish, price in self.menu_items.items():
            print(f'{dish} for {str(price).ljust(column_width)}€.') 

#Use this function add any dish with a given price
    def add_item_to_menu(self):
        item_to_add = input(f'What would you like to add to our menu?: ').capitalize()
        price_to_add = float(input(f'How much would it cost?: '))
        self.menu_items[item_to_add] = price_to_add
        print(f'{item_to_add} is added to the restaurant menu.')
        answer = input(
            f'Would you like to add one portion of it to your order list?\n'
            f'Please write me \'YES (Y)\' or \'NO (N)\': '
            )
    #Ask if the customer want to add that item and price into the list. If yes, add to customer_orders to count later
        if answer.upper() == 'YES' or answer.upper() == 'Y':
            self.customer_orders[item_to_add] = 1
        return self.menu_items, self.customer_orders
    
#Reserve a table
    def book_table(self):
    #Ask the preferred table number
        wanted_table_number = int(input(f'Which table would you like to have? Give me a table number please, Sir: '))
        wanted_index = wanted_table_number - 1      #Given table number == its index + 1, process the index below
    #Check if the table number is valid and empty
        if wanted_index < len(self.tables) and self.tables[wanted_index] == 'EMPTY':
            self.tables[wanted_index] = 'RESERVED'
            return self.tables
    #If not, assign the first empty table you see in the list
        for i_table in range(len(self.tables)):
            if self.tables[i_table] == 'EMPTY':
                self.tables[i_table] = 'RESERVED'
                return self.tables

    #Print the dishes and the portion ordered
    def print_order_details(self):
        print(f'Our customer ordered:\n')
        for dish, portion in self.customer_orders.items():
            print(f'{str(portion)} times {dish}.')

#Complete th transaction, use decimal module for precision issues
    def confirm_payment(self):
        from decimal import Decimal
        total_bill = Decimal('0')

        for dish, price in self.menu_items.items():
            price = Decimal(price)
            portion = Decimal(str(self.customer_orders[dish]))
            total_bill += price * portion
        total_bill = round(total_bill, 2)
    #If the credit is enough, accomplish the transaction
        if total_bill < Decimal(str(self.customer_budget)):
            change = Decimal(str(self.customer_budget - total_bill))
            print(
                f'Payment has been confirmed.\n'
                f'The shopping costed {str(total_bill)}€.\n'
                f'Remaining credit is {str(change)}€.'
            )
    #If not, ask for more credits       
        else:
            print(
                f'Insufficient credits. Please add more credits.\n'
                f'Required balance is {str(total_bill)}€.\n'
                f'Your balance is {str(self.customer_budget)}€.'
            )
