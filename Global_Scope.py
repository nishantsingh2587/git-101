#Global_Scope
app_name =" My First App"

#local Scope
"""
def show_total():
    total=999
    print("welcome to :",app_name)
    print("inside:",total)
show_total()
"""

def make_multiplier(factor):
    def multiply(n):
        return n*factor
    return multiply
triple=make_multiplier(3)
print(triple(10))
tenfold=make_multiplier(10)
print(tenfold(90))
