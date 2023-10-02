##Spam out infinity islands/oceans with chatgpt
import os
import json
from dotenv import load_dotenv
load_dotenv()

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

island_count = 0
ocean_count = 0

ISLANDNO = 2
OCEAN_SIZE = 10
ISLAND_SIZE = 10

def get_latest_file_number(directory, prefix):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f)) and f.startswith(prefix)]
    if not files:
        return 0
    numbers = [int(f.replace(prefix, '').replace('.json', '')) for f in files]
    return max(numbers)

def initialize_counts():
    if not os.path.exists('processed'):
        os.makedirs('processed')

    global island_count, ocean_count
    processed_dir = "processed"
    island_count = get_latest_file_number(processed_dir, "island") + 1
    ocean_count = get_latest_file_number(processed_dir, "ocean") + 1

rules = f"""I want you to generate a map of a fantasy island of size {ISLAND_SIZE}x{ISLAND_SIZE} using only these keys and nothing else.
O is for ocean, representing every ocean hex. H is for hill, representing every hill hex. 
M is for mountain, representing every mountain hex. F is for forest. P is for plains.. 
Now using these characters in sequential order, build out a fantasy continent with realistic proportions
Each island should be unique.
Give a single entry with no other text
"""
ENCOUNTER_RULES = """
For each character in the provided map, generate an encounter based on its terrain type:
BE precise. do not say "perhaps" or "possible" or anything like that. say everything with certainty.
- O (Ocean): Possible encounters include sea monsters, shipwrecks, or mysterious floating objects.
- H (Hill): Possible encounters include bandit camps, hidden treasures, or wandering merchants.
- M (Mountain): Possible encounters include dragon lairs, ancient ruins, or mountain hermits.
- F (Forest): Possible encounters include wild animals, hidden groves, or enchanted clearings.
- P (Plains): Possible encounters include nomadic tribes, lost travelers, or mysterious stone circles.

Provide a unique encounter or feature for each hex tile.
"""

FEATURE_RULES = """
For each character in the provided map, generate a feature based on its terrain type:
BE precise. do not say "perhaps" or "possible" or anything like that. say everything with certainty.
- O (Ocean): Possible features include coral reefs, whirlpools, or sunken cities.
- H (Hill): Possible features include ancient burial mounds, lookout points with scenic views, or mysterious stone formations.
- M (Mountain): Possible features include hidden caves, mineral-rich mines, or sacred mountain peaks.
- F (Forest): Possible features include ancient trees, druidic circles, or hidden waterfalls.
- P (Plains): Possible features include port-towns(each map should have 0-2) These towns must be adjacent to water.

Not every tile needs a feature; some can be left without any notable landmarks.
"""

llm = OpenAI(temperature=.9, openai_api_key=os.getenv('OPENAI_API_KEY'))


def generate_features(terrain_map):
    prompt = PromptTemplate(
        input_variables=["terrain_map", "FEATURE_RULES"],
        template="Here is the terrain map: {terrain_map}. Now, based on these rules {FEATURE_RULES}: generate one feature for each character."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(terrain_map=terrain_map, FEATURE_RULES=FEATURE_RULES)
    return resp.splitlines()

def generate_encounters(terrain_map, features):
    prompt = PromptTemplate(
        input_variables=["terrain_map", "features", "ENCOUNTER_RULES"],
        template="Here is the terrain map: {terrain_map}. Now, based on these rules: {ENCOUNTER_RULES}, and these features: {features} generate encounters for each character."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(terrain_map=terrain_map, features=features, ENCOUNTER_RULES=ENCOUNTER_RULES)
    return resp.splitlines()  # Assuming each encounter/feature is on a new line

def generate_serially():
    global island_count
    prompt = PromptTemplate(
        input_variables=["rules"],
        template="Here are the rules: {rules}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    for i in range(ISLANDNO):
        terrain_map = chain.run(rules=rules)
        features = generate_features(terrain_map)
        encounters = generate_encounters(terrain_map, features)
        
        # Create an array of JSON objects
        hex_data = []
        for j, (terrain, encounter, feature) in enumerate(zip(terrain_map, encounters, features)):
            hex_data.append({
                "number": island_count,
                "terrain": terrain,
                "feature": feature,  # You can modify this to generate features if needed
                "encounter": encounter
            })
            
        # Save the JSON data to a file
        with open(f'processed/island{island_count}.json', 'w') as file:
            json.dump(hex_data, file, indent=4)
            island_count += 1

def generate_ocean_map():
    return """
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO
OOOOOOOOOO    
"""

def generate_ocean_encounters(ocean_map):
    ocean_map_lines = ocean_map.strip().split("\n")  # Split the multi-line string into individual lines
    prompt = PromptTemplate(
        input_variables=["ocean_map_lines", "ENCOUNTER_RULES"],
        template="Here is the ocean map: {ocean_map_lines}. Now, based on these rules: {ENCOUNTER_RULES}, generate encounters for each ocean tile."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(ocean_map_lines=ocean_map_lines, ENCOUNTER_RULES=ENCOUNTER_RULES)
    return resp.splitlines()  # Assuming each encounter is on a new line

def generate_ocean_serially():
    global ocean_count
    for i in range(ISLANDNO):
        ocean_map = generate_ocean_map()
        encounters = generate_ocean_encounters(ocean_map)
        
        # Create an array of JSON objects
        hex_data = []
        for j, (terrain, encounter) in enumerate(zip(ocean_map, encounters)):
            hex_data.append({
                "number": ocean_count,
                "terrain": terrain,
                "feature": "",  # No features for ocean tiles in this case
                "encounter": encounter
            })
        
        # Save the JSON data to a file
        with open(f'processed/ocean{ocean_count}.json', 'w') as file:
            json.dump(hex_data, file, indent=4)
            ocean_count += 1

def start():
    initialize_counts()
    generate_serially()
    generate_ocean_serially()
    
start()