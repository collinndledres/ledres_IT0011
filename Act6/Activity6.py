class Item:
    def __init__(self, item_id, name, description, price):
        if not item_id.strip() or not name.strip() or not description.strip() or price <= 0:
            raise ValueError("Invalid input: Make sure all fields are filled correctly and the price is positive.")
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

    def __str__(self):
        return f"ID: {self.item_id}, Name: {self.name}, Description: {self.description}, Price: ${self.price:.2f}"


class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self):
        try:
            item_id = input("Enter Item ID: ").strip()
            if item_id in self.items:
                print("Item with this ID already exists.")
                return
            name = input("Enter Item Name: ").strip()
            description = input("Enter Item Description: ").strip()
            price = float(input("Enter Item Price: ").strip())
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("Item created successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def read_items(self):
        if not self.items:
            print("No items available.")
        else:
            for item in self.items.values():
                print(item)

    def update_item(self):
        item_id = input("Enter Item ID to update: ").strip()
        if item_id not in self.items:
            print("Item not found.")
            return
        item = self.items[item_id]

        name = input("Enter new Item Name (leave blank to keep current): ").strip()
        description = input("Enter new Item Description (leave blank to keep current): ").strip()
        price_input = input("Enter new Item Price (leave blank to keep current): ").strip()

        if name:
            item.name = name
        if description:
            item.description = description
        if price_input:
            try:
                price = float(price_input)
                if price <= 0:
                    print("Price must be positive.")
                    return
                item.price = price
            except ValueError:
                print("Invalid price value.")
                return

        print("Item updated successfully!")

    def delete_item(self):
        item_id = input("Enter Item ID to delete: ").strip()
        if item_id in self.items:
            del self.items[item_id]
            print("Item deleted successfully!")
        else:
            print("Item not found.")


def main():
    manager = ItemManager()

    while True:
        print("\nItem Management Application")
        print("1. Create Item")
        print("2. View All Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            manager.create_item()
        elif choice == '2':
            manager.read_items()
        elif choice == '3':
            manager.update_item()
        elif choice == '4':
            manager.delete_item()
        elif choice == '5':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()