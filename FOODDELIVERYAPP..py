# food_delivery_app.py

class FoodDeliveryApp:
    def __init__(self):
        self.menu = {
            'Pizza': 10.00,
            'Burger': 5.00,
            'Salad': 7.00
        }
        self.orders = []
    
    def display_menu(self):
        print("Menu:")
        for item, price in self.menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self):
        self.display_menu()
        order_item = input("Enter the food item you want to order (or type 'done' to finish): ")
        while order_item.lower() != 'done':
            if order_item in self.menu:
                self.orders.append(order_item)
                print(f"Added {order_item} to your order.")
            else:
                print("Item not found on the menu.")
            order_item = input("Enter another item (or type 'done' to finish): ")

    def view_order(self):
        if not self.orders:
            print("No orders yet.")
            return
        print("Your order:")
        total = 0
        for item in self.orders:
            print(f"{item}: ${self.menu[item]:.2f}")
            total += self.menu[item]
        print(f"Total: ${total:.2f}")

    def run(self):
        while True:
            print("\\nWelcome to the Food Delivery App")
            print("1. View Menu")
            print("2. Order Food")
            print("3. View Order")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                self.display_menu()
            elif choice == '2':
                self.take_order()
            elif choice == '3':
                self.view_order()
            elif choice == '4':
                print("Thank you for using the Food Delivery App. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    app = FoodDeliveryApp()
    app.run()
