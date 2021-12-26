import sqlite3
from armbot_classes_Clients import Clients
from armbot_classes_Product import Product

conn = sqlite3.connect('armbot_db.db')

c = conn.cursor()

conn.execute('PRAGMA foreign_keys = ON')


def insert_client(client):
    with conn:
        c.execute('INSERT INTO clients VALUES (:id, :name, :phone, :email)',
                  {'id': None, 'name': client.name, 'email': client.email, 'phone': client.phone})


def insert_product(product):
    with conn:
        c.execute('INSERT INTO products VALUES (:productid, :name, :desc, :sizes , :price, :estoque)',
                  {'productid': product.productid, 'name': product.name, 'desc': product.desc, 'sizes': product.sizes, 'price': product.price, 'estoque': product.estoque})


def insert_to_cart(userid, productid, quantity):
    with conn:
        cart = get_cart(userid)
        for item in cart:
            if item[1] == productid:
                c.execute(f'UPDATE carrinho SET quantity = quantity + {quantity} WHERE userid=:userid AND productid=:productid',
                          {'userid': userid, 'productid': productid})
                return
        c.execute('INSERT INTO carrinho VALUES (:userid, :productid, :quantity)', {
                  'userid': userid, 'productid': productid, 'quantity': quantity})


def remove_from_cart(userid, productid):
    with conn:
        cart = get_cart(userid)
        for item in cart:
            if item[1] == productid and item[2] == 1:
                c.execute('DELETE FROM carrinho WHERE userid = :userid AND productid = :productid', {
                          'userid': userid, 'productid': productid})
                return
            if item[1] == productid:
                c.execute(f'UPDATE carrinho SET quantity = quantity - 1 WHERE userid=:userid AND productid=:productid',
                          {'userid': userid, 'productid': productid})
                return


def get_cart(userid):
    with conn:
        c.execute('''SELECT carrinho.userid, carrinho.productid, carrinho.quantity , products.name, products.price
                    FROM carrinho
                    INNER JOIN products ON carrinho.productid = products.productid WHERE userid=:userid''',
                  {'userid': userid})

        return c.fetchall()


def remove_client_by_phone(client):
    with conn:
        c.execute('DELETE FROM clients WHERE phone=:phone', {
                  'phone': client.phone})


def remove_product_by_id(product):
    with conn:
        c.execute('DELETE FROM products WHERE productid=:productid', {
                  'productid': product.productid})


def remove_client_by_email(client):
    with conn:
        c.execute('DELETE FROM clients WHERE email=:email', {
                  'email': client.email})


def get_client_by_email(client):
    c.execute('SELECT * FROM clients WHERE email=:email',
              {'email': client.email})
    return c.fetchall()


def get_client_by_phone(client):
    c.execute('SELECT * FROM clients WHERE phone=:phone',
              {'phone': client.phone})
    return c.fetchall()


def get_product_by_id(productid):
    c.execute('SELECT * FROM products WHERE productid=:productid',
              {'productid': productid})
    print(c.fetchall())
    return c.fetchall()


# client1 = Clients('Filho', 'wwwww', 5656)
# prod1 = Product('c15', 'Calça Pantalona Jeans',
#                 'Calça jeans da moda', '38 40 42 44', 139, True)
# insert_product(prod1)
# insert_client(client1)
# insert_to_cart(2, 'c15')
# insert_to_cart(2, 'c15')
# insert_to_cart(2, 'c10')
# insert_to_cart(2, 'c10')
# insert_to_cart(4, 'c10')
# insert_to_cart(2, 'c15', 1)
# remove_from_cart(4, 'c10')
print(get_cart(2))
conn.close()
