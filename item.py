class InventoryItem:
    """Class for all inventory items"""

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price

    @property
    def listing(self):
        return "Item Name:{}\nAmount In Inventory: {}\nPrice Per Kg:{}".format(self.name, self.amount, self.price)

    def to_dict(self):
        return {
            'name': self.name,
            'amount': self.amount,
            'price': self.price
        }
