class menu_item:
    def __init__(self, name, category, description, price):
        self.name = name
        self.category = category
        self.description = description
        self.price = price

    def __str__(self):
        return f'{self.name} - ${self.price}\t {self.description}'




# Lines 17 thru 59 is testing / validation.

h1 = menu_item("Little Hamburger", "Burgers", "Single patty hamburger with Lettuce, Tomatoes, and Ketchup.", 2.99)
h2 = menu_item("Little Cheeseburger", "Burgers", "Single patty hamburger with Cheese, Lettuce, Tomatoes, and Ketchup.", 3.99)
h3 = menu_item("Little Bacon Burger", "Burgers", "Single patty hamburger with Bacon, Lettuce, Tomatoes, and Ketchup.", 4.99)
h4 = menu_item("Little Bacon Cheeseburger", "Burgers", "Single patty hamburger with Bacon, Cheese Lettuce, Tomatoes, and Ketchup.", 5.99)
h5 = menu_item("Hamburger", "Burgers", "Double patty hamburger with Lettuce, Tomatoes, and Ketchup.", 5.99)
h6 = menu_item("Cheeseburger", "Burgers", "Double patty hamburger with Cheese, Lettuce, Tomatoes, and Ketchup.", 6.99)
h7 = menu_item("Bacon Burger", "Burgers", "Double patty hamburger with Bacon, Lettuce, Tomatoes, and Ketchup.", 7.99)
h8 = menu_item("Bacon Cheeseburger", "Burgers", "Double patty hamburger with Bacon, Cheese Lettuce, Tomatoes, and Ketchup.", 8.99)

h9 = menu_item("Hotdog", "Dogs", "Grilled all-beef hotdog.", 1.99)
h10 = menu_item("Cheese Dog", "Dogs", "Grilled all-beef hotdog, topped with Cheese sauce.", 2.99)
h11 = menu_item("Chili Dog", "Dogs", "Grilled all-beef hotdog, topped with our homemade Chili.", 2.99)
h12 = menu_item("Chili-Cheese Dog", "Dogs", "Grilled all-beef hotdog, topped with our homemade Chili and Cheese sauce", 3.99)

h13 = menu_item("Fries", "Fries", "Freshly made fries, cooked in peanut oil, seasoned with salt.", 1.99)
h14 = menu_item("Season-Fries", "Fries", "Freshly made fries, cooked in peanut oil, seasoned with our signature blend of cajun spices.", 1.99)
h15 = menu_item("Cheese Fries", "Fries", "Freshly made fries, cooked in peanut oil, topped with Cheese sauce.", 2.99)
h16 = menu_item("Loaded Fries", "Fries", "Freshly made fries, cooked in peanut oil, topped with our homemade Chili and Cheese sauce.", 4.99)

h17 = menu_item("Small Fountain Drink", "Drinks", "Small drink.", 1.99)
h18 = menu_item("Large Fountain Drink", "Drinks", "Large drink.", 2.49)
h19 = menu_item("Water Bottle", "Drinks", "16oz Desani", 1.99)


menu = [h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12, h13, h14, h15, h16, h17, h18, h19]

# Create a dictionary to organize items by category
menu_by_category = {}

# Populate the dictionary
for item_number, item in enumerate(menu, start=1):
    category = item.category
    if category not in menu_by_category:
        menu_by_category[category] = []

    menu_by_category[category].append((item_number, item))


# Print menu items per category with item number
for category, items in menu_by_category.items():
    print(f"{category}:")
    for item_number, item in items:
        print(f"  {item_number}: {item.name} - {item.description} - ${item.price}")
    print()






