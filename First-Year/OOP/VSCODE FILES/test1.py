# class StartPlaying:
#     def __init__(self):
#         self.start = ''
#         self.name = ''
#         self.again = ''

#     def start_game(self):
#         self.start = input('Do you wanna play? (y/n)')
#         while self.start not in ['y', 'n']:
#             print('It must be y or n. Please try again')
#             self.start = input('Do you wanna play? (y/n)')
#         if self.start == 'y':
#             print('Yay, let\'s get started!')
#             self.name = input('What\'s your name?')
#             print('Your name is', self.get_name())
#             print('Gud name tho :3')
#             self.play_again()
#         else:
#             print('Maybe next time')

#     def get_name(self):
#         return self.name

#     def play_again(self):
#         self.again = input('Again? (y/n)')
#         if self.again == 'y':
#             print('Haha')
#         else:
#             print('Okay, bye then')
    
    

    

# player1 = StartPlaying()
# player1.start_game()


# # WEEK 4
# # Overide method example
# class Insect:
#     def move(self):
#         print('I\'m crawling')

# class Bee(Insect):
#     def move(self):
#         print('I\'m flying')

# class Grasshopper(Insect):
#     def move(self):
#         print('I\'m jumping')

# insect = [Insect(), Bee(), Bee(), Grasshopper()]
# for x in insect:
#     x.move()


class Animal:
    def __init__(self, species):
        self.__species = species

    def get_species(self):
        return self.__species

    species = property(get_species)

    def makeSound(self):
        print('Grrrrrrr')

class Dog(Animal):
    def __init__(self):
        super().__init__('Dog')

    def makeSound(self):
        super().makeSound()
        Cat().makeSound()
        print('Woof Woof')
    
    '''def makeSound(self):
        print('Woof Woof')'''

class Cat(Animal):
    def __init__(self):
        super().__init__('Cat')

    def makeSound(self):
        super().makeSound()
        print('Meow Meow')

    '''def makeSound(self):
        print('Meow Meow')'''

def describe(animal):
    print(animal.get_species())
    animal.makeSound()

animal = [Animal('Animal'), Dog(), Cat()]
for x in animal:
    describe(x)

# # abc abstract base class will not be initalised, just play as a template for its subclasses
# # from module import className, methodName
# # check isinstance() for more specific parent class and its subclasses

# from abc import ABC, abstractmethod
# class Operator(ABC):
#     @abstractmethod
#     def calculate(self, a, b):
#         pass
    
#     @abstractmethod
#     def get_symbol(self):
#         pass

# class Calculator:
#     def __init__(self):
#         self.operators = []

#     def register(self, op):
#         self.operators.append(op)

#     def calculate(self):
#         a = float(input('a: '))
#         op = input('op: ')
#         b = float(input('b: '))

#         for x in self.operators:
#             if x.get_symbol() == op:
#                 print(a, x.get_symbol(), b, '=', x.calculate(a, b))

# class Addition(Operator):
#     def calculate(self, a, b):
#         return a + b
    
#     def get_symbol(self):
#         return '+'

# add = Calculator()
# add.register(Addition())
# add.calculate()

# # cls => used in class method
# class Contact:
#     all_contacts = []

#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#         Contact.all_contacts.append(self)

#     @classmethod
#     def pritnt_contact(cls):

# print(type(input('sfds')))

class Play:
    command = ['a', 's', 'd', 'w']
    def __init__(self):
        self.__user = input('Please enter either a, s, d, w:')
        while self.__user not in Play.command:
            print('Please enter again')
            self.__user = input('Please enter either a, s, d, w:')
        
        print('Yay, u did it!')

x = Play()
            
        
