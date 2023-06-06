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
        does_item_exist = self.read_one_inventory(item.name)
        if does_item_exist is None:
            with self.conn:
                self.c.execute("INSERT INTO items VALUES (:name, :amount, :price)", {
                    'name': item.name, 'amount': item.amount, 'price': item.price})
        else:
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nItem already exists\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nAdding to existing item\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            self.update_inventory_item(item)
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nItem updated\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            print(
                '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nItem now looks like this\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            self.read_one_inventory(item.name)
        """This function first checks to see if an inventory item exists in the database,
        if it does then it adds the number to the existing item count, 
        otherwise it will create a new item in the database"""

        pass

    def create_many_items(self, items):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nCreate {} Items\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(
            len(items)))
        for item in items:
            self.create_inventory_item(item)

        """Similar to the create one item,
        this first checks to see if an item exists in the inventory and either adds to the existing list or continues creating
            if they already exist"""

    def read_all_inventory(self):
        with self.conn:
            self.c.execute("SELECT * FROM items")
            items = self.c.fetchall()

            if len(items) == 0:
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n No items in inventory\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            else:
                for item in items:
                    print(
                        f"Item Name: {item[0]}\nAmount In Inventory: {item[1]}\nPrice Per Kg: {item[2]}")
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Reading Inventory\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
        """This will print out a formatted string of all items in the inventory menu"""

    def read_one_inventory(self, name):
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Searching for {} Item\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(
            name))
        with self.conn:
            self.c.execute(
                "SELECT * FROM items WHERE name = :name", {'name': name})
            item = self.c.fetchone()
            if item is None:
                print(
                    "~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Item does not exist\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
                return None
            else:
                print(
                    f"Item Name: {item[0]}\nAmount In Inventory: {item[1]}\nPrice Per Kg: {item[2]}")
                return item

        """This will get a specific thing from the menu
        and print a formatted string of the number of items currently in the menu or null if it doesn't exist"""
        pass

    def update_item(self, item_name, target, value):
        """This code will search the database for an item that exists,
        if it doesn't exist then it return None
        and if it does exist then it will update the passed key with the passed value """
        with self.conn:
            self.c.execute("SELECT * FROM items WHERE :name",
                           {'name': item_name})
            item = self.c.fetchone()
            if item is None:
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Item does not exist\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                return None
            else:
                self.c.execute("UPDATE items SET :target = :target +  :value WHERE :name", {
                    'target': target, 'value': value, 'name': item_name})
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Item updated\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Item now looks like this\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
                self.read_one_inventory(item_name)

    def delete_item(self, key):
        """This will take in a key of an item in the menu and delete the item if 
        it exists or send an alert of I cannot delete what does not exist"""
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Delete {}\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n'.format(key))
        with self.conn:
            self.c.execute("DELETE FROM items WHERE :name", {'name': key})
            item = self.c.fetchone()
            if item is None:
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Item does not exist\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
            else:
                self.c.execute("DELETE FROM items WHERE :name", {'name': key})
                print(
                    '~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n Item deleted\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
