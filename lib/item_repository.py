from lib.orderitem import Item

class ItemRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM items ORDER BY id")
        items = []
        for row in rows:
            item = Item(row['id'], row['item_name'], row['unit_price'], row['quantity'])
            items.append(item)
        return items
    
    def create(self, item_name, unit_price, quantity):
        self._connection.execute(
            "INSERT INTO items (item_name, unit_price, quantity) " \
                "VALUES (%s, %s, %s)", [item_name, unit_price, quantity]
        )

    def get_item_by_id(self, id):
        rows = self._connection.execute(
            "SELECT * FROM items WHERE id = %s", [id]
        )
        row = rows[0]
        return Item(row['id'], row['item_name'], row['unit_price'], row['quantity'])
    
    def degrement_item(self, item_id):
        # UPDATE table SET column = new_value WHERE conditions
        new_quantity = self.get_item_by_id(item_id).quantity - 1
        if new_quantity < 0:
            return False
        self._connection.execute(
            "UPDATE items SET quantity = %s WHERE id = %s", [new_quantity, item_id]
        )
        return True