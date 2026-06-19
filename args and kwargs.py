"""
*Args(extra positional-->tuple)
**kwargs(extra keyword)
"""
"""
def total(*args):
    print("args is tuple",args)
    return sum(args)
print("Total(10,20,40)=",total(10,20,40))
print("Total(10,250)=",total(10,250))
print("Total()=",total())
"""
def make_user(**kwargs):
    print("kwargs is a dict",kwargs)
    return kwargs

make_user(name="ashish",age=22,city="lucknow")
make_user(name="ben")