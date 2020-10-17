class Employee:

    def __init__(self, first_name, last_name):
        # instance specific variables
        self.first_name = first_name
        self.last_name = last_name

    # def fullname(self):
    #   return f"{self.first_name} {self.last_name}"

    # Below is the example of getter property.
    @property
    def email(self):
        return f"{self.first_name}.{self.last_name}@company.com "

    @property
    def fullname(self):
        return f"{self.first_name} {self.last_name}"

    # Below is the example of setter property
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

    @fullname.deleter
    def fullname(self):
        print("Deleting fullname")
        self.first_name = None
        self.last_name = None


emp_1 = Employee("John", "Ceena")

print(emp_1.email)
print(emp_1.fullname)

emp_1.fullname = "Chandler Bing"
print(emp_1.fullname)

del emp_1.fullname

