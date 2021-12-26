class Clients:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone


class Product:
    def __init__(self, productid, name, desc, sizes, price, estoque):
        self.name = name
        self.desc = desc
        self.sizes = sizes
        self.productid = productid
        self.price = price
        self.estoque = estoque
