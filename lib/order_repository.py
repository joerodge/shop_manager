from lib.orderitem import Order, Item

class OrderRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM orders ORDER BY id")
        orders =[]
        for row in rows:
            order = Order(row['id'], row['customer_name'], str(row['order_date']))
            orders.append(order)
        return orders


    def create(self, customer_name, order_date, items):
        self._connection.execute(
            "INSERT INTO orders (customer_name, order_date) " \
            "VALUES(%s, %s)", [customer_name, order_date]
        )
        rows = self._connection.execute(
            "SELECT id FROM orders WHERE customer_name = %s", [customer_name])
        
        order_id = rows[0]['id']
        for item_id in items:
            self._connection.execute(
                "INSERT INTO orders_items (order_id, item_id) VALUES (%s, %s)", 
                [order_id, item_id]
            )


    def get_order_items(self, id):
        rows = self._connection.execute(
            "SELECT items.id, items.item_name, items.unit_price, items.quantity " \
            "FROM orders " \
            "JOIN orders_items on orders_items.order_id = orders.id " \
            "JOIN items on orders_items.item_id = items.id " \
            "WHERE orders.id = %s", [id]
        )
        items = []
        for row in rows:
            item = Item(row['id'], row['item_name'], row['unit_price'], row['quantity'])
            items.append(item)
        return items

