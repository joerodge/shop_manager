from lib.orderitem import Item
from lib.item_repository import ItemRepository

def test_all_returns_list_of_all_items(db_connection):
    db_connection.seed('seeds/shop.sql')
    item_repo = ItemRepository(db_connection)
    assert item_repo.all() == [
        Item(1, 'Peas', 120, 17),
        Item(2, 'Rice', 150, 12),
        Item(3, 'Potatoes', 200, 9),
    ]

def test_adding_an_item(db_connection):
    db_connection.seed('seeds/shop.sql')
    item_repo = ItemRepository(db_connection)
    item_repo.create('Beef', 350, 8)
    assert item_repo.all() == [
        Item(1, 'Peas', 120, 17),
        Item(2, 'Rice', 150, 12),
        Item(3, 'Potatoes', 200, 9),
        Item(4, 'Beef', 350, 8),
    ]

def test_get_by_id(db_connection):
    db_connection.seed('seeds/shop.sql')
    item_repo = ItemRepository(db_connection)
    assert item_repo.get_item_by_id(2) == Item(2, 'Rice', 150, 12)

def test_decrement(db_connection):
    db_connection.seed('seeds/shop.sql')
    item_repo = ItemRepository(db_connection)
    assert item_repo.get_item_by_id(2) == Item(2, 'Rice', 150, 12)
    item_repo.degrement_item(2)
    assert item_repo.get_item_by_id(2) == Item(2, 'Rice', 150, 11)