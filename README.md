# Restaurant Management System

## Overview
**Restaurant Management System** is a Python-based application designed to simulate the management of a restaurant. It features functionalities for displaying a menu, taking orders, booking tables, and processing payments. The system also handles basic restaurant operations like updating menu items and checking customer budgets.

## Features
* **Menu Management:** Display and update the restaurant menu.
* **Table Reservation:** Book tables and manage table availability.
* **Order Handling:** Take customer orders and manage customer-specific requests.
* **Payment Processing:** Handle transactions and manage customer budgets.

## Installation
1. **Clone the repository**: 
    ```bash
    git clone https://github.com/yourusername/restaurant_management_system.git
    ```

2. **Navigate to the project directory**:  
    ```bash
    cd restaurant_management_system
    ```

3. **Install any required dependencies (if applicable)**.
    ```bash
    pip install -r requirements.txt
    ```

## Usage  
1. Ensure you have Python 3.x installed.

2. Run the application by executing:
    ```bash
    python main.py
    ```

3. Follow the on-screen prompts to book a table, view the menu, place orders, and process payments.

## Project Structure
* **src/**: Contains source code files.
  * ***\__init__.py***: Initializes the source package and sets up logging.
  * ***constants.py***: Defines constants used throughout the application.
  * ***restaurant.py***: Contains the `Restaurant` class with methods for managing restaurant operations.
  
* **.gitignore**: Specifies files and directories to be ignored by Git (e.g., virtual environments, build artifacts).
* **.gitattributes**: Ensures consistent line endings across different operating systems in the repository.

## Code Example
* **Menu Management**: The `print_menu` method in `Restaurant` displays the current menu.
* **Table Reservation**: The `book_table` method allows for reserving a table.
* **Order Handling**: The `get_order` and `print_order_details` methods handle and display customer orders.
* **Payment Processing**: The `get_payment` method processes the customer's payment.

## Code Example
**main.py**: The entry point of the application. It initializes the restaurant system, handles table booking, menu display, order taking, and payment processing. It provides a complete flow from starting the application to completing a transaction.

```python
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
```

## Contact
Let me know if there are any specific details you’d like to adjust or additional sections you want to include!  
* **Email**: kivancgordu@hotmail.com
* **Version**: 1.0.0
* **Date**: 22-06-2024
