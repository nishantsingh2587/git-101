"""
seconds =int(input("enter seconds"))
hours=seconds//3600
minute=(seconds%3600)//60
secs=seconds%60
print((hours,minute,secs))
"""
#task 2

def to_hms(total_seconds):
    hours=total_seconds//3600
    leftover=total_seconds%3600

    minutes=leftover//60
    seconds=leftover%60
    return(hours,minutes,seconds)