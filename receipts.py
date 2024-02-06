class calc:
    def __init__(self, cart):
        self.cart = cart

    def print_sub_grand(self, sub, grand):
        print(f'\nsub total: $%.2f' % sub)
        print(f'Grand total: $%.2f' % grand)
        return ""

    def get_change(self, change):
        return f'your change is $%.2f' % change

    def process_payment(self, grand, payment_type):
        if payment_type == "cash":
            amount = int(input("Enter amount tendered: $"))
            amount = amount - grand
            print(calc.get_change("", amount))
            return ""
        elif payment_type == "check":
            check_number = input("Enter check number: ")
            print(f"Thanks for your payment! \nyour payment info{check_number}")
            return ""
        elif payment_type == "credit":
            ccnum = input("Enter credit card number: ")
            expiration = input("Enter expiration date (MMYY): ")
            cvv = input("Enter CVV: ")
            ccnum = str(ccnum)
            print("thanks for your payment!")
            print(f"your cc info {ccnum[-4:]}")
            print(f"your expiration info {expiration}")
            print(f"your cvv info {cvv}")
            print()
            return ""
