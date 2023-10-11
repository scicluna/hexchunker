import random
import re
from lists.encounterCombos import encounters
from lists.encounterCombos import encounter_templates

def random_encounter(char):
    template = random.choice(encounter_templates)
    if char == "O" and random.randint(1, 8) != 8:
        return ""

    # If char is not in the dictionary, default to empty lists.
    cat = encounters.get(char, {key: [] for key in encounters["O"]})

    placeholders = ["entities", "actions", "objects", "hidingplaces", "sounds", "smells", "feelings", "remnants", "vegetation", "obstacles", "quests"]
    for placeholder in placeholders:
        if f"[{placeholder}]" in template and cat[placeholder]:  # Ensuring that the list is not empty.
            template = template.replace(f"[{placeholder}]", random.choice(cat[placeholder]))

    # Convert entire template to lowercase
    template = template.lower()

    # Capitalize the first letter of the entire string and the first letter after any period
    template = re.sub(r'(^|\.\s*)\w', lambda match: match.group(0).upper(), template)
    template = template.replace(',,', ',')

    return template