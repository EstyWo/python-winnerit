class Person:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return f"Name from Person class: {self._name}"

class Student(Person):
    def __init__(self, name, student_id):
        self._name = name
