class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price
    
    def __str__(self):
        return f"{self.item_id:<6} | {self.name:<25} | {self.description:<30} | PHP {self.price:>6.2f}"

class ItemManagement:
    def __init__(self):
        self.items = {}
        self.load_items()
    
    def add_item(self, item_id, name, description, price):
        if item_id in self.items:
            print("Item ID already exists.")
            return
        
        try:
            if len(item_id) != 6 or not item_id.isdigit():
                raise ValueError("Item ID must be a 6-digit number.")
            if not name.strip():
                raise ValueError("Item name cannot be empty.")
            if not description.strip():
                raise ValueError("Description cannot be empty.")
            price = float(price)
            if price <= 0:
                raise ValueError("Price must be a positive number.")
            self.items[item_id] = Item(item_id, name, description, price)
            self.save_items()
            print("Item added successfully!")
        except ValueError as e:
            print("Error:", e)
    
    def view_items(self):
        if not self.items:
            print("No items available.")
            return
        print("-" * 100)
        print(f"{'ID':<6}   {'Name':<25}   {'Description':<30}   {'Price'}")
        print("-" * 100)
        for item in self.items.values():
            print(item)
        print("-" * 100)
    
    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Item ID not found.")
            return
        
        if name:
            self.items[item_id].name = name
        if description:
            self.items[item_id].description = description
        if price:
            try:
                price = float(price)
                if price <= 0:
                    raise ValueError("Price must be a positive number.")
                self.items[item_id].price = price
            except ValueError as e:
                print("Error:", e)
                return
        
        self.save_items()
        print("Item updated successfully!")
    
    def delete_item(self, item_id):
        if item_id not in self.items:
            print("Item ID not found.")
            return
        del self.items[item_id]
        self.save_items()
        print("Item deleted!")
    
    def save_items(self):
        with open("item.txt", "w") as file:
            for item in self.items.values():
                file.write(f"{item.item_id},{item.name},{item.description},{item.price}\n")
    
    def load_items(self):
        try:
            with open("item.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(",")
                    if len(parts) < 4:
                        print(f"Skipping invalid entry: {line.strip()}")
                        continue
                    item_id, name, description, price = parts[0], parts[1], ",".join(parts[2:-1]), parts[-1]
                    self.items[item_id] = Item(item_id, name, description, float(price))
        except FileNotFoundError:
            pass

def main():
    manager = ItemManagement()
    while True:
        print("-" * 40)
        print("\tBook Management System")
        print("-" * 40)
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")
        print("-" * 40)
        choice = input("Enter your choice: ")

        if choice == "1":
            item_id = input("Enter 6-digit item ID: ")
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = input("Enter item price: ")
            print("-" * 40)
            manager.add_item(item_id, name, description, price)
        elif choice == "2":
            manager.view_items()
        elif choice == "3":
            item_id = input("Enter item ID: ")
            name = input("Enter name: ")
            description = input("Enter description: ")
            price = input("Enter price: ")
            print("-" * 40)
            manager.update_item(item_id, name or None, description or None, price or None)
        elif choice == "4":
            item_id = input("Enter item ID: ")
            print("-" * 40)
            manager.delete_item(item_id)
        elif choice == "5":
            print("Thank you for using our program!...")
            break
        else:
            print("Invalid choice. Please try again.")
            print("-" * 40)
            
if __name__ == "__main__":
    main()