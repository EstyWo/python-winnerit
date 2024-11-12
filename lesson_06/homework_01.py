class Person:
    def __init__(self, name: str):
        self.name = name

    # מתודה בקלאס האב שמחזירה את השם
    def get_name(self):
        return f"Name from Person class: {self.name}"

class Employee(Person):
    def __init__(self, name: str, salary: int, role: str):
        super().__init__(name)
        self.salary = salary
        self.role = role

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: int):
        if new_salary > 0:
            self.__salary = new_salary
        else:
            raise ValueError("Salary cannot be negative")

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, new_role: str):
        if len(new_role) > 0:
            self.__role = new_role
        else:
            raise ValueError("Role can't be empty")

employee1 = Employee("Ben", 4000, "Manager")
print (employee1.get_name())
print ("Salary: ", employee1.salary)
print ("Role: " , employee1.role)

employee1.salary = 5000
employee1.role = "Release manager"
print (f"\nAfter promotion:")
print (f"New salary: {employee1.salary}")
print (f"New role: {employee1.role}")

try:
    employee1.role = ""
except ValueError as e:
    print (f"\nValidation error: {e}")



