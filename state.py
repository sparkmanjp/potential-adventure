# Brendon Nguyen, Jack Sparkman
# June 11, 2018

import characters

"""
state
- character : Character
    - current_hp
    - max_hp
    - move
    - speed
    - damage
    - range
    - coordinates
- rooms : Room list
    - rooms are revealed as player explores
- current_room : Room
    - enemies : Enemy list
    - items : Item list
- inventory : Item dictionary
    - keys : Item
    - bombs : Item
    - coins : Item
    - trinket : Item
    - spacebar_item : Item
    - consumable : Item
- game_over : bool
    - final boss hp = 0 or current hp = 0
    - final boss hp = 0 and current hp != 0
"""

class State(object):
    """A State object represents all the information in a single gamestate."""
    def __init__(self,
                character = characters.Isaac,
                rooms = [],
                current_room,
                ):
