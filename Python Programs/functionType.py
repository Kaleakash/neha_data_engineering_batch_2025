# # basic function 
# # function no passing parameter and no return 
# def greet():
#     print("Hello, World!")

# greet()  # Output: Hello, World!

# # function with passing parameter 
# def add(a, b):
#     sum = a+b;
#     print("Sum is:", sum)

# add(5, 10)  # Output: Sum is: 15
# add(20, 30)  # Output: Sum is: 50

# # function pass parameter and return value 
# def check_even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"
# print(check_even_odd(4))  # Output: Even
# print(check_even_odd(7))  # Output: Odd

# function with parameter names 
# def employee_info(name, age, position):
#     print("Name:", name)
#     print("Age:", age)
#     print("Position:", position)

# employee_info("Alice", 30, "Developer");
# #employee_info(40, "Manager", "Bob");  
# employee_info(position="Manager", name="Bob", age=40);

# function with arbitrary number of parameters
# def student_info(id,name, *marks):
#     print("ID:", id)
#     print("Name:", name)
#     print("Marks:", marks)
#     total = sum(marks)
#     print("Total Marks:", total)

# student_info(101, "John", 85, 90, 78)
# student_info(102, "Jane", 88)
# student_info(103, "Mike")

# function with default parameter values
# def emp_info(id=0,name="Unknown",salary=10000):
#     print("ID:", id)
#     print("Name:", name)
#     print("Salary:", salary)

# emp_info(1,"Alice",50000)
# emp_info(2,"Bob");
# emp_info(3)
# emp_info();

# function with return multiple values
# def calculation(a,b):
#     sum = a+b;
#     sub = a-b;
#     mul = a*b;
#     div = a/b;
#     return sum, sub, mul, div

# calculation_result = calculation(20, 5)
# print("Calculation Results:", calculation_result)
# print("Sum:", calculation_result[0])
# print("Subtraction:", calculation_result[1])
# print("Multiplication:", calculation_result[2])
# print("Division:", calculation_result[3])

# function with lambda expression
# square = lambda x: x * x
# print("Square of 5:", square(5))  # Output: Square of 5: 25
# print("Square of 10:", square(10))  # Output: Square of 10

# lambda with map function 
# numbers = [1, 2, 3, 4, 5]
# squared_numbers = list(map(lambda x: x * x, numbers))
# print("Squared Numbers:", squared_numbers)  # Output: Squared Numbers: [1, 4, 9, 16, 25]

# lambda with filter function
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Even Numbers:", even_numbers)  # Output: Even Numbers: [2, 4, 6, 8, 10]
print("Odd Numbers:", odd_numbers)    # Output: Odd Numbers: [1, 3, 5, 7, 9]










