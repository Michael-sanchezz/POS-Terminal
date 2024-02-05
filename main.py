import user_input
import menu
import receipts

tax = .05
price = 0
sub_total = 0
grand_total = 0
cart = []
cart_quantity = []

val = False

rec = receipts.calc
while val == False:

    selection = int(input("which item would you like to purchase? select number "))
    for index, items in enumerate(menu.menu):
        if index + 1 == selection:
            cart.append(items.name) #adds name of item to the cart
            print(f'you selected {items.name}!')
            quantity = int(input("how many would you like? "))# how many of the item you selected
            cart_quantity.append(quantity)# add quantity to a cart list
            user_input.cart_items(cart, cart_quantity) #calls userinput file to show cart items and quantity
            sub_total += quantity * items.price #calculates subtotal
            grand_total = (sub_total * tax) + sub_total #calculates grandtotal
            rec.print_sub_grand("", sub_total, grand_total)# prints the subtotal and grandtotal

            choice = input("would you like to display the menu? Or would you like to complete your purchase? menu/finish ")
            # if finish then break out of loop and go to payment/ if menu then stay in loop and select more items
            if choice == "menu":
                print()
            elif choice == "finish":
                val = True

payment = input("how would you like to pay? cash credit or check\n")
receipts.calc.process_payment("", grand_total, payment)# select payment based on your choice




