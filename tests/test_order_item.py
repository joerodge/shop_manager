from lib.orderitem import Order, Item

def test_order_creation():
    order = Order(1, 'Joe', '2023-12-01')
    assert order.id == 1
    assert order.customer_name == 'Joe'
    assert order.order_date == '2023-12-01'
    assert order.items == []

def test_order_equal():
    order = Order(1, 'Joe', '2023-12-01')
    order2 = Order(1, 'Joe', '2023-12-01')
    assert order == order2

def test_order_repr():
    order = Order(1, 'Joe', '2023-12-01')
    assert str(order) == 'Order(1, Joe, 2023-12-01, Items: 0)'


def test_item_creation():
    item = Item(1, 'Peas', 120, 17)
    assert item.id == 1
    assert item.item_name == 'Peas'
    assert item.unit_price == 120
    assert item.quantity == 17

def test_item_equal():
    item = Item(1, 'Peas', 120, 17)
    item2 = Item(1, 'Peas', 120, 17)
    assert item == item2

def test_item_repr():
    item = Item(1, 'Peas', 120, 17)
    assert str(item) == 'Item(1, Peas, 120, 17)'