# Brendon Nguyen, Jack Sparkman
# June 11, 2018

class Enemy(object):
    """Stats for enemy characters"""
    def __init__(self, name = "Default Enemy",
                       current_hp = 3,
                       move_speed= 1, # multiplier, 1 as default
                       tps = 2.67, # shots per second
                       damage = 2, # damage per shot
                       range = 6,
                       aggressive = True): # tiles traveled)
        self.name = name
        self.current_hp = current_hp
        self.move_speed = move_speed
        self.tps = tps
        self.damage = damage
        self.range = range
        self.aggressive = aggressive

Slime = Enemy("Slime")
