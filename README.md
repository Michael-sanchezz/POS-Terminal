Title: POS-Terminal

Tech: PyCharm (Python)

Project Description: The program is a cash register/ self-service terminal for a fast food resturant. It recieves an order from the customer and prompts payment options. The end result prints out the items ordered, substotal, grand total and appropriate payment info. 

Issues: While creating this program, we had to merge different codes from each group member to create a completed and seamless program. It took a bit of trial and error, along with a few logical errors to combine but after changing variable/function names and working to incoroporate each others code, we were able to achieve the desired result. 

How to use the project: The project should prompt the user to choose an item from the menu, after displaying it. The user must then decide how many of that item they choose and if they would like to choose something else from the menu or finish their order. Once the order is complete, the user is then prompted to answer if they would like to pay with cash, credit or a check. Based on the choice, the items ordered, subtotal , grand total and apppropriate payment info is displayed. The program then finishes. 

User selection and quantity:
selection = int(input("Which item would you like to purchase? select number "))
        if 1 <= selection <= len(menu.menu):
            items = menu.menu[selection - 1]
            cart.append(items.name) #adds name of item to the cart
            print(f'you selected {items.name}!')
            quantity = int(input("how many would you like? "))# how many of the item you selected
            
User selection to on which method to pay with:
while payment_val == True:
    payment = input("How would you like to pay? cash credit or check\n").lower()
    if payment == "cash" or payment == "credit" or payment == "check":
        receipts.calc.process_payment("", grand_total, payment)# select payment based on your choice
        payment_val = False
    else:
        print("Invalid payment option. Please enter cash, credit or check.")

