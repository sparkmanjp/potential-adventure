# Brendon Nguyen, Jack Sparkman
# June 11, 2018

class Item(object):
    """Items are anything that can be picked up or purchased in the game.
    - name : string
    - category : "consumable", "resource", "spacebar", or "trinket"
    -
    """
    def __init__(self, name):
        self.name = name 

class Resource(Item):
    """Resources are items that you can acquire more than one of, such as
    keys, bombs, and coins."""
    def __init__(self, name, amt):
        Item.__init__(self, name)
        self.amount = amt

class Consumable(Item):
    """Consumables are items that disappear after one use, such as pills.
    - modifiers : int list [move, speed, damage, range]
        - example: [0, 0, 2, -1] increases damage by 2 and decreases range by 1.
    """
    def __init__(self, name, mods):
        Item.__init__(self, name)
        self.modifiers = mods

class Trinket(Item):
    """Trinkets are items that provide stat modifiers and can be replaced with
    other trinkets picked up."""
    def __init__(self, name):
        Item.__init__(self, name)
        self.modifiers = mods
