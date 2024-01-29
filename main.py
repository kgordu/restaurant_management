from modules.restaurant import Restaurant

def main():
    my_restaurant = Restaurant(
    menu_items={'Main Dish': 20.99, 'Soup': 12.00, 'Drink': 5.25, 'Dessert' : 7.25},
    tables=['RESERVED', 'EMPTY', 'EMPTY'],
    customer_orders={'Soup': 2, 'Main Dish' : 1, 'Drink' : 2, 'Dessert' : 0},
    customer_budget = 120
    )

    my_restaurant.add_item_to_menu()
    my_restaurant.print_menu()
    my_restaurant.book_table()
    my_restaurant.print_order_details()
    my_restaurant.confirm_payment()

if __name__ == '__main__':
    main()