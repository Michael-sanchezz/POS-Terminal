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

            # if payment == "cash":
            #     cash = int(input("what cash amount will you give "))
            #     change = cash - grand_total
            #     print(f"your change is $%.2f" % sub_total)
            # elif payment == "check":
            #     check_num = int(input("enter check number "))
            # elif payment == "credit":
            #     cc_num = int(input("enter credit card number "))
            #     cc_exp = int(input("enter expiration date in mmyy format"))
            #     cc_cvv = int(input("enter cvv"))
            # print(receipt(shopping_cart, shopping_cart_quantity))

            # print(f'you selected {items.name}')
            # user_input.user_choice(user_input.shopping_cart.append(items.name))
#             shopping_cart.append(items.name)
#             price = items.price
#             quantity = int(input("how many would you like? "))
#             sub_total += (quantity * price)
#             user_input.user_choice(selection)
#             # user_input.user_choice(user_input.shopping_cart_quantity.append(items.name))
#             shopping_cart_quantity.append(quantity)
#             user_input.cart_items(shopping_cart,shopping_cart_quantity)
#             grand_total = (sub_total * tax) + sub_total
#             print(f'\nsub total: ${sub_total}\ntax: {tax}\nGrand total: $%.2f' % grand_total)
#     choice = input("would you like to display the menu? Or would you like to complete your purchase? menu/finish ")
#     if choice == "menu":
#         print()
#     elif choice == "finish":
#         val = True
# #
# payment = input("how would you like to pay? cash credit or check\n")
# if payment == "cash":
#     cash = int(input("what cash amount will you give "))
#     change = cash - grand_total
#     print(f"your change is $%.2f" % sub_total)
# elif payment == "check":
#     check_num = int(input("enter check number "))
# elif payment == "credit":
#     cc_num = int(input("enter credit card number "))
#     cc_exp = int(input("enter expiration date in mmyy format"))
#     cc_cvv = int(input("enter cvv"))
# print(receipt(shopping_cart, shopping_cart_quantity))
