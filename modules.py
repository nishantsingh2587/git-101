"""
modules-->pull in python standard libraries
"""
"""import math
print(math.pi)
print(math.sqrt(144))
print(math.ceil(4.1))"""

import math
from random import randint,choice,seed
import datetime as dt 
import json  
print(math.pi)
print(math.sqrt(144))
print(math.ceil(4.1))
print(randint(1,6))
print(choice(["Rock","Paper","Scissors"]))
today =dt.date.today()
print(today)
print(type(today))
print(today.year)
print(today.month)
print(today.day)

new_year=dt.date(today.year,12,13)
my_bday=dt.date(2005,8,25)
print(my_bday)
print("new year",new_year)

user={"name":"arjit","skills":["py","ai"]}
text=json.dumps(user)
print("user json",text)
back=json.loads(text)

