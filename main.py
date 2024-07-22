from src.constants import MENU_ITEMS, TABLES, CUSTOMER_ORDERS, CUSTOMER_BUDGET
from src.restaurant import Restaurant

def main():
    menu_items = MENU_ITEMS
    tables = TABLES
    customer_orders = CUSTOMER_ORDERS
    customer_budget = CUSTOMER_BUDGET

    print("Welcome to my restaurant, Sir\n")
    
    my_restaurant = Restaurant(menu_items, tables, customer_orders, customer_budget)
    my_restaurant.book_table()
    my_restaurant.print_menu()
    my_restaurant.get_order()
    my_restaurant.print_order_details()
    my_restaurant.get_payment()

if __name__ == '__main__':
    main()
