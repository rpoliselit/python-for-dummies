'''
Messed code that exemplifies
Object-Oriented Programming.
'''

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first.strip().title()
        self.last = last.strip().title()
        self.pay = float(pay)

        Employee.num_of_emps += 1

    @property
    def email(self):
        return f'{self.first.lower()}.{self.last.lower()}@company.com'

    @property
    def fullname(self):
        return f'{self.first} {self.last}'

    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print('Deleted name!')
        self.first = None
        self.last = None

    def apply_raise(self):
        self.pay = self.pay * self.raise_amount

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_str(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    def __repr__(self):
        # It changes what is exbited on print(object).
        return f"Employee('{self.first}', '{self.last}', '{self.pay}')"

    def __str__(self):
        return f'{self.fullname} - {self.email}'

    def __add__(self, other):
        # It sums the wages of object.
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname)

class Developer(Employee):
    raise_amount = 1.06

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
#         Employee.__init__(self, first, last, pay)
        self.prog_lang = prog_lang.strip().upper()

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname)
            if isinstance(emp, Developer):
                print('  *', emp.prog_lang)




print(f'AMOUNT OF EMPLOYEES: {Employee.num_of_emps}')

emp1 = Employee('muriola', 'calça ajustada', 5000)
emp2 = Employee('nelmo', 'noone', 6000)
allEmp = [emp1, emp2]


'''Classes and instances'''
print(f'{" CLASSES AND INSTANCES ":*^50}')
print(emp1)
print(emp2)
print()
# print(emp1.fullname
for i in allEmp:
    print(f'FULLNAME: {i.fullname}\nEMAIL: {i.email}\n')


'''Class variables'''
print(f'{" CLASSES VARIABLES ":*^50}')
print(Employee.raise_amount)
emp1.raise_amount = 1.1
for i in allEmp:
    print(f'{i.raise_amount}')
print()
# print(Employee.__dict__)
# print()
# for i in allEmp:
#     print(i.__dict__)
# print()
for c, i in enumerate(allEmp):
    i.apply_raise()
    print(f'EMP{c+1} PAY: {i.pay}')
print(f'AMOUNT OF EMPLOYEES: {Employee.num_of_emps}')
print()


'''Classmethods'''
print(f'{" CLASSMETHODS ":*^50}')
# Employee.set_raise_amt(1.15)
emp1.set_raise_amt(1.15)
print(Employee.raise_amount)
for i in allEmp:
    print(f'{i.raise_amount}')
print()

emp_str_1 = 'Ana-Silva-70000'
new_emp1 = Employee.from_str(emp_str_1)

# print(new_emp1.__dict__)
print(f'AMOUNT OF EMPLOYEES: {Employee.num_of_emps}')
print()


'''Staticmethods'''
print(f'{" STATICMETHODS ":*^50}')
import datetime
myDate = datetime.date(2019, 6, 16)
print(Employee.is_workday(myDate))
myDate = datetime.date(2019, 6, 18)
print(Employee.is_workday(myDate))
print()


'''Inheritance - Creating subclasses'''
print(f'{" SUBCLASSES ":*^50}')
dev_1 = Developer('Joaquim', 'Manuel', 1000, 'python')
print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
# print(dev_1.__dict__)
# print()
mgr_1 = Manager('Catarina', 'von Stein', 10000, [emp1, new_emp1])
# print(mgr_1.__dict__)
print(f'\n{mgr_1.email}')
mgr_1.print_emps()
print(f'\n{mgr_1.email}')
mgr_1.add_employee(dev_1)
mgr_1.remove_employee(new_emp1)
mgr_1.print_emps()
print()
print(issubclass(Manager, Employee))
print(issubclass(Developer, Manager))
print(f'AMOUNT OF EMPLOYEES: {Employee.num_of_emps}')
print()


'''Special (magic/dunder) methods'''
print(f'{" SPECIAL METHODS ":*^50}')
print(f'''{repr(emp1)}
{str(emp1)}

{emp1.__repr__()}
{emp1.__str__()}

{emp1 + dev_1}
{Employee.__add__(emp1, dev_1)}
{emp1.__add__(dev_1)}

{len(emp1)}
''')


'''Property decorators - getters, setters, and deleters'''
print(f'{" PROPERTY DECORATORS ":*^50}')

emp3 = Employee('Jandira', 'Biscoitera', 3000)
print(emp3)
emp3.fullname = 'Valdir Desdentado'
print(emp3.first)
print(emp3.email)
print(emp3.fullname)
del emp3.fullname
