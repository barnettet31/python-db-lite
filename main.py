from item import Inventory
inventory = Inventory()

choice = input('What would you like to do?\n1. Read All Existing Inventory\n2. Read a specific item\n3. Create A New Item\n4. Create Multiple Items\n5. Update an Item\n6. Delete an item\n7. Quit\nType your choice: ')
options = {
    1: inventory.read_all_inventory,
    2: inventory.read_one_inventory,
    3: inventory.add_item_to_inventory,
    4: inventory.add_multiple_items_to_inventory,
    5: inventory.update_item_in_inventory,
    6: inventory.delete_item_from_inventory,

}
while int(choice) != 7:
    option = options.get(int(choice))
    if option is not None:
        option()
    choice = input('What would you like to do?\n1. Read All Existing Inventory\n2. Read a specific item\n3. Create A New Item\n4. Create Multiple Items\n5. Update an Item\n6. Delete an item\n7. Quit\nType your choice: ')

print('Thank you for using the inventory system')
