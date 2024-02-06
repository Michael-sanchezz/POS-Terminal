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
    try:#try statement to catch incorrect inputs
        selection = int(input("Which item would you like to purchase? select number "))
        if 1 <= selection <= len(menu.menu):# selects menu option only. If not in menu then returns invalid
            items = menu.menu[selection - 1]# menu choice
            cart.append(items.name) #adds name of item to the cart
            print(f'you selected {items.name}!')# displays the selected item
            quantity = int(input("how many would you like? "))# how many of the item you selected
            if quantity>0:#this if statement adds item to cart
                cart_quantity.append(quantity)# add quantity to a cart list
                user_input.cart_items(cart, cart_quantity) #calls userinput file to show cart items and quantity
                sub_total += quantity * items.price #calculates subtotal
                grand_total = (sub_total * tax) + sub_total #calculates grandtotal
                rec.print_sub_grand("", sub_total, grand_total)# prints the subtotal and grandtotal
                val2 = True
                while val2 == True:
                    choice = input("Would you like to display the menu? Or would you like to complete your purchase? menu/finish ").lower()
                # if finish then break out of loop and go to payment/ if menu then stay in loop and select more items
                    if choice == "menu":
                        print(menu.menu_item.print_menu(""))#displays the menu
                        break
                    elif choice == "finish":#proceeds to payment if this condition is triggered
                        val2 = False
                        val = True
                    else:
                        print("Invalid choice, please select menu or finish.")#checks for invalid input
            else:
                print("Invalid selection. Please choose a valid item number.")
    except ValueError:(
        print("Invalid input. Please enter a number."))
payment_val= True
while payment_val == True:
    payment = input("How would you like to pay? cash credit or check\n").lower()
    rec.print_sub_grand("", sub_total, grand_total)
    if payment == "cash" or payment == "credit" or payment == "check":#check for 1 of 3 payment options
        receipts.calc.process_payment("", grand_total, payment)# select payment based on your choice
        payment_val = False
    else:#if incorrect option selected asks for input again
        print("Invalid payment option. Please enter cash, credit or check.")

