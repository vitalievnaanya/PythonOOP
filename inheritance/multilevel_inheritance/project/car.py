from multilevel_inheritance.project.vehicle import Vehicle


class Car(Vehicle):

    def drive(self):
        return f'driving...'
