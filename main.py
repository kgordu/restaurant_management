from src.constants import MENU_ITEMS, TABLES, CUSTOMER_ORDERS, CUSTOMER_BUDGET
from src.restaurant import Restaurant

def main():
    menu_items = MENU_ITEMS
    tables = TABLES
    customer_orders = CUSTOMER_ORDERS
    customer_budget = CUSTOMER_BUDGET

    print("Welcome to my restaurant, Sir\n")
    
    # Initialize the Restaurant object
    my_restaurant = Restaurant(menu_items, tables, customer_orders, customer_budget)
    
    # Display available tables and book a table
    print("Checking table availability...")
    my_restaurant.book_table()
    
    # Display the current menu
    print("Displaying the menu...")
    my_restaurant.print_menu()
    
    # Get orders from the user
    print("Taking customer orders...")
    my_restaurant.get_order()
    
    # Display details of the order
    print("Displaying order details...")
    my_restaurant.print_order_details()
    
    # Process payment
    print("Processing payment...")
    my_restaurant.get_payment()

    # Final message
    print("Thank you for visiting our restaurant. Have a great day!")

if __name__ == '__main__':
    main()
