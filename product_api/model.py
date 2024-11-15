class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - {self.price:.2f} ({self.description})"
#This class represents a product with its name, description, and price.



