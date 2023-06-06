from db import Database


class InventoryItem:
    """Class for all inventory items"""

    def __init__(self, name, amount, price):
        self.name = name
        self.amount = int(amount)
        self.price = int(price)

    @property
    def listing(self):
        return "Item Name:{}\nAmount In Inventory: {}\nPrice Per Kg:{}".format(self.name, self.amount, self.price)

    def to_dict(self):
        return {
            'name': self.name,
            'amount': self.amount,
            'price': self.price
        }


class Inventory:
    """"Class To Manage Inventory System"""

    def __init__(self):
        self.database = Database()

    def add_item_to_inventory(self):
        item_name = input(
            'What is the name of the item you are trying to add to the inventory? ')
        item_amount = input(
            'How many of this item are you adding to the inventory? ')
        item_price = input('What is the price per kg of this item? ')
        new_item = InventoryItem(item_name, item_amount, item_price)
        item_exists = self.database.read_one_inventory(new_item.name)
        if item_exists is None:
            print('Creating new item')
            self.database.create_inventory_item(new_item)
        else:
            print('Item already exists')
            print('Adding to existing item. Here is the item name {}'.format(
                new_item.name))
            print('~~~~~~~~~~~~~~~Updating Amount~~~~~~~~~~~~~~~~~~~~')
            self.database.update_item(new_item.name, 'amount', new_item.amount)
            self.database.update_item(new_item.name, 'price', new_item.price)
            print('Item updated')
            print('Item now looks like this')
            self.database.read_one_inventory(new_item.name)

    def add_multiple_items_to_inventory(self):
        items = []
        item_amount = input('How many items are you adding to the inventory? ')
        for item in range(int(item_amount)):
            item_name = input(
                'What is the name of the item you are trying to add to the inventory? ')
            item_amount = input(
                'How many of this item are you adding to the inventory? ')
            item_price = input('What is the price per kg of this item? ')
            items.append(InventoryItem(item_name, item_amount, item_price))
        self.database.create_many_items(items)

    def update_item_in_inventory(self):
        item_name = input(
            'What is the name of the item you are trying to update? ')
        item_amount = input(
            'How many of this item are you adding to the inventory? ')
        item_price = input('What is the price per kg of this item? ')
        item = InventoryItem(item_name, item_amount, item_price)
        self.database.update_item(item.name, 'amount', item.amount)
        self.database.update_item(item.name, 'price', item.price)

    def delete_item_from_inventory(self):
        item_name = input(
            'What is the name of the item you are trying to delete? ')
        self.database.delete_item(item_name)

    def read_all_inventory(self):
        self.database.read_all_inventory()

    def read_one_inventory(self):
        item_name = input(
            'What is the name of the item you are trying to read? ')
        item = self.database.read_one_inventory(item_name)
        if item is None:
            print('Item does not exist')
