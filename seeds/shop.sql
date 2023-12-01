DROP TABLE IF EXISTS orders_items;
DROP TABLE IF EXISTS orders;
DROP TABLE IF EXISTS items;


CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    customer_name text,
    order_date date
);

CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    item_name text,
    unit_price int,
    quantity int
);

-- Create the join table.
CREATE TABLE orders_items (
    order_id int,
    item_id int,
    constraint fk_order foreign key(order_id) references orders(id) on delete cascade,
    constraint fk_item foreign key(item_id) references items(id) on delete cascade,
    PRIMARY KEY (order_id, item_id)
);


INSERT INTO items (item_name, unit_price, quantity) VALUES('Peas', 120, 17);
INSERT INTO items (item_name, unit_price, quantity) VALUES('Rice', 150, 12);
INSERT INTO items (item_name, unit_price, quantity) VALUES('Potatoes', 200, 9);

INSERT INTO orders (customer_name, order_date) VALUES('Joe', '2023-12-01');
INSERT INTO orders (customer_name, order_date) VALUES('Tom', '2023-11-12');
INSERT INTO orders (customer_name, order_date) VALUES('Dick', '2023-10-23');
INSERT INTO orders (customer_name, order_date) VALUES('Harry', '2023-11-24');

INSERT INTO orders_items (order_id, item_id) VALUES(1, 1);
INSERT INTO orders_items (order_id, item_id) VALUES(1, 3);
INSERT INTO orders_items (order_id, item_id) VALUES(2, 1);
INSERT INTO orders_items (order_id, item_id) VALUES(2, 2);
INSERT INTO orders_items (order_id, item_id) VALUES(2, 3);
INSERT INTO orders_items (order_id, item_id) VALUES(3, 2);