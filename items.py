# Brendon Nguyen, Jack Sparkman
# June 11, 2018

class Item(object):
    """Items are anything that can be picked up or purchased in the game.
    - name : string
    - description : string
    """

    def __init__(self, name, desc = "Generic description."):
        self.name = name
        self.description = desc

    def set_name(self, name):
        self.name = name

    def set_description(self, desc):
        self.description = desc

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

class Resource(Item):
    """Resources are items that you can acquire more than one of, such as
    keys, bombs, and coins.
    - amount : int """

    def __init__(self, name, amt):
        Item.__init__(self, name)
        self.amount = amt

    def set_amount(self, amt):
        self.amount = amt

    def get_amount(self):
        return self.amount

class Consumable(Item):
    """Consumables are items that disappear after one use, such as pills.
    - mods : int list [move, speed, damage, range]
        - example: [0, 0, 2, -1] increases damage by 2 and decreases range by 1.
    """
    def __init__(self, name, mods, uses = 1):
        Item.__init__(self, name)
        self.mods = mods
        self.uses = uses

    def set_modifiers(self, mods):
        self.mods = mods

    def get_modifiers(self):
        return self.mods

class Trinket(Item):
    """Trinkets are items that provide stat modifiers and can be replaced with
    other trinkets picked up."""

    def __init__(self, name):
        Item.__init__(self, name)
        self.modifiers = mods

    def set_modifiers(self, mods):
        self.mods = mods

    def get_modifiers(self):
        return self.mods

keys = Resoruce("key", 0)
bombs = Resource("bomb", 0)
coins = Resource("coin", 0)
trinket1 = Consumable("Consecrated Poop Rag", [3, 3, 3, 3], 2)
