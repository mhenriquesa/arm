from webhookserver import db


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.phone}')"


class Products(db.Model):
    id = db.Column(db.String(10), unique=True, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    desc = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    estoque = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.price}')"


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    clientid = db.Column(db.Integer, db.ForeignKey(
        'client.id'), nullable=False)

    productid = db.Column(db.String(10), db.ForeignKey(
        'products.id'), nullable=False)

    quantity = db.Column(db.Integer,  nullable=False)

    def __repr__(self):
        return f"User('{self.id}', '{self.name}', '{self.price}')"
