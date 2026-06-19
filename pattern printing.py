"""
nested loop-- a loop inside the loop
"""
"""
#Mental model Rows X cols
for row in range(3):
    for col in range(4):
        print(f"({row},{col})",end="")
    print()   

"""
n=int(input("enter a number"))
for n in range(1,21):
    if n%3==0 and n%5==0: 
        print("fizzbuzz")  
    elif n%3==0:
        print("fiz")
    elif n%5==0: 
        print("buzz") 
    else:
        print(n)      