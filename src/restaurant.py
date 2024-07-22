from decimal import Decimal, ROUND_HALF_UP

class Restaurant:
    def __init__(self, menu_items, tables, customer_orders, customer_budget):
        self.menu_items = menu_items
        self.tables = tables
        self.customer_orders = customer_orders
        self.customer_budget = Decimal(customer_budget)

#Print the dishes in the menu_items with their prices
    def print_menu(self):
        print("The current menu is:\n")
        for dish, price in self.menu_items.items():
            print(f"{dish:<15} {price:.2f}€.")
        print()

#Checks whether order is in menu_items and the decision.
#If not and decision == 'C', add it to the menu_items.
#If yes, increment its portion

#If not in menu_items and decision == 'O'
#Add both to menu_items and customer_orders
    def add_order(self, order, decision):
        try:
            order = order.title()
            if order in self.menu_items.keys() and decision == 'C':
                if order in self.customer_orders:
                    self.customer_orders[order] += 1
                else:
                    self.customer_orders[order] = 1
                print(f"'{order}' is added to the orders.")
            elif order not in self.menu_items or decision == 'O':
                self.menu_items[order] = 15.00
                self.customer_orders[order] = 1
                print(f"'{order}' is added both to the restaurant menu and customer orders.\n")
            else:
                print("Invalid decision. Please follow the instructions properly.\n")
        except Exception as e:
            print(f"An error occurred during the order: {e}\n")

#Ask user for a choice between 'C' and 'O' while is_enough == 'N'
#Use add_order function and every time check the value of is_enough
    def get_order(self):
        is_enough = 'N'
        while is_enough == 'N':
            decision = input(
                "Would you like to order from the menu or something special?\n"
                "Please write me 'C' to choose from the menu or 'O' to order your wish for 15€.\n"
                ).capitalize()
            if decision in ['C', 'O']:
                order = input("Which meal would you like to choose from the menu?\n")
                if not order.strip():
                    print("Empty order. Please specify a dish.\n")
            self.add_order(order, decision)
            enough = input(
                "Would you like anything else?\n"
                "Please write 'Y' for yes or 'N' for no: ").capitalize()
            if enough == 'N':
                is_enough = 'Y'
    
#Reserve a table
    def book_table(self):
        try:
        #Ask the preferred table number
            wanted_table_number = int(input("Which table would you like to have?\n"
                                            "Give me a table number please, Sir: "))
            wanted_index = wanted_table_number - 1      #Given table number == its index + 1, process the index below
        #Check if the table number is valid and empty
            if 0 <= wanted_index < len(self.tables) and self.tables[wanted_index] == 'EMPTY':
                print("Here is your table, Sir. Please make yourself comfortable")
                self.tables[wanted_index] = 'RESERVED'
                return self.tables
        #If not, assign the first closest empty table you see in the list
            else:
                print("Unfortunately, the table is reserved. Please let me guid to the next empty table.\n")
                for i in range(len(self.tables)):
                    if self.tables[i] == 'EMPTY':
                        self.tables[i] = 'RESERVED'
                        break
            print("Sorry, there is no table available at this very moment.")
        except Exception as e:
            print(f"An error occurred during booking the table: {e}\n")

    #Print the dish and the portion ordered
    def print_order_details(self):
        print("Our customer ordered:")
        for dish, portion in self.customer_orders.items():
            print(f"{portion}x {dish}.")
        print()

#Complete the transaction, use decimal module for precision issues
    def get_payment(self):
        try:
            total_bill = Decimal('0')

            for dish, portion in self.customer_orders.items():
                price = Decimal(str(self.menu_items[dish]))
                total_bill += price * portion

            total_bill = total_bill.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        #If the credit is enough, accomplish the transaction
            if total_bill <= self.customer_budget:
                change = self.customer_budget - total_bill
                print(
                    "Payment has been confirmed.\n"
                    f"The order costed: {total_bill}€.\n"
                    f"Remaining credit: {change}€.\n"
                )
        #If not, ask for more credits       
            else:
                print(
                    "Insufficient credits. Please add more credits.\n"
                    f"Required balance: {total_bill}€.\n"
                    f"Your balance:     {self.customer_budget}€.\n"
                )
        except Exception as e:
            print("An error occurred during the payment: {e}\n")
