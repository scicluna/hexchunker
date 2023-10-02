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

ISLANDNO = 1
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

rules = f"""I want you to generate a map of a fantasy island of size {ISLAND_SIZE}x{ISLAND_SIZE} with 100 total characters using only these keys and nothing else.
O is for ocean, representing every ocean hex. H is for hill, representing every hill hex. 
M is for mountain, representing every mountain hex. F is for forest. P is for plains. T is for town.
Each island should have 0-2 towns.
Build a fantasy island with these characters. Hills and Mountains should bias towards the middle of islands.
Each island must be surrounded by O on each edge.
example: 
OOOOOOOOOO
OOOOOOOOOO
OOOOPPOOOO
OOOPHPOOOO
OOPFFHPOOO
OPPFFHPOOO
OOPHHHPOOO
OOOPPPPOOO
OOOOOOOOOO
OOOOOOOOOO
Each island should be unique.
Give a single entry with no other text
"""
ENCOUNTER_RULES = """
Generate an encounter for each character based on its terrain type (OHMFP).
Each encounter should consist of an adjective followed by a noun, making it typically two words. Ensure the combination makes sense for the terrain type.
All encounters should be unique and certain in their descriptions. Avoid words like "perhaps" or "possible".
Do not include headers or context lines in the output.
Example encounters:
O (Ocean): "Lurking Shark", "Sunken Ship"
H (Hill): "Hidden Treasure", "Rolling Fog"
M (Mountain): "Dragon Lair", "Snowy Peak"
F (Forest): "Enchanted Grove", "Wild Deer"
P (Plains): "Nomadic Tribe", "Stone Circle"
Example output -- For the input terrain string "OFHMP", generated encounters output look like:
O (Ocean): "Lurking Shark"
F (Forest): "Enchanted Grove"
H (Hill): "Hidden Treasure"
M (Mountain): "Dragon Lair"
P (Plains): "Nomadic Tribe"
"""

FEATURE_RULES = """
Generate a feature for each character based on its terrain type (OHMFP).
Features are landmarks or objects.
Each feature should be 2-3 words and should make sense for the terrain type.
All features should be unique and certain in their descriptions. Avoid words like "perhaps" or "possible".
Not every tile needs a feature.
Do not include headers or context lines in the output.
Example features:
O (Ocean): "Coral Reef", "Whirlpool", "Sunken City"
H (Hill): "Burial Mound", "Lookout Point"
M (Mountain): "Hidden Cave", "Sacred Peak"
F (Forest): "Ancient Tree", "Druidic Circle"
P (Plains): "Grassy Field", "Flower Meadow"
Example output -- For the input terrain string "OFHMP", generated features output could look like:
O (Ocean): "Coral Reef"
F (Forest): "Ancient Tree"
H (Hill): "Burial Mound"
M (Mountain): "Hidden Cave"
P (Plains): "Grassy Field"
"""


llm = OpenAI(temperature=.9, openai_api_key=os.getenv('OPENAI_API_KEY'))


def generate_encounters_for_chunk(terrain_chunk):
    prompt = PromptTemplate(
        input_variables=["terrain_chunk", "ENCOUNTER_RULES"],
        template="Here is the terrain chunk: {terrain_chunk}. Now, based on these rules: {ENCOUNTER_RULES}, generate encounters for each character."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(terrain_chunk=terrain_chunk, ENCOUNTER_RULES=ENCOUNTER_RULES)
    return resp.splitlines()

def generate_encounters(terrain_map):
    encounters = []
    for i in range(0, len(terrain_map), 5):  # Breaking the map into chunks of 5
        terrain_chunk = terrain_map[i:i+5]
        chunk_encounters = generate_encounters_for_chunk(terrain_chunk)
        encounters.extend(chunk_encounters)
    return encounters

# Similarly for features:
def generate_features_for_chunk(terrain_chunk):
    prompt = PromptTemplate(
        input_variables=["terrain_chunk", "FEATURE_RULES"],
        template="Here is the terrain chunk: {terrain_chunk}. Now, based on these rules {FEATURE_RULES}: generate one feature for each character."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(terrain_chunk=terrain_chunk, FEATURE_RULES=FEATURE_RULES)
    return resp.splitlines()

def generate_features(terrain_map):
    features = []
    for i in range(0, len(terrain_map), 5):  # Breaking the map into chunks of 5
        terrain_chunk = terrain_map[i:i+5]
        chunk_features = generate_features_for_chunk(terrain_chunk)
        features.extend(chunk_features)
    return features

def generate_serially():
    global island_count
    prompt = PromptTemplate(
        input_variables=["rules"],
        template="Here are the rules: {rules}"
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    for i in range(ISLANDNO):
        terrain_map_str = chain.run(rules=rules)
        print(f"RAW terrain: {terrain_map_str}")
        terrain_map = [char for char in terrain_map_str if char != '\n']  # Splitting on every character and filtering out newlines
       
        while len(terrain_map) < 100:
            terrain_map.append('O')
        terrain_map = terrain_map[:100]

        print(f"PROCESSED TERRAIN, {terrain_map} {len(terrain_map)}")

        features = [feature.split(': ')[-1].strip() for feature in generate_features(terrain_map_str)]
        encounters = [encounter.split(': ')[-1].strip() for encounter in generate_encounters(terrain_map_str)]
        

        while len(features) < len(terrain_map):
            features.append("")
        while len(encounters) < len(terrain_map):
            encounters.append("")


        # Create an array of JSON objects
        hex_data = []
        for j, (terrain, encounter, feature) in enumerate(zip(terrain_map, encounters, features)):
            hex_data.append({
                "pos": j,
                "number": island_count,
                "terrain": terrain,
                "feature": feature,
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
    ocean_map_list = [char for char in ocean_map if char != '\n']  # Convert the multi-line string into a list of characters
    prompt = PromptTemplate(
        input_variables=["ocean_map_list", "ENCOUNTER_RULES"],
        template="Here is the ocean map: {ocean_map_list}. Now, based on these rules: {ENCOUNTER_RULES}, generate encounters for each ocean tile."
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    resp = chain.run(ocean_map_list=ocean_map_list, ENCOUNTER_RULES=ENCOUNTER_RULES)
    return resp.splitlines()  # Assuming each encounter is on a new line

def generate_ocean_serially():
    global ocean_count
    for i in range(round(ISLANDNO*1.5)):
        ocean_map_str = generate_ocean_map()
        ocean_map = [char for char in ocean_map_str if char != '\n']  # Convert the multi-line string into a list of characters
        
        # Adjust the length of ocean_map to always be 100
        while len(ocean_map) < 100:
            ocean_map.append('O')
        ocean_map = ocean_map[:100]
        
        # Create an array of JSON objects
        hex_data = []
        for j, (terrain) in enumerate(zip(ocean_map)):
            hex_data.append({
                "pos": j,
                "number": ocean_count,
                "terrain": terrain,
                "feature": "",  # No features for ocean tiles in this case
                "encounter": ""
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