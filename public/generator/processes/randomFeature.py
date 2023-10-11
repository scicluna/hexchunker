import random
from lists.featureCombos import features

def random_feature(char):
    terrain_map = {
        "O": "Ocean",
        "P": "Plains",
        "H": "Hills",
        "M": "Mountains",
        "F": "Forest",
        "T": "Town"
    }

    terrain = terrain_map.get(char)

    if terrain:
        if terrain == "Town":
            return random.choice(features[terrain]["name"])
        
        if terrain == "Ocean":
            rng = random.randint(1, 10)
            if rng != 10:
                return ""
        
        return f"{random.choice(features[terrain]['adjectives'])} {random.choice(features[terrain]['nouns'])}"

    return ""