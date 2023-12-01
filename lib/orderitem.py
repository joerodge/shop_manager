class Order:
    def __init__(self, id, customer_name, order_date, items=[]):
        self.id = id
        self.customer_name = customer_name
        self.order_date = order_date
        self.items = items

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Order({self.id}, {self.customer_name}, {self.order_date}, Items: {len(self.items)})"



class Item:
    def __init__(self, id, item_name, unit_price, quantity):
        self.id = id
        self.item_name = item_name
        self.unit_price = unit_price
        self.quantity = quantity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Item({self.id}, {self.item_name}, {self.unit_price}, {self.quantity})"
    
