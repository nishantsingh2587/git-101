"""
seconds =int(input("enter seconds"))
hours=seconds//3600
minute=(seconds%3600)//60
secs=seconds%60
print((hours,minute,secs))
"""
#task 2
#bmi calculator
"""
weight=float(input("enter a weight in kg"))
height=float(input("enter a height in meter"))
bmi=weight/(height**2)
print("bmi=",round(bmi,1))
"""
#task3
#initial form name
"""
full_name=input("enter full name")
words=full_name.split
intials=""
for words in words():
    intials+=words[0].upper()+"."
print(intials)
"""
#task4
"""def is_palindrome(text):
    cleaned=text.lower().replace("","")
    reversed_text=cleaned[::-1]
    return cleaned==reversed_text
print(is_palindrome("race car"))
print(is_palindrome("hello"))
print(is_palindrome("nurses run"))"""

#task5
text = input("Enter text: ")

words = text.split()

result = []

for word in words:
    result.append(word.capitalize())

print(" ".join(result))

#task6
"""def get_grade(marks):
    if marks<0 or marks>100:
        return "invalid"
    elif marks>=90:
        return"A"
    elif marks>=75:
        return"B"
    elif marks>=60:
        return"C"
    elif marks>=40:
        return"D"
    else:
        return"F"
marks=int(input("enter marks:"))
print("Grade:",get_grade(marks))"""
#leap year or not
"""def is_leap_year(year):
    return (year % 4==0 and year%100 !=0) or (year % 400==0)

year=int(input("enter a year"))
if is_leap_year(year):
    print("Leap year")
else:
    print("Not a leap year")"""

#task 8
"""
def digit_info(n):
    Return (sum_of_digits, number_of_digits).
    
    if n == 0:
        return (0, 1)

    digit_sum = 0
    digit_count = 0

    while n > 0:
        digit = n % 10
        digit_sum += digit
        digit_count += 1
        n //= 10

    return (digit_sum, digit_count)
print(digit_info(12345))
"""
#task9
"""
def print_triangle(n):
    
    for r in range(1, n + 1):
        print("* " * r)
print_triangle(4)
"""
"""
#task 10
def fibonacci(count):
    if count <= 0:
        return []

    fib = []
    a, b = 0, 1

    for _ in range(count):
        fib.append(a)
        a, b = b, a + b

    return fib

print(fibonacci(7))
"""
"""
#task11
def convert(temp, to="C"):
    if to == "F":
        return temp * 9/5 + 32
    elif to == "C":
        return (temp - 32) * 5/9
    else:
        return "Invalid unit"

print(convert(25, "F"))  # 77.0
print(convert(77, "C"))  # 25.0
"""
#task 12
def stats(*numbers):
    
    if not numbers:
        return None

    return {
        "min": min(numbers),
        "max": max(numbers),
        "avg": sum(numbers) / len(numbers)
    }

print(stats(10, 20, 30, 40))


print(stats())


