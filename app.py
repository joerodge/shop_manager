from lib.database_connection import DatabaseConnection
from lib.item_repository import ItemRepository
from lib.order_repository import OrderRepository
from sys import exit

INTRO_MESSAGE = '''
What do you want to do?
    1 = list all shop items
    2 = create a new item
    3 = list all orders
    4 = create a new order
    q = quit
'''

class Application:
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/shop.sql")
        self.item_repo = ItemRepository(self.connection)
        self.order_repo = OrderRepository(self.connection)

    def print_all_items(self):
        items = self.item_repo.all()
        for item in items:
            print(f"  #{item.id} {item.item_name} - Price: £{item.unit_price/100:.2f} - Quantity: {item.quantity}")

    def print_all_orders(self):
        orders = self.order_repo.all()
        for order in orders:
            print(f"  #{order.id} Customer name: {order.customer_name} - Date: {order.order_date} - Items: ")
            self.print_order_items(order)

    def print_order_items(self, order):
        order_items = self.order_repo.get_order_items(order.id)
        for item in order_items:
            print(f"    {item.item_name} - Price: £{item.unit_price/100:.2f}")

    def create_new_item(self):
        name = input("Please enter new item name: ")
        price = input("Please enter new item price in pence: ")
        quantity = input("Please enter new item quantity: ")
        self.item_repo.create(name, price, quantity)

    def create_new_order(self):
        name = input("Please enter customer name: ")
        date = input("Please enter order date (format YYYY-MM-DD): ")
        item_count = int(input("Please enter number of items: "))
        item_ids = []
        for i in range(item_count):
            item_id = int(input(f"Enter item id of item #{i+1} : "))
            if self.item_repo.degrement_item(item_id):
                item_ids.append(item_id)
            else:
                print(f'The item with id {item_id} is out of stock '
                    'so it was not added to the order')
            
        self.order_repo.create(name, date, item_ids)


    def run(self):
        print(INTRO_MESSAGE)
        choice = input('> ').strip()
        if choice == '1':
            self.print_all_items()
        elif choice == '2':
            self.create_new_item()
        elif choice == '3':
            self.print_all_orders()
        elif choice == '4':
            self.create_new_order()
        elif choice == 'q':
            exit(0)
        else:
            print('\nInvalid choice')


if __name__ == '__main__':
    app = Application()
    print('Welcome to the shop management program!')
    while True:
        app.run()