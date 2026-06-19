"""
dict=store in key and value pairs
"""
student={
    "name":"Nishant",
    "age":21,
    "marks":[88,43,23]

}
"""
print("Name:",student["name"])
print("how many item in dict:",len(student))
print("age in student:","age"in student)
print("missing value:",student(college))
"""
"""
removed_item=student.pop("marks")
print(removed_item)
"""
"""
#task-->create the total bill
prices={
    "coffee":120,
    "juice":100,
    "sandwidth":150

}
"""
order=[coffee,juice]
total_bill=0
for item in order:
    total_bill +=prices.get(item)
