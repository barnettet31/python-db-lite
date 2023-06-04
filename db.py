import sqlite3


class Database:
    """The following is for the purposes of creating inventory, 
reading inventory, updating inventory,
 and deleting inventory"""

    def __init__(self):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nChecking for existing database....\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
        try:
            self.conn = sqlite3.connect(
                "file:./database/inventory.db?mode=rw", uri=True)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nDatabase found using exisiting....\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            self.c = self.conn.cursor()

        except sqlite3.OperationalError:
            print(
                "~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nNo database found, creating one.\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            self.conn = sqlite3.connect('./database/inventory.db')
            self.c = self.conn.cursor()
            self.c.execute("""CREATE TABLE items (
        name text,
        amount text,
        price integer
        )""")

    def create_inventory_item(self, item):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nCreate {} Item\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(
            item.name))
        """This function first checks to see if an inventory item exists in the database,
        if it does then it adds the number to the existing item count, 
        otherwise it will create a new item in the database"""

        pass

    def create_many_items(self, items):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nCreate {} Items\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(
            len(items)))

        """Similar to the create one item,
        this first checks to see if an item exists in the inventory and either adds to the existing list or continues creating
            if they already exist"""
        pass

    def read_all_inventory(self):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Reading Inventory\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')

        """This will print out a formatted string of all items in the inventory menu"""
        pass

    def read_one_inventory(self, name):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Read {} Item\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(
            name))

        """This will get a specific thing from the menu
        and print a formatted string of the number of items currently in the menu"""
        pass

    def update_item(self, item_name, target, value):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Updated this property {} on this Item {} with this value {}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(
            target, item_name, value))

        """This code will search the database for an item that exists,
        if it doesn't exist then it will create the item 
        and if it does exist then it will update the passed key with the passed value """
        pass

    def delete_item(self, key):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Delete {}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(key))

        """This will take in a key of an item in the menu and delete the item if 
        it exists or send an alert of I cannot delete what does not exist"""
        pass
