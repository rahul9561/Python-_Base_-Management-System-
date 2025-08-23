class Employee:
    def __init__(self, name, age, department, salary):
        self.name = name
        self.age = age
        self.department = department
        self.salary = salary

    def to_tuple(self):
        return (self.name, self.age, self.department, self.salary)
