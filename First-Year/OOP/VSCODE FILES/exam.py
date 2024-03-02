class PowerOfTenIterable:
    def __iter__(self):
        return PowerOfTenIterator()

class PowerOfTenIterator:
    def __init__(self):
        self.num = 1
        self.index = 0

    def __next__(self):
        if self.index > 9:
            raise StopIteration()

        else:
            num = self.num * (10 ** self.index)
            self.index += 1
            return num

for x in PowerOfTenIterable():
    print(x)


# class Car:
#     def __init__(self):
#         self.__speed = 0

#     def increase_speed(self, amount):
#         self.__speed += amount

#     def get_speed(self):
#         return self.__speed

# class PetrolCar(Car):
#     def __init__(self):
#         super().__init__()

#     def accelerate(self):
#         self.increase_speed(20)

# class ElectricCar(Car):
#     def __init__(self):
#         super().__init__()

#     def accelerate(self):
#         self.increase_speed(10)

# class HybridCar(PetrolCar, ElectricCar):
#     def __init__(self, mode = 'electric'):
#         self.mode = mode
#         PetrolCar.__init__(self)
#         ElectricCar.__init__(self)

#     def accelerate(self):
#         if self.mode == 'electric':
#             ElectricCar.accelerate(self)

#         else:
#             PetrolCar.accelerate(self)

# h = HybridCar()
# h.accelerate()
# print(h.get_speed())
# h.mode = "petrol"
# h.accelerate()
# print(h.get_speed())

# class Vehicle:
#     def __init__(self, name, doors):
#         self.name = name
#         self.__doors = doors

#     def get_doors(self):
#         return self.__doors

# class Truck(Vehicle):
#     def __init__(self, name, doors, drive, maxload):
#         super().__init__(name, doors)
#         self.drive = drive
#         self.__maxload = maxload

#     def get_description(self):
#         return f'{self.name} is {self.drive} and has {self.get_doors()} doors and max load of {self.__maxload} kgs.'
        


# t = Truck("Ute", 2, "4WD", 970)
# print(t.get_description())



# class User:
#     def __init__(self, user_id, pw, login = False):
#         self.__user_id = user_id
#         self.__password = pw
#         self.__logged_in = login

#     def login(self, password):
#         if self.__password == password:
#             self.__logged_in = True

#     def logout(self):
#         self.__logged_in = False

#     def is_logged_in(self):
#         return self.__logged_in

# class Customer(User):
#     def __init__(self, user_id, pw):
#         super().__init__(user_id, pw)
#         self.__balance = 0
#         self.__orders = []

#     def get_balance(self):
#         if self.is_logged_in():
#             return self.__balance
#         print('Cannot access balance. Not logged in.')
#         return 0

#     def pay(self, amount):
#         if self.is_logged_in():
#             self.__balance -= amount
#         else:
#             print('Cannot pay. Not logged in.')

#     def order(self, products):
#         if self.is_logged_in():
#             order = Order(products)
#             self.__orders.append(order)
#             self.__balance += order.get_total()
#         else:
#             print("Cannot order. Not logged in.")

# class Order:
#     def __init__(self, products):
#         self.__products = products
        
#     def get_total(self):
#         total = 0
#         for x in self.__products:
#             total += x.price
#         return total

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# num = 5
# if num %2 != 0:

#   raise ValueError('not the right type')

# print(num)


