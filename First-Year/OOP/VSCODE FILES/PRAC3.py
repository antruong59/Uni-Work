class Employees:
    def __init__(self, fname, lname, e_id):
        self.first_name = fname
        self.last_name = lname
        self.employee_id = e_id
        self.base_salary = 0
    
    def set_base_salary(self, b_salary):
        self.base_salary = b_salary
        return self.base_salary
        
class TeachingStaff(Employees):
    def __init__(self, fname, lname, e_id, teach_area, category): 
        super().__init__(fname, lname, e_id)
        self.teaching_area = teach_area
        self.category = category
        self.salary = 0

        if self.category not in range(1, 6):
           self.category = 1
    
    def get_salary(self):
        self.salary = 0.01 * (10 * self.category + 100) * self.base_salary

    def get_staff_info(self):
        self.get_salary()
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmployee ID: {self.employee_id}\nArea of Expertise: {self.teaching_area}\nCategory: {self.category}\nSalary: {self.salary}"

jerry = TeachingStaff('Jerry', 'Smith', 110022123, 'IT', 3)
jerry.set_base_salary(90000)
print(jerry.get_staff_info())

class AdministrativeStaff(Employees):
    def __init__(self, fname, lname, e_id, level):
        super().__init__(fname, lname, e_id)
        self.level = level
        self.salary = 0
        
        if self.level not in range(1, 4):
            self.level = 1

    def get_salary(self):
        self.salary = 0.01 * (15 * self.level + 100) * self.base_salary

    def get_staff_info(self):
        self.get_salary()
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmployee ID: {self.employee_id}\nLevel: {self.level}\nSalary: {self.salary}"

print('\n')
alice = AdministrativeStaff('Alice', 'Brown', 78845389, 3)
alice.set_base_salary(90000)
print(alice.get_staff_info())
