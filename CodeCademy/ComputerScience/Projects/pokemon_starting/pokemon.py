class Pokemon():
    def __init__(self):

        self.name = ''
        self.level = ''
        self.health = 100
        self.max_health = ''
        self.type = ''
        self.knocked_out = False

    def get_name(self):
        return self.name

    def get_level(self):
        return self.level

    def get_current_health(self):
        return self.health

    def get_type(self):
        return self.type

    def lose_health(self, amount):
        health = self.health - amount
        self.health = health
        print('Pow! You took a hit and lose {1} health. Your current health is: {2}.'.format(amount, health))
        return self.health

    def gain_health(self, amount):
        health = self.health + amount
        self.health = health
        print('Wow! That was an amazing match, you gained {1} health. Your current health is: {2}'.format(amount, health))
        return self.health

    def knock_out(self):
        self.knocked_out = True
        return self.knocked_out

    def revive(self):
        self.knocked_out = False
        return self.knocked_out
        
