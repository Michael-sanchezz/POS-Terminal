# create function for user choice
# display everything in cart that they have picked so far


def cart_items(cart, quantity):
    for x, y in zip(cart, quantity):
        print(f'{y} {x}(s) in your cart')
    return ""
