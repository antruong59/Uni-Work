#
# COMP 1046 OOP
# Workshop 7
#

# Multiple exceptions occur at once

# class B(Exception):
#     pass

# class C(B):
#     pass

# class D(C):
#     pass

# for cls in [B, C, D]:
#     try:
#         raise cls()
#     except D:
#         print("D")
#     except C:
#         print("C")
#     except B:
#         print("B")

# class Error(Exception):
#   def __init__(self, par, message = 'Message'):
#     self.par = par
#     self.message = message
#     super().__init__(self.message)


class InvalidCategoryError(Exception):
  pass

class InvalidLevelError(Exception):
  pass

class Employee:
  def __init__(self, first_name, last_name, employee_id):
    self.first_name = first_name
    self.last_name = last_name
    self.employee_id = employee_id
    self.base_salary = 0
  
  def set_base_salary(self, salary):
    self.base_salary = salary   

class TeachingStaff (Employee):
  def __init__(self, first_name, last_name, employee_id, teaching_area, category):
    super().__init__(first_name, last_name, employee_id)
    self.teaching_area = teaching_area

    # category is not int --> raise TypeError

    try: 
      if category>=1 and category<=5:
        self.category = category
      else:
        self.category = 0
        raise InvalidCategoryError('The category of a teaching staff must be between 1 and 5.')

    except TypeError:
      print('TypeError: the category attribute must contain a number.')
    
  def get_salary(self):

    # category is not int --> raise TypeError
    # base_salary is not either int or float --> raise TypeError

    try: 
      salary = (((self.category * 10) + 100)/100) * self.base_salary
      return salary

    except TypeError:
      print('TypeError: the category attribute must contain a number.')

    

  def get_staff_info(self):

    # first_name is not a str --> raise TypeError
    # last_name is not a str --> raise TypeError
    # teaching_area is not a str --> raise TypeError

    try:
      return 'First name: ' + self.first_name + \
      '\nLast name: ' + self.last_name + \
      '\nEmployee ID: ' + str(self.employee_id) + \
      '\nArea of Expertise: ' + self.teaching_area + \
      '\nCategory: ' + str(self.category) + \
      '\nSalary: ' + str(self.get_salary())
    
    except TypeError:
      print('Type Error: One of the TeachingStaff attributes are not a string.')
    

class AdministrativeStaff(Employee):
  def __init__(self, first_name, last_name, employee_id, level):
    super().__init__(first_name, last_name, employee_id)
    
    # level is not int --> raise TypeError
    try:
      if level>=1 and level<=3:
        self.level = level
      else:
        self.level = 0
        raise InvalidLevelError('The level of an administrative staff must be between 1 and 3.')

    except TypeError:
      print('TypeError: the level must be an integer.')

  def get_salary(self):

    # level is not int --> raise TypeError

    try:
      salary = (((self.level * 15) + 100)/100) * self.base_salary
      return salary
    
    except TypeError:
      print('TypeError: the level muat be an integer.')

    

  def get_staff_info(self):

    # first_name is not a str --> raise TypeError
    # last_name is not a str --> raise TypeError

    try: 
      return 'First name: ' + self.first_name + \
      '\nLast name: ' + self.last_name + \
      '\nEmployee ID: ' + str(self.employee_id) + \
      '\nLevel: ' + str(self.level) + \
      '\nSalary: ' + str(self.get_salary())
    
    except TypeError:
      print('Type Error: One of the AdministrativeStaff attributes are not a string.')
    

t = TeachingStaff(1,2,3,"4","5")
print(t.get_staff_info())
print("This message must appear on your screen.")
e = AdministrativeStaff(1,2,3,2)
print(e.get_staff_info())
print("This message must appear if exceptions are all handled correctly.")

t = TeachingStaff("John", "Smith", 45678, "Software Engineering",7)
print("This line should not be printed on the screen.")

# e = AdministrativeStaff("Sarah", "Smith", 123, 8)
# print("This line should also not be printed on the screen.")