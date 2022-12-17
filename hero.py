class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def defend(self, blood):
        if blood >= self.health:
            return f'{self.name} was defeated '
        self.health = self.health - blood

    def heal(self, blood):
        self.health = self.health + blood
        return self.health


hero = Hero("Peter", 100)
print(hero.defend(50))
hero.heal(50)
print(hero.defend(99))
print(hero.defend(1))