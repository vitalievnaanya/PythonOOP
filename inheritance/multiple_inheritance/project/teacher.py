from multiple_inheritance.project.employee import Employee
from multiple_inheritance.project.person import Person


class Teacher(Person, Employee):

    def teach(self):
        return f'teaching...'
