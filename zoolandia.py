class Animal:

    def __init__(self, name, species):
        self.species = species
        self.name = name


class Species:

    def __init__(self):
        self.common_name = ""
        self.geo_region = ""


class Betta(Species):
    def __init__(self, color):
        self.color = color


class Habitat:

    def __init__(self):
        self.name = ""
        self.members = set()


class Walking:

    def __init__(self):
        self.walk_speed = 0
        self.legs = 0


class Swimming:

    def __init__(self):
        self.swim_speed = 0
        self.fins = False
        self.web_feet = False
        self.flippers = False


class Flying:

    def __init__(self):
        self.air_speed = 0
        self.wings = 0

