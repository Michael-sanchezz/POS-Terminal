class MenuItem:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} - ${self.price}\t {self.description}'

class Calc:
    def __init__(self, cart):
        self.cart = cart

    def calculate_totals(self, sub_total):
        sales_tax = sub_total * tax
        grand_total = sub_total + sales_tax
        return sub_total, sales_tax, grand_total

    def process_payment(self, payment_type, sub_total):
        if payment_type == "cash":
            amount = float(input("Enter amount tendered: $"))
            return amount - sub_total
        elif payment_type == "check":
            check_number = input("Enter check number: ")
            return f"Check Number: {check_number}"
        elif payment_type == "credit":
            ccnum = input("Enter credit card number: ")
            expiration = input("Enter expiration date (MM/YY): ")
            cvv = input("Enter CVV: ")
            return f"Credit Card: {ccnum}, Expiration: {expiration}, CVV: {cvv}"

    def receipt(self, sub_total, grand_total, tax):
        print("Receipt:")
        print(f"Subtotal: ${sub_total}")
        print(f"Sales Tax: ${sub_total * tax}")
        print(f"Grand Total: ${grand_total}")

h1 = MenuItem("Little Hamburger", "Burgers", "Single patty hamburger with Lettuce, Tomatoes, and Ketchup.", 2.99)
h2 = MenuItem("Little Cheeseburger", "Burgers", "Single patty hamburger with Cheese, Lettuce, Tomatoes, and Ketchup.", 3.99)
h3 = MenuItem("Little Bacon Burger", "Burgers", "Single patty hamburger with Bacon, Lettuce, Tomatoes, and Ketchup.", 4.99)
h4 = MenuItem("Little Bacon Cheeseburger", "Burgers", "Single patty hamburger with Bacon, Cheese Lettuce, Tomatoes, and Ketchup.", 5.99)
h5 = MenuItem("Hamburger", "Burgers", "Double patty hamburger with Lettuce, Tomatoes, and Ketchup.", 5.99)
h6 = MenuItem("Cheeseburger", "Burgers", "Double patty hamburger with Cheese, Lettuce, Tomatoes, and Ketchup.", 6.99)
h7 = MenuItem("Bacon Burger", "Burgers", "Double patty hamburger with Bacon, Lettuce, Tomatoes, and Ketchup.", 7.99)
h8 = MenuItem("Bacon Cheeseburger", "Burgers", "Double patty hamburger with Bacon, Cheese Lettuce, Tomatoes, and Ketchup.", 8.99)

h9 = MenuItem("Hotdog", "Dogs", "Grilled all-beef hotdog.", 1.99)
h10 = MenuItem("Cheese Dog", "Dogs", "Grilled all-beef hotdog, topped with Cheese sauce.", 2.99)
h11 = MenuItem("Chili Dog", "Dogs", "Grilled all-beef hotdog, topped with our homemade Chili.", 2.99)
h12 = MenuItem("Chili-Cheese Dog", "Dogs", "Grilled all-beef hotdog, topped with our homemade Chili and Cheese sauce", 3.99)

h13 = MenuItem("Fries", "Fries", "Freshly made fries, cooked in peanut oil, seasoned with salt.", 1.99)
h14 = MenuItem("Season-Fries", "Fries", "Freshly made fries, cooked in peanut oil, seasoned with our signature blend of cajun spices.", 1.99)
h15 = MenuItem("Cheese Fries", "Fries", "Freshly made fries, cooked in peanut oil, topped with Cheese sauce.", 2.99)
h16 = MenuItem("Loaded Fries", "Fries", "Freshly made fries, cooked in peanut oil, topped with our homemade Chili and Cheese sauce.", 4.99)

h17 = MenuItem("Small Fountain Drink", "Drinks", "Small drink.", 1.99)
h18 = MenuItem("Large Fountain Drink", "Drinks", "Large drink.", 2.49)
h19 = MenuItem("Water Bottle", "Drinks", "16oz Desani", 1.99)


menu_items = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19]

menu_by_category = {}

for item_number, item in enumerate(menu_items, start=1):
    category = item.category
    if category not in menu_by_category:
        menu_by_category[category] = []

    menu_by_category[category].append((item_number, item))

for category, items in menu_by_category.items():
    print(f"{category}:")
    for item_number, item in items:
        print(f"  {item_number}: {item.name} - {item.description} - ${item.price}")
    print()

cart = []
sub_total = 0
grand_total = 0
rec = Calc(cart)
tax = 0.08

val = False
while not val:
    selection = int(input("Which item would you like to purchase? Select number: "))
    for index, item in enumerate(menu_items, start=1):
        if index == selection:
            cart.append(item)
            print(f'You selected {item.name}!')
            quantity = int(input("How many would you like? "))
            cart.append(quantity)
            sub_total += quantity * item.price
            grand_total = (sub_total * tax) + sub_total
            choice = input("Would you like to display the menu? Or would you like to complete your purchase? menu/finish ")
            if choice == "menu":
                print()
            elif choice == "finish":
                val = True

payment = input("How would you like to pay? Cash, credit, or check")
payment_result=rec.process_payment(payment, sub_total)
rec.receipt(sub_total, grand_total, tax)

print(payment_result)

