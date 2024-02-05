class calc:
    def __init__(self, cart):
        self.cart = cart

    def calculate_totals(self, sub, grand):
        print(f'\nsub total: $%.2f' % sub)
        print(f'Grand total: $%.2f' % grand)
        return ""

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
