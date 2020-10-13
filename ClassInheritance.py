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


class Developer(Employee):

    def __init__(self, first_name, last_name, pay, pro_lang):
        super().__init__(first_name, last_name, pay)
        self.pro_lang = pro_lang


class Manager(Employee):
    def __init__(self, first_name, last_name, pay, employees=None):
        super().__init__(first_name, last_name, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print("------>", emp.full_name())


dev1 = Developer("John", "Snow", 50000, "Python")
dev2 = Developer("Kira", "Jones", 40000, "Java")

# print(help(dev1))

print(dev1.pro_lang)
print(dev1.full_name())

mgr_1 = Manager("Sue", "Smith", 80000, [dev1])

mgr_1.add_emp(dev2)
print(mgr_1.full_name())
print(mgr_1.print_emps())

mgr_1.remove_emp(dev1)
print(mgr_1.print_emps())

