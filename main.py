from db import Database
from item import InventoryItem

inventory = Database()

choice = input('What would you like to do?\n1. Read All Existing Inventory\n2. Read a specific item\n3. Create A New Item\n4. Create Multiple Items\n5. Update an Item\n6. Delete an item\n7. Quit\nType your choice: ')

test_item = InventoryItem('test name', 500, 5)
inventory.create_inventory_item(test_item)
inventory.create_many_items([test_item])
inventory.read_one_inventory(test_item.name)
inventory.delete_item('Delete Key')
inventory.update_item(test_item.name, 'amount', 5000)
inventory.read_all_inventory()
print(choice)
