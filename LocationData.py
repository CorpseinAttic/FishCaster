# locationData.py

locations = [
    # Regular Locations
    {
        "name": "Pond",
        "level_required": 0,
        "cost": 0,
        "rarity_boosts": {
            "common": 0.5,
            "uncommon": 0.2,
            "rare": 0.01
        }
    },
    {
        "name": "Lake",
        "level_required": 5,
        "cost": 2_000,
        "rarity_boosts": {
            "common": 0.45,
            "uncommon": 0.25,
            "rare": 0.02
        }
    },
    {
        "name": "River",
        "level_required": 10,
        "cost": 5_000,
        "rarity_boosts": {
            "common": 0.4,
            "uncommon": 0.3,
            "rare": 0.025,
            "epic": 0.002
        }
    },
    {
        "name": "Beach",
        "level_required": 20,
        "cost": 10_000,
        "rarity_boosts": {
            "uncommon": 0.35,
            "rare": 0.035,
            "epic": 0.005
        }
    },
    {
        "name": "Open Sea",
        "level_required": 30,
        "cost": 25_000,
        "rarity_boosts": {
            "rare": 0.045,
            "epic": 0.007,
            "legendary": 0.001
        }
    },

    # Ultra Locations
    {
        "name": "Mystic Falls",
        "level_required": 50,
        "cost": 1_000_000,
        "rarity_boosts": {
            "epic": 0.12,
            "legendary": 0.06,
            "mythical": 0.004,
            "divine": 0.0015,
            "fantasia": 0.0002
        }
    },
    {
        "name": "Enchanted Trench",
        "level_required": 60,
        "cost": 2_500_000,
        "rarity_boosts": {
            "legendary": 0.08,
            "mythical": 0.006,
            "divine": 0.002,
            "fantasia": 0.0006,
            "secrecy": 0.0002
        }
    },
    {
        "name": "Timeworn Grotto",
        "level_required": 75,
        "cost": 5_000_000,
        "rarity_boosts": {
            "mythical": 0.008,
            "divine": 0.003,
            "fantasia": 0.0009,
            "secrecy": 0.0004,
            "extinct": 0.0002
        }
    },
    {
        "name": "Ancient Abyss",
        "level_required": 90,
        "cost": 10_000_000,
        "rarity_boosts": {
            "divine": 0.004,
            "fantasia": 0.0012,
            "secrecy": 0.0006,
            "extinct": 0.0003,
            "old_aged": 0.0002
        }
    },
    {
        "name": "??? Realm",
        "level_required": 100,
        "cost": 25_000_000,
        "rarity_boosts": {
            "fantasia": 0.0015,
            "secrecy": 0.0008,
            "extinct": 0.0004,
            "old_aged": 0.0003,
            "question": 0.0000001
        }
    }
]
