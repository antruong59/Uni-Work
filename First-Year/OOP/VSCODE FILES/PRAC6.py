#
# COMP 1046 OOP
# Practical 6 - Task 1
# 

class Base:
    def printMe(self):
        print("Calling method printMe() in class Base.")

class Left(Base):
    def printMe(self):
        super().printMe()
        print("Calling method printMe() in class Left.")
        

class Right(Base):
    def printMe(self):
        super().printMe()
        print("Calling method printMe() in class Right.")
        

class Sub(Right, Left):
    def printMe(self):
        super().printMe()
        print("Calling method printMe() in class Sub.")
        

print(Sub.mro())
s = Sub()
s.printMe()

class Person:
    def __init__(self, fname, lname, dob):
        self.first_name = fname
        self.last_name = lname
        self.date_of_birth = dob

    def get_details(self):
        return f'Name: {self.first_name} {self.last_name}\nDate of Birth: {self.date_of_birth}'
class Worker:
    def __init__(self, tfn, supernum):
        self.tax_file_number = tfn
        self.super_number = supernum

    def get_info(self):
        return f'TFN: {self.tax_file_number}\nSuper: {self.super_number}'
        
class Employee(Person, Worker):
    def __init__(self, fname, lname, dob, tfn, supernum, e_id, pos):
        Person.__init__(self, fname, lname, dob)
        Worker.__init__(self, tfn, supernum)
        self.employee_id = e_id
        self.position = pos

    def get_details(self):
        print(super().get_details())
        print(f'Employee ID: {self.employee_id}\nPosition: {self.position}')
        print(super().get_info())
        return ''


print()
p = Person('Kim', 'White', '12/08/2020')
print(p.get_details())
print()
w = Worker(4556655, 567)
print(w.get_info())
print()
e = Employee('Kim', 'White', '12/08/2020', 4556655, 567, 1121, 'Developer')
print(e.get_details())

class PhoneBook:
    def __init__(self):
        self.__contacts = {}

    def add_contact(self, name, phone):
        self.__contacts[name] = phone

    def get_phone(self, name):
        return self.__contacts.get(name)
        
pb = PhoneBook()
pb.add_contact('Matt', '231-2341')
pb.add_contact('John', '342-5831')
pb.add_contact('Luke', '523-3997')
pb.add_contact('Mark', '932-9683')
print("John's phone number is", pb.get_phone('John'))
print("Mark's phone number is", pb.get_phone('Mark'))