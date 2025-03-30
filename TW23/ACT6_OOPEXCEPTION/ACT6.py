class Item:
    def __init__(self, item_id: int, name: str, description: str, price: float):
        if not isinstance(item_id, int) or item_id <= 0:
            raise ValueError("ID must be a positive integer.")
        if not name.strip():
            raise ValueError("Name cannot be empty.")
        if not isinstance(price, (int, float)) or price < 0:
            raise ValueError("Price must be a non-negative number.")
        
        self.id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"Item[ID: {self.id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}]"

class ItemManager:
    def __init__(self):
        self.items = {}
    
    def create_item(self, item_id, name, description, price):
        try:
            if item_id in self.items:
                raise ValueError("Item ID already exists.")
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item added successfully!")
        except ValueError as e:
            print(f"Error: {e}")
    
    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)
    
    def update_item(self, item_id, name=None, description=None, price=None):
        if item_id not in self.items:
            print("Error: Item ID not found.")
            return
        
        item = self.items[item_id]
        if name:
            item.name = name
        if description:
            item.description = description
        if price is not None:
            if not isinstance(price, (int, float)) or price < 0:
                print("Error: Invalid price.")
                return
            item.price = price
        
        print("Item updated successfully!")
    
    def delete_item(self, item_id):
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Error: Item ID not found.")

if __name__ == "__main__":
    manager = ItemManager()
    manager.create_item(1, "Laptop", "Gaming laptop", 1500.0)
    manager.create_item(2, "Mouse", "Wireless mouse", 25.0)
    
    print("\nAll Items:")
    manager.read_items()
    
    manager.update_item(1, price=1400.0)
    print("\nAfter Update:")
    manager.read_items()
    
    manager.delete_item(2)
    print("\nAfter Deletion:")
    manager.read_items()