students = {1:"Alice", 2:"Bob", 3:"Charlie"}
print(students)
print(type(students))
print(students[2])  # Accessing value using key
students[4] = "David"  # Adding a new key-value pair
print(students)
students[1]= "Alicia"  # Modifying an existing value
print(students)
print(len(students))  # Getting the number of key-value pairs
print(students.keys())  # Getting all keys
print(students.values())  # Getting all values
#del students[30]  # Deleting a key-value pair
print(students)
result = students.pop(2)  # Removing a key-value pair and returning its value
print(students)
print(result)