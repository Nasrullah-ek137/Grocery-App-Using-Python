# -------------------- ROYAL SMART GROCERY APP  ---------------------

class Store:
    def __init__(self):
        # DEFAULT PRODUCTS (7 PRODUCTS)
        self.products = [
            {"name": "Rice", "qty": 30, "price": 60},
            {"name": "Wheat Flour", "qty": 25, "price": 45},
            {"name": "Sugar", "qty": 40, "price": 42},
            {"name": "Milk", "qty": 20, "price": 50},
            {"name": "Surf Excel", "qty": 15, "price": 120},
            {"name": "Coca-Cola", "qty": 18, "price": 45},
            {"name": "Apple", "qty": 30, "price": 120}
        ]

        self.sales_history = []  # stores bills of customers

    # Find product by name
    def find_product(self, name):
        for p in self.products:
            if p['name'].lower() == name.lower():
                return p
        return None

    # Add product
    def add_product(self):
        print("\n--- Add New Product ---")
        name = input("Enter product name: ")

        existing = self.find_product(name)
        if existing:
            print("❌ Product already exists!")
            return

        try:
            qty = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
        except:
            print("Invalid Input!")
            return

        self.products.append({"name": name, "qty": qty, "price": price})
        print("✅ Product added successfully!")

    # Delete product
    def delete_product(self):
        print("\n--- Delete Product ---")
        name = input("Enter product name to delete: ")

        product = self.find_product(name)
        if product:
            self.products.remove(product)
            print("🗑 Product deleted!")
        else:
            print("❌ Product not found!")

    # Update product
    def update_product(self):
        print("\n--- Update Product ---")
        name = input("Enter product name to update: ")
        product = self.find_product(name)

        if not product:
            print("❌ Product not found!")
            return

        print("Current Details:", product)

        new_name = input("New name (blank = same): ")
        if new_name.strip():
            product['name'] = new_name

        new_qty = input("New quantity (blank = same): ")
        if new_qty.strip():
            product['qty'] = int(new_qty)

        new_price = input("New price (blank = same): ")
        if new_price.strip():
            product['price'] = float(new_price)

        print("✅ Product updated successfully!")

    # View products
    def view_products(self):
        print("\n--- All Products ---")
        if not self.products:
            print("No products available.")
            return

        for p in self.products:
            print(f"Name: {p['name']} | Qty: {p['qty']} | Price: ₹{p['price']}")

    # Low stock alert
    def low_stock(self):
        print("\n--- Low Stock Alerts ---")
        found = False
        for p in self.products:
            if p['qty'] <= 2:
                print(f"⚠ {p['name']} stock low ({p['qty']} left)")
                found = True

        if not found:
            print("No low-stock products.")


# -------------------------- CUSTOMER SYSTEM --------------------------
class Customer:
    def __init__(self, store: Store):
        self.store = store
        self.cart = []

    def view_products(self):
        self.store.view_products()

    # Add item to cart
    def purchase_product(self):
        print("\n--- Purchase Product ---")
        name = input("Enter product name: ")

        product = self.store.find_product(name)
        if not product:
            print("❌ Product not found!")
            return

        if product['qty'] <= 0:
            print("❌ Product out of stock!")
            return

        try:
            qty = int(input("Enter quantity: "))
        except:
            print("Invalid quantity!")
            return

        if qty > product['qty']:
            print(f"Only {product['qty']} left in stock!")
            return

        # Add to cart
        self.cart.append({
            "name": product['name'],
            "qty": qty,
            "price": product['price']
        })

        # Reduce store stock
        product['qty'] -= qty
        print("🛒 Added to cart!")

    # Billing + Gift logic
    def generate_bill(self):
        print("\n-----------------   BILL  ----------------")

        if not self.cart:
            print("Cart is empty!")
            return

        total = 0
        for item in self.cart:
            amount = item['qty'] * item['price']
            total += amount
            print(f"{item['name']} - Qty: {item['qty']} - ₹{amount}")

        print("-------------------------------------------------------")
        print(f"Total Amount: ₹{total}")

        # GIFT SYSTEM (Correct order)
        gift = None
        if total > 10000:
            gift = "Bluetooth Earphones"
        elif total > 2000:
            gift = "Sanitizer 50ml "
        elif total > 1000:
            gift = "Chocolate"

        if gift:
            print("🎉 Congratulations! You won:", gift)

        # PAYMENT MODE
        mode = input("\nSelect payment mode (COD/UPI): ").upper()
        if mode == "UPI":
            print("💳 Payment successful via UPI!")
        else:
            print("🚚 Cash on Delivery selected!")

        print("Thank you for shopping with us ❤")

        # Save sale
        self.store.sales_history.append({"cart": self.cart, "total": total})

        # Clear cart
        self.cart = []


# -------------------------- ADMIN SYSTEM --------------------------
class Admin:
    def __init__(self, store: Store):
        self.store = store   # FIXED

    def login(self):
        print("\n--- Admin Login ---")
        username = input("Enter username: ")
        password = input("Enter password: ")

        return username == "admin" and password == "1234"

    def admin_menu(self):
        while True:
            print("\n--- Admin Menu ---")
            print("1. Add Product")
            print("2. Delete Product")
            print("3. Update Product")
            print("4. View Products")
            print("5. Low Stock Alerts")
            print("6. Back to Home")

            choice = input("Enter choice: ")

            if choice == "1":
                self.store.add_product()
            elif choice == "2":
                self.store.delete_product()
            elif choice == "3":
                self.store.update_product()
            elif choice == "4":
                self.store.view_products()
            elif choice == "5":
                self.store.low_stock()
            elif choice == "6":
                break
            else:
                print("Invalid option!")


# -------------------------- MAIN APP --------------------------
class SmartGroceryApp:
    def __init__(self):
        self.store = Store()   # FIXED

    def run(self):
        while True:
            print("\n========== ROYAL SMART GROCERY APP ==========")
            print("1. Admin Login")
            print("2. Customer Panel")
            print("3. Exit")
            print("========================================")

            choice = input("Enter your choice: ")

            if choice == "1":
                admin = Admin(self.store)
                if admin.login():
                    print("Login Successful!")
                    admin.admin_menu()
                else:
                    print("❌ Incorrect credentials!")

            elif choice == "2":
                customer = Customer(self.store)
                while True:
                    print("\n--- Customer Menu ---")
                    print("1. View Products")
                    print("2. Purchase Product")
                    print("3. Generate Bill")
                    print("4. Back to Home")

                    c = input("Enter choice: ")

                    if c == "1":
                        customer.view_products()
                    elif c == "2":
                        customer.purchase_product()
                    elif c == "3":
                        customer.generate_bill()
                    elif c == "4":
                        break
                    else:
                        print("Invalid option!")

            elif choice == "3":
                print("Thank you for using Royal Smart Grocery App 😊")
                break

            else:
                print("Invalid Choice!\n")


# -------------------------- RUN APP --------------------------
app = SmartGroceryApp()
app.run()