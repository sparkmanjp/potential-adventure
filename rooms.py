class Room(object):
    """description of rooms"""
    def __init__(self,
                 name,
                 exits = [],
                 enemies = [],
                 trinkets = [],
                 consumables = [],
                 resources = [],
                 cool_items = []): # tiles traveled
        self.name = name
        self.exits = exits
        self.enemies = enemies
        self.trinkets = trinkets
        self.consumables = consumables
        self.resources = resources
        self.cool_items = cool_items


StartingRoom = Room('StartingRoom')
