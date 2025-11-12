# creating Simple class 

# class Car:
#     pass;
# # creating object of class
# innova = Car()
# print(innova)
# print(type(innova))


# creating class with methods or function 
# class Car :
#     def start(self):
#         print("car started")
#     def stop(self):
#         print("car stopped")

# innova = Car();
# innova.start()
# innova.stop()

# creating Car class with attributes and methods
# class Car:
#     wheel = 4  # class attribute
#     price = 1000000  # class attribute
#     color = "red"  # class attribute
#     def print_car_details(self):  # method
#         print(f"Car color is {self.color}")
#         print(f"Car price is {self.price}")
#         print(f"Car has {self.wheel} wheels")
# innova = Car()
# innova.color = "white"
# innova.price = 30000000
# innova.print_car_details()
# print("-----")
# swift = Car()
# swift.color = "black"
# swift.price = 1500000
# swift.print_car_details()

# creating class with constructor
# class Car:
#     def __init__(self):
#         print("Constructor called")
#     def car_function(self):
#         print("car function called")
# innova = Car()
# innova.car_function()
# innova.car_function()
# swift = Car()
# swift.car_function()


# creating class with parameterized constructor
# class Car:
#     def __init__(self, color, price=1000000, model="Base Model"):
#         self.color = color
#         self.price = price
#         self.model = model

#     def print_car_details(self):
#         print(f"Car model is {self.model}")
#         print(f"Car color is {self.color}")
#         print(f"Car price is {self.price}")
# innova = Car("white", 3000000, "Innova Crysta")
# innova.print_car_details()
# print("-----")
# swift = Car("black", 1500000, "Swift Dzire")
# swift.print_car_details()
# print("-----")
# baleno = Car("blue", 1200000)
# baleno.print_car_details()
# print("-----")
# ertiga = Car("silver")
# ertiga.print_car_details()

# python with constructor and destructor example 
# class Car:
#     def __init__(self,color,wheel):
#         print("Object created")
#         self.color= color;
#         self.wheel= wheel;
#     def hello(self):
#         print("Hello Car ",self.color,self.wheel)
#     def __del__(self):      # destructor
#         print("Object destroyed")
#     def __str__(self):
#         return f"Car color is {self.color} and Car has {self.wheel} wheels"
# innova = Car("Black",4)
# innova.hello()
# innova.hello()
# print(innova.color,innova.wheel)
# print(innova)   # it call automatically when ever we display reference using print
#innova=None  # dereferencing the object

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_employee_details(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Salary: {self.salary}")
# emp1 = Employee("John Doe", 50000)
# emp1.display_employee_details()
# print(hasattr(emp1, 'name'))  # True
# print(hasattr(emp1, 'age'))  # False
# # we can set dynamic property 
# setattr(emp1, 'age', 30)
# print(hasattr(emp1, 'age'))  # True
# print(getattr(emp1, 'age'))  # 30

# class property private and public 
# class Employee:
#     def __init__(self):
#         self.name = "John"      # public property
#         self.__salary = 50000   # private property
#     def display_employee_details(self):
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Salary: {self.__salary}")
#     def __private_method(self):
#         print("This is a private method")
# emp1 = Employee()
# emp1.display_employee_details()
# print(emp1.name)        # accessible
# #print(emp1.__salary)  # AttributeError: 'Employee' object has no attribute
# #emp1.__private_method()  # AttributeError: 'Employee' object has no attribute

#Simple Inheritance example 

# class Parent:
#     def parentFunction(self):
#         print("This is parent function")

# class Child(Parent):
#     def childFunction(self):
#         print("This is child function")

# p=Parent();
# p.parentFunction();

# c = Child();
# c.childFunction();
# c.parentFunction(); 

# 

# class Employee:
#     def __init__(self, id,name, salary):
#         self.id = id
#         self.name = name
#         self.salary = salary

#     def display_employee_details(self):
#         print(f"Employee ID: {self.id}")
#         print(f"Employee Name: {self.name}")
#         print(f"Employee Salary: {self.salary}")

# class Manager(Employee):
#     def __init__(self, id, name, salary, numberOfEmp):
#         super().__init__(id, name, salary)      # passing the value to super class __init__ method to set the value 
#         self.numberOfEmp = numberOfEmp

#     def display_manager_details(self):
#         self.display_employee_details()
#         print(f"Manager Department: {self.numberOfEmp}")

# class Developer(Employee):
#     def __init__(self, id, name, salary, projectName):
#         super().__init__(id, name, salary)      # passing the value to super class __init__ method to set the value 
#         self.projectName=projectName
    
#     def display_developer_details(self):
#         self.display_employee_details()
#         print(f"Working in project as : {self.projectName}")

# mgr = Manager(100,"John",45000,10)
# mgr.display_manager_details();
# print("-----------------")
# dev = Developer(101,"Ajay",34000,"Python");
# dev.display_developer_details();

# class Bike:
#     def speed(self):
#         print("Generic Bike speed is 60km/hr")
# class Honda(Bike):
#     def mailage(self):
#         print("Honda mailage is 80km/lt")
#     def speed(self):
#         print("Honda Bike speed is 55km/hr")
# class Pulsar(Bike):
#     def mailage(self):
#         print("Honda mailage is 80km/lt")
#     def speed(self):
#         print("Pulsar Bike speed is 90km/hr")
# hh=Honda()
# pu=Pulsar()
# hh.speed()
# hh.mailage()
# pu.speed()
# pu.mailage()

from abc import abstractmethod
class Bike:
    # def speed(self):
    #     raise "Sub class need to provide the body"
    @abstractmethod
    def speed(self):
        raise "Sub class need to provide the body"
class Honda(Bike):
    def mailage(self):
        print("Honda mailage is 80km/lt")
    def speed(self):
        print("Honda Bike speed is 55km/hr")
class Pulsar(Bike):
    def mailage(self):
        print("Honda mailage is 80km/lt")
    def speed(self):
        print("Pulsar Bike speed is 90km/hr")
hh=Honda()
pu=Pulsar()
hh.speed()
hh.mailage()
pu.speed()
pu.mailage()