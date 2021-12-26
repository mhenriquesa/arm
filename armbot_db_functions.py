import sqlite3
from armbot_classes_Clients import Clients
from armbot_classes_Product import Product

conn = sqlite3.connect('armbot_db.db')

c = conn.cursor()

conn.execute('PRAGMA foreign_keys = ON')


def insert_client_to_db(user_data):
    with conn:
        user_found = get_client_by_email(user_data.email)
        if user_found:
            print('Cliente ja cadastrado')
            return "Cliente ja cadastrado!"
        else:
            c.execute('INSERT INTO clients VALUES (:id, :name, :phone, :email)',
                      {'id': None, 'name': user_data.name, 'email': user_data.email, 'phone': user_data.phone})


def remove_client_by_phone(client):
    with conn:
        c.execute('DELETE FROM clients WHERE phone=:phone', {
                  'phone': client.phone})


def remove_client_by_email(client_email):
    with conn:
        user_found = get_client_by_email(client_email)
        if user_found:
            c.execute('DELETE FROM clients WHERE email=:email', {
                'email': client_email})
            print('Usuario removido')
            return
        else:
            print('Usuario nao encontrado')
            return 'Not found'


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


def remove_from_cart(userid, productid, quantity):
    with conn:
        cart = get_cart(userid)
        for item in cart:
            if item[1] == productid and item[2] - quantity == 0:
                c.execute('DELETE FROM carrinho WHERE userid = :userid AND productid = :productid', {
                          'userid': userid, 'productid': productid})
                return
            if item[1] == productid:
                c.execute(f'UPDATE carrinho SET quantity = quantity - {quantity} WHERE userid=:userid AND productid=:productid',
                          {'userid': userid, 'productid': productid})
                return


def get_cart(userid):
    with conn:
        c.execute('''SELECT carrinho.userid, carrinho.productid, carrinho.quantity , products.name, products.price
                    FROM carrinho
                    INNER JOIN products ON carrinho.productid = products.productid WHERE userid=:userid''',
                  {'userid': userid})

        return c.fetchall()


def remove_product_by_id(product):
    with conn:
        c.execute('DELETE FROM products WHERE productid=:productid', {
                  'productid': product.productid})


def get_client_by_email(client_email):
    c.execute('SELECT * FROM clients WHERE email=:email',
              {'email': client_email})
    return c.fetchall()


def get_client_by_phone(client_phone):
    c.execute('SELECT * FROM clients WHERE phone=:phone',
              {'phone': client_phone.phone})
    return c.fetchall()


def get_product_by_id(productid):
    c.execute('SELECT * FROM products WHERE productid=:productid',
              {'productid': productid})
    print(c.fetchall())
    return c.fetchall()


client1 = Clients('Ana Ramos', 'www', 11999999)
# prod1 = Product('c15', 'Calça Pantalona Jeans',
#                 'Calça jeans da moda', '38 40 42 44', 139, True)
# insert_product(prod1)
# insert_to_cart(2, 'c15')
# insert_to_cart(2, 'c15')
# insert_to_cart(2, 'c10')
# insert_to_cart(2, 'c10')
# insert_to_cart(4, 'c10')
# insert_to_cart(2, 'c15', 3)
# remove_from_cart(2, 'c15', 6)
# insert_client_to_db(client1)
remove_client_by_email('www')
# get_client_by_email('bbbb')
# print(get_cart(2))
conn.close()
