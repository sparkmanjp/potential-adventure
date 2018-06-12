
class Character(object):
    """Stats for playable characters """
    def __init__(self, current_hp = 3,
                       max_hp = 3,
                       move = 1, # multiplier, 1 as default
                       tps = 2.67, # shots per second
                       damage = 2, # damage per shot
                       range = 6): # tiles traveled
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.move_speed = move_speed
        self.tps = tps
        self.damage = damage
        self.range = range
