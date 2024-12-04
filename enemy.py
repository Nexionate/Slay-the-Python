"""
Ethan O'Connor
A01435041
Set E
"""

enemies_easy = (
    {"name": "mugger", "current HP": 36, "max HP": 36, "current block": 0, "attack pattern": False,
     "attack": [{"damage": 7, "block": 0}, {"damage": 11, "block": 0}, {"damage": 5, "block": 7},
                {"damage": 0, "block": 8}]},
    {"name": "slime", "current HP": 21, "max HP": 21, "current block": 0, "attack pattern": False,
     "attack": [{"damage": 4, "block": 0}, {"damage": 6, "block": 6}, {"damage": 5, "block": 0}]},
    {"name": "fat gremlin", "current HP": 25, "max HP": 25, "current block": 8, "attack pattern": False,
     "attack": [{"damage": 6, "block": 0}, {"damage": 6, "block": 0}, {"damage": 0, "block": 8},
                {"damage": 4, "block": 6}]},

)
enemies_hard = (
    {"name": "gremlin nob", "current HP": 53, "max HP": 53, "current block": 0, "attack pattern": True,
     "attack": [{"damage": 0, "block": 0}, {"damage": 8, "block": 0}, {"damage": 16, "block": 0},
                {"damage": 20, "block": 0}, {"damage": 20, "block": 0}, {"damage": 20, "block": 0}]},
    {"name": "ogre", "current HP": 44, "max HP": 44, "current block": 0, "attack pattern": True,
     "attack": [{"damage": 15, "block": 0}, {"damage": 15, "block": 0}, {"damage": 0, "block": 5},
                {"damage": 15, "block": 0}, {"damage": 15, "block": 0}, {"damage": 0, "block": 5}]},
)

# maybe make tuple -> breaks code, don't bother with time constraints
boss_attacks = [{"damage": 8, "block": 0},
                {"damage": 6, "block": 0, "debuff": 2},
                {"damage": 12, "block": 0},
                {"damage": 6, "block": 12},
                {"damage": 12, "block": 0},
                {"damage": 6, "block": 0, "debuff": 2}]
enemies_boss = (
    {"name": "hexaghost", "current HP": 115, "max HP": 115, "current block": 0, "attack pattern": True, "attack":
        [{"damage": 0, "block": 0}] + (boss_attacks * 5)})
