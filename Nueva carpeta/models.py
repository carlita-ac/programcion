class Product:
    """
    Modelo de datos para un producto en MotoShop.
    Representa motos, accesorios y repuestos.
    """

    def __init__(self, id, name, category, price, stock, description=""):
        self.id = id
        self.name = name
        self.category = category  # moto, repuesto, accesorio
        self.price = price
        self.stock = stock
        self.description = description

    @classmethod
    def from_tuple(cls, tup):
        """Crea un Product desde una tupla de la base de datos"""
        return cls(
            id=tup[0],
            name=tup[1],
            category=tup[2],
            price=tup[3],
            stock=tup[4],
            description=tup[5]
        )

    def to_tuple(self):
        """Convierte el producto en una tupla para insertar o actualizar en DB"""
        return (self.name, self.category, self.price, self.stock, self.description)

    def __repr__(self):
        return f"Product(id={self.id}, name='{self.name}', category='{self.category}', price={self.price}, stock={self.stock})"