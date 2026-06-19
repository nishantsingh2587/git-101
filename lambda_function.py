"""
Lambda function-->throwaway function you do not use def keyword

"""

"""def square_def(n):
    return n*n
square_lambda=lambda n:n*n
print(square_def(10))
print(square_lambda(10))"""

"""nums=[1,2,3,4,5,6]
#map:apply a function to every item.ab
double=list(map(lambda n:n*2,nums))
print(double)
"""
evens=list(filter(lambda n: n%2==0,nums))
print(evens)
