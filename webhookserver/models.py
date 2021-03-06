from webhookserver import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    cep = db.Column(db.String(8))
    logradouro = db.Column(db.Text)
    numero = db.Column(db.String(7))
    complemento = db.Column(db.Text)
    bairro = db.Column(db.String(20))
    cidade = db.Column(db.String(20))
    estado = db.Column(db.String(20))

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self. phone = phone

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.phone}')"

    def json(self):
        return {
            "name": self.name,
            "email": self.email,
            "phone": self.phone
        }

    @classmethod
    def find_by_phone(cls, phone):
        return cls.query.filter_by(phone=phone).all()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).all()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Products(db.Model):
    id = db.Column(db.String(10), unique=True, primary_key=True)
    cat = db.Column(db.String(15), nullable=False)
    subcat = db.Column(db.String(15), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    tamanhos = db.Column(db.String(8), nullable=False)
    photo = db.Column(db.Text, nullable=False)
    link = db.Column(db.Text, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def __init__(self, id, cat, subcat, desc, price, tamanhos, photo, link, estoque):
        self.id = id
        self.cat = cat
        self.subcat = subcat
        self.desc = desc
        self.price = price
        self.tamanhos = tamanhos
        self.photo = photo
        self.link = link
        self.estoque = estoque

    def __repr__(self):
        return f"Product('{self.id}', '{self.cat}','{self.subcat}', '{self.price}')"

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).all()

    @classmethod
    def get_categorie(cls, categorie):
        prods = cls.query.filter_by(cat=categorie).all()
        prodstr = ''

        for product in prods:
            prodstr += f"""
                C??d do produto: {product.id}
                C??d do produto: {product.cat + ' ' + product.subcat}
                Descri????o: {product.tamanhos}
                Pre??o: {product.price}
                Tamanho: {product.tamanhos}
                Fotos aqui -> : {product.link}
                ========================
                    """
        return {
            "fulfillmentText": f"{prodstr}",
            "source": 'webhook'
        }

        return

    def create_prod(self):
        db.session.add(self)
        db.session.commit()


class Cart(db.Model):
    Rowid = db.Column(db.Integer, primary_key=True)
    clientid = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)
    productid = db.Column(db.String(10), db.ForeignKey(
        'products.id'), nullable=False)
    quantity = db.Column(db.Integer,  nullable=False)

    def __init__(self, clientid, productid, quantity):
        self.clientid = clientid
        self.productid = productid
        self. quantity = quantity

    def __repr__(self):
        return f"Cart('{self.clientid}', '{self.productid}', '{self.quantity}')"

    @classmethod
    def find(cls, clientid, productid):
        result = cls.query.filter_by(
            clientid=clientid, productid=productid).all()
        print(result)
        return result

    @classmethod
    def get_cart(cls, clientid):
        result = db.session.query(Cart, Products).join(
            Products).filter(Cart.clientid == clientid).all()
        cartstr = ""
        for cart, product in result:
            cartstr += f"""
                Produto: {product.name}
                Codigo do produto: {product.id}
                Quantidade: {cart.quantity}
                Pre??o: {product.price}
                Tamanho: {product.tamanho}
                Cor: {product.cor}
                ========================
                    """
        return {
            "fulfillmentText": f"{cartstr}",
            "source": 'webhook'
        }

    @classmethod
    def remove(cls, clientid, productid, quantity):
        product_in_cart = cls.find(clientid, productid)

        if product_in_cart:
            if product_in_cart[0].quantity - quantity <= 0:
                db.session.delete(product_in_cart[0])
                db.session.commit()
                return

            product_in_cart[0].quantity -= quantity
            db.session.commit()
            return
        print("there is no such product in cart")

    @classmethod
    def add(cls, clientid, productid, quantity):
        product_exists = Products.find_by_id(productid)
        if not product_exists:
            print("Esse produto nao existe em nossa loja")
            return

        product_in_cart = cls.find(clientid, productid)

        if product_in_cart:
            product_in_cart[0].quantity += quantity
            db.session.commit()
            return

        products_to_add = Cart(clientid, productid, quantity)
        db.session.add(products_to_add)
        db.session.commit()

    def json(self):
        return {
            "clientid": self.clientid,
            "productid": self.productid,
            "quantity": self.quantity
        }
