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
class Car:
    def __init__(self, color, price=1000000, model="Base Model"):
        self.color = color
        self.price = price
        self.model = model

    def print_car_details(self):
        print(f"Car model is {self.model}")
        print(f"Car color is {self.color}")
        print(f"Car price is {self.price}")
innova = Car("white", 3000000, "Innova Crysta")
innova.print_car_details()
print("-----")
swift = Car("black", 1500000, "Swift Dzire")
swift.print_car_details()
print("-----")
baleno = Car("blue", 1200000)
baleno.print_car_details()
print("-----")
ertiga = Car("silver")
ertiga.print_car_details()