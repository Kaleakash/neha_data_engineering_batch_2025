# try:
#     result = 100/0
#     print(result)
# except:
#     print("Some error generated")
# print("Bye..")
# print("Bye...")
# num=20;
# try:
#     if num > 10:
#         print("Yes")
#     else:
#         print("No")
#     result = 100/0
#     print(result)
# except Exception as exp:
#     print("Error generated")
#     print(exp)
# print("Bye...")
# print("Bye...")

# import sys

# a=10;
# b=1;
# try:
#     result = a/b;
# except:
#     print(sys.exc_info()[0])
#     print(sys.exc_info()[1])
# finally:
#     print("Executed 100% sure doesn't matter exception generate or not ")
# print("Normal Statement execute")

# try:
#     result = 100/0;
#     print("No Exception")
# finally:
#     print("finally block")
# print("normal Statement")

# creating custom exception 
# class AgeException(Exception):
#     pass

# age=13;
# try:
#     if age >= 21:
#         print("You can apply for this job")
#     else:
#         raise AgeException("Age must be >=21");
# except AgeException as exp:
#     print(exp)
# print("normal Statement")