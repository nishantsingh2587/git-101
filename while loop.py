""" 
while loop
"""
#Anatomy ==> init =>test => update
"""
count=1
while count<= 5:
    print(f"Rap {count} of 5")
    count+=1
print("Done Counting\n")    
"""
"""
num=10
while num>0:
    print(f"launched in{num}num")
    num-=1
print("take off\n")   
"""
"""
pending_order = ["ORD101","ORD102","ORD103"]
while pending_order:
    order=pending_order.pop(0)
    print(f"processing{order}..shipped")
print("all orderd procssed!\n")    
"""
"""
print("Tiny menu-type'quit'to leave")
while True:
    choice=input("pick(status/help/quit)".strip().lower())
    if choice == "quit":
        print("bye")
        break
    elif choice=="status":
        print("all system up")
    elif choice=="help":
        print("commands :status,help,quit")
    else:
        print(f"unknown command :{choice}")    

"""        