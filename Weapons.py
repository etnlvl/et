class Weapons:
    pass


class Laser:
    def __init__(self):
        self.Pc = 0.5          # probability of hit
        self.ammunition = 150  # ammunition remaining
        self.rc = 200          # maximum range

class Gun:
    def __init__(self):
        self.Pc = 0.60
        self.ammunition = 60
        self.rc = 200


class Net:
    def __init__(self):
        self.Pc = 0.85
        self.ammunition = 10
        self.rc = 100


class Jammer:
    def __init__(self):
        self.Pc = 1
        self.ammunition = 80
        self.rc = 60


class Grenade:
    def __init__(self):
        self.Pc = 0.85
        self.ammunition = 80
        self.rc = 60
