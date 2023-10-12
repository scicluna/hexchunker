import json
import os
import re  # Import the re module
from processes.randomFeature import random_feature
from processes.randomEncounter import random_encounter

def text_to_json():
    # Set the raw and processed directory
    raw_directory = "./public/generator/raw/"
    processed_directory = "./public/generator/processed/"
    
    # Clear out the processed folder or make it if it doesn't exist
    if os.path.exists(processed_directory):
        for file in os.listdir(processed_directory):
            os.remove(os.path.join(processed_directory, file))
    else:
        os.makedirs(processed_directory)
    
    # List all text files in raw directory
    files = [f for f in os.listdir(raw_directory) if f.endswith(".txt")]
    
    # Process each file
    for x,file in enumerate(files):
        # Extract the number from the filename using regex
        chunk_number = int(re.search(r'(\d+)(?=.txt)', file).group(1))
        
        # Open the file
        with open(raw_directory + file, 'r') as f:
            lines = f.readlines()

            # Determine the width of the chunk
            chunk_width = len(lines[0].strip())
            
            # Process each line to generate the JSON structure
            # and call the random feature and encounter functions
            json_content = []
            for j,line in enumerate(lines):
                for i, char in enumerate(line.strip()):
                    json_content.append({
                        "chunk": chunk_number,
                        "pos": j*chunk_width+i,
                        "terrain": char,
                        "features": random_feature(char),
                        "encounter": random_encounter(char),
                        "history": []
                    })
            
            # Save the JSON to the processed directory
            with open(processed_directory + file.replace(".txt", ".json"), 'w') as json_file:
                json.dump(json_content, json_file, indent=4)
                
        print(f"Processed {file} into JSON format.")

text_to_json()

