import datetime


class Employee:

    # Class variable
    raise_amount = 1.04
    no_of_employees = 0

    def __init__(self, first_name, last_name, pay):
        # instance specific variables
        self.first_name = first_name
        self.last_name = last_name
        self.pay = pay
        self.email = first_name + '.' + last_name + '@company.com'

        Employee.no_of_employees +=1

    # Regular methods: They receive instance by default.
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount

    # Class methods: They receive class as a parameter by default.

    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount

    # Class method can be used as an alternative constructor
    @classmethod
    def get_employee(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    # Static Methods: When function does not use instance or class to perform the action
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


emp1 = Employee("John", "Cna", 500000)
emp2 = Employee("Jill", "Jacob", 900000)

# If we write like this: emp1.new_function() we by default pass emp1 instance to the new_function method.
# So self should be passed in the method.

print(emp1.full_name())

# Another way of writing the above statement using class name.
print(Employee.full_name(emp2))

# Class variables demo
print("Employees pay before raise: " + str(emp1.pay))
emp1.apply_raise()
print("Employees pay after raise: " + str(emp1.pay))

print(emp1.__dict__)
emp1.raise_amount = 1.05

print(emp1.__dict__)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)
print(Employee.no_of_employees)

# Calling class method
Employee.set_raise_amount(1.02)
print(Employee.raise_amount)

emp_str_1 = "Marlyn-Mounroy-980000"

new_emp1 = Employee.get_employee(emp_str_1)

print(new_emp1.full_name())

my_date = datetime.date(2020, 10, 13)
print(my_date)
print("Weekday : " + str(Employee.is_work_day(my_date)))

