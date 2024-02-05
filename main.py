import user_input
import menu
import receipts

tax = .05
# cost_of_item = 0
# quantity = 0
price = 0
sub_total = 0
grand_total = 0
# shopping_cart = []
# shopping_cart_quantity = []

val = False
cart = []
cart_quantity = []
rec = receipts.calc
while val == False:

    selection = int(input("which item would you like to purchase? select number "))
    for index, items in enumerate(menu.menu):
        if index + 1 == selection:
            cart.append(items.name)
            print(f'you selected {items.name}!')
            quantity = int(input("how many would you like? "))
            cart_quantity.append(quantity)
            user_input.cart_items(cart, cart_quantity)
            sub_total += quantity * items.price
            grand_total = (sub_total * tax) + sub_total
            rec.calculate_totals("", sub_total, grand_total)

            choice = input("would you like to display the menu? Or would you like to complete your purchase? menu/finish ")
            if choice == "menu":
                print()
            elif choice == "finish":
                val = True
payment = input("how would you like to pay? cash credit or check\n")
receipts.calc.process_payment("", payment)

class calc: 
    def __init__(self,cart):
        self.cart=cart
    def calculate_totals(self):
        subtotal = sum(item['line_total'] for item in self.cart)
        sales_tax = subtotal * 0.08
        grand_total = subtotal + sales_tax
        return subtotal, sales_tax, grand_total

    def process_payment(self, payment_type):
        if payment_type == "cash":
            amount = float(input("Enter amount tendered: $"))
            return amount - self.calculate_totals()
        elif payment_type == "check":
            check_number = input("Enter check number: ")
            return f"Check Number: {check_number}"
        elif payment_type == "credit":
            ccnum = input("Enter credit card number: ")
            expiration = input("Enter expiration date (MM/YY): ")
            cvv = input("Enter CVV: ")
            return f"Credit Card: {ccnum}, Expiration: {expiration}, CVV: {cvv}"

    def receipt(self):
        subtotal, sales_tax, grand_total = self.calculate_totals()
        print("Receipt:")
        self.display_cart()
        print(f"Subtotal: ${subtotal}")
        print(f"Sales Tax: ${sales_tax}")
        print(f"Grand Total: ${grand_total}")



