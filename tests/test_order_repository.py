from lib.orderitem import Order, Item
from lib.order_repository import OrderRepository

def test_all_returns_list_of_all_items(db_connection):
    db_connection.seed('seeds/shop.sql')
    order_repo = OrderRepository(db_connection)
    assert order_repo.all() == [
        Order(1, 'Joe', '2023-12-01'),
        Order(2, 'Tom', '2023-11-12'),
        Order(3, 'Dick', '2023-10-23'),
        Order(4, 'Harry', '2023-11-24'),
    ]

def test_get_order_items(db_connection):
    db_connection.seed('seeds/shop.sql')
    order_repo = OrderRepository(db_connection)
    assert order_repo.get_order_items(1) == [
        Item(1, 'Peas', 120, 17),
        Item(3, 'Potatoes', 200, 9),
    ]

def test_create_new_order_adds_it_to_db(db_connection):
    db_connection.seed('seeds/shop.sql')
    order_repo = OrderRepository(db_connection)
    order_repo.create('Jane', '2023-11-29',[1, 2])
    assert len(order_repo.all()) == 5
    assert order_repo.get_order_items(5) == [
        Item(1, 'Peas', 120, 17),
        Item(2, 'Rice', 150, 12),
    ]


    