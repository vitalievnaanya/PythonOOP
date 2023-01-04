from movie_world.project.mapper import mapper


class DVD:
    def __init__(self, name, id, creation_year, creation_month, age_restriction):
        self.name = name
        self.id = id
        self.creation_year = creation_year
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, id, name, date, age_restriction):
        _, month, year = [int(x) for x in date.split('.')]
        month_name = mapper[month]
        return cls(name, id, month_name, year, age_restriction)

    def __repr__(self):
        status = 'rented' if self.is_rented else 'not rented'
        return f'{self.id}: {self.name} ({self.creation_month} {self.creation_year}) has age restriction' \
               f' {self.age_restriction}. Status: {status}'
