class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Error: Item ID already exists.")
            return
        if price < 0:
            print("Error: Price cannot be negative.")
            return
        self.items[item_id] = Item(item_id, name, description, price)
        print("Item added successfully.")

    def read_item(self, item_id):
        item = self.items.get(item_id)
        if item:
            print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")
        else:
            print("Error: Item not found.")

    def update_item(self, item_id, name=None, description=None, price=None):
        item = self.items.get(item_id)
        if not item:
            print("Error: Item not found.")
            return
        if price is not None and price < 0:
            print("Error: Price cannot be negative.")
            return
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            item.price = price
        print("Item updated successfully.")

    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully.")
        else:
            print("Error: Item not found.")

    def list_items(self):
        if not self.items:
            print("No items available.")
            return
        for item in self.items.values():
            print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: {item.price}")


def menu():
    manager = ItemManager()
    while True:
        print("\nItem Management System")
        print("1. Add Item")
        print("2. View Item")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. List All Items")
        print("6. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                item_id = input("Enter item ID: ")
                name = input("Enter item name: ")
                description = input("Enter item description: ")
                price = float(input("Enter item price: "))
                manager.create_item(item_id, name, description, price)
            except ValueError:
                print("Error: Invalid input for price.")
        elif choice == '2':
            item_id = input("Enter item ID: ")
            manager.read_item(item_id)
        elif choice == '3':
            item_id = input("Enter item ID: ")
            name = input("Enter new name (or leave blank): ") or None
            description = input("Enter new description (or leave blank): ") or None
            try:
                price_input = input("Enter new price (or leave blank): ")
                price = float(price_input) if price_input else None
            except ValueError:
                print("Error: Invalid input for price.")
                continue
            manager.update_item(item_id, name, description, price)
        elif choice == '4':
            item_id = input("Enter item ID: ")
            manager.delete_item(item_id)
        elif choice == '5':
            manager.list_items()
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

menu()
