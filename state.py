# Brendon Nguyen, Jack Sparkman
# June 11, 2018

"""
state
- character : Character
    - current hp
    - max hp
    - mutable attributes
- rooms : Room list
    - rooms are revealed as player explores
- current_room : Room
- enemies_in_room : Enemy list
- items_in_room : Item list
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
