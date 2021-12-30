import sqlite3
from webhookserver.models import Client


conn = sqlite3.connect('armbot_db.db')

c = conn.cursor()

conn.execute('PRAGMA foreign_keys = ON')


def insert_client_to_db(user_data):
    user_found = get_client_by_phone(user_data.phone)
    if user_found:
        print('Cliente ja cadastrado')
        return "Cliente ja cadastrado!"
    else:
        with conn:
            c.execute('INSERT INTO clients VALUES (:id, :name, :phone, :email)',
                      {'id': None, 'name': user_data.name, 'email': user_data.email, 'phone': user_data.phone})
            print('cliente cadastrado')


def remove_client_by_phone(client_phone):
    with conn:
        user_found = get_client_by_phone(client_phone)
        if user_found:
            userid = user_found[0][0]

            clean_cart(userid)
            c.execute('DELETE FROM clients WHERE phone=:phone', {
                'phone': client_phone})
            print('cliente removido')

            return
        else:
            print('cliente nao encontrado')


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


def insert_product_to_db(product):
    with conn:
        c.execute('INSERT INTO products VALUES (:productid, :name, :desc, :sizes , :price, :estoque)',
                  {'productid': product.productid, 'name': product.name, 'desc': product.desc, 'sizes': product.sizes, 'price': product.price, 'estoque': product.estoque})


def insert_product_to_cart(userid, productid, quantity):
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


def clean_cart(userid):
    has_product = get_cart(userid)
    if has_product:
        with conn:
            c.execute('DELETE FROM carrinho WHERE userid = :userid',
                      {'userid': userid})
            print('carrinho acabou de ser limpo')
            return
    else:
        print('carrinho limpo')


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
    print(dir(Client.query.filter_by(phone=client_phone).all()[0]))
    # print(Client.query.all())


def get_product_by_id(productid):
    c.execute('SELECT * FROM products WHERE productid=:productid',
              {'productid': productid})
    print(c.fetchall())
    return c.fetchall()


conn.close()
