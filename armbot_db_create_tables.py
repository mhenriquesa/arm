import sqlite3

conn = sqlite3.connect('armbot_db.db')
c = conn.cursor()

c.execute(''' CREATE TABLE IF NOT EXISTS clients
              (id integer primary key,
              name text not null,
              phone char(20) not null,
              email char(50) not null)''')

c.execute(''' CREATE TABLE IF NOT EXISTS products
              (productid char(10) primary key,
              name text not null,
              desc text not null,
              sizes char(5) not null)''')

c.execute(''' CREATE TABLE IF NOT EXISTS carrinho
              (userid integer not null,
              productid char(10) not null,
              FOREIGN KEY(userid) REFERENCES clients(id),
              FOREIGN KEY(productid) REFERENCES products(productid))''')

conn.close()
