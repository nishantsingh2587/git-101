"""
Break- Quit the loop 
continue-Skip the round 
"""
"""
orders=[100,299,499,1299,80]
for amount in orders :
    if amount >1000:
        print(f"We Have  a Big order :Rs{amount}-stopping")
        break
    print(f"checked Rs {amount}:Small Orders")

"""
"""
transaction = [300,343,800,343,-300,-199,400]
income=0
for t in transaction:
    if t<0:
        print(f"Skipping Refund : {t}")
        continue
    income+=t
print(f"total income : {income}")    
"""   

correct_pin=1234
attempt_left=3

while attempt_left>0:
    enterd_pin=input(f"enter pin.{attempt_left}attempt left")
    if enterd_pin==correct_pin:
        print("acess granted!")
        break
    attempt_left-=1
    print("wrong pin")
else:
    print("card blocked !!!")