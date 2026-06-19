"""

def add_cart_item(item,cart=[]):
    cart.append(item)
    return cart

print("",add_cart_item("apple"))
print("",add_cart_item("banana"))
print("",add_cart_item("bread"))    
"""
def add_cart(item,cart=None):
    if cart is None:
        cart=[]
    cart.append(item)
    return cart
print("",add_cart("Apple"))
print("",add_cart("Banana"))
print("",add_cart("Milk"))