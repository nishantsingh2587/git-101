#list
"""
cart=["milk","bread","banana"]
print("cart:",cart)
print("first item of cart",cart[0])
cart.append("rice")
cart.insert(0,"tea")
shopping_list=["jam","oil"]
cart.extend(shopping_list)
print(cart)
"""
"""
demo=[1,2]
demo.append([3,4])
print("demo after append",demo)
demo=[1,2]
demo.extend([3,4])
print("demo after extend",demo)
"""

print_queue=[]
print_queue.append("report.pdf")
print_queue.append("invoice.pdf")
print_queue.append("photo.png")
print(f"{len(print_queue)}jobs waiting")
