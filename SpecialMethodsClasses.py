# __init__ is an example of special method. Such kind of methods are also called magical methods.
# double underscore before and after is called dunder and this will be read as dunder init.


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

        Employee.no_of_employees += 1

    # Regular methods: They receive instance by default.
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def apply_raise(self):
        self.pay = self.pay * Employee.raise_amount

    # ambiguous representation of an object and mostly used for debugging, logging and things like that.
    def __repr__(self):
        return f"{self.first_name} {self.last_name} | {self.pay}"

    # readable representation of an object and can be used for display purpose.
    def __str__(self):
        pass

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.full_name())


emp_1 = Employee("Chandler", "Bing", 190000)
emp_2 = Employee("Monica", "Gellar", 150000)
print(repr(emp_1))

# above line can be printed using below code.
print(emp_1.__repr__())

print(emp_1 + emp_2)

print(len(emp_2))


