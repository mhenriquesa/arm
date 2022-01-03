class Produto:
    def __init__(self, name, regularprice, desc, categories, images):
        self.name = name,
        self.regularprice = regularprice,
        self.desc = desc,
        self.categories = categories,
        self.images = images

    def json(self):
        return {
            "name": self.name,
            "regularprice": self.regularprice,
            "desc": self.desc,
            "categories": self.categories,
            "images": self.images
        }
