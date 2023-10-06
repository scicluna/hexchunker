import json
import os

def text_to_json():
    raw_directory = "./public/_islands/raw/"
    processed_directory = "./public/_islands/processed/"
    
    # Ensure the processed directory exists
    if not os.path.exists(processed_directory):
        os.makedirs(processed_directory)
    
    # List all text files in raw directory
    files = [f for f in os.listdir(raw_directory) if f.endswith(".txt")]
    
    for file in files:
        with open(raw_directory + file, 'r') as f:
            lines = f.readlines()
            
            # Process each line to generate the JSON structure
            json_content = []
            for j,line in enumerate(lines):
                for i, char in enumerate(line.strip()):
                    json_content.append({
                        "pos": j*10+i,
                        "terrain": char,
                        "features": "",
                        "encounter": ""
                    })
            
            # Save the JSON to the processed directory
            with open(processed_directory + file.replace(".txt", ".json"), 'w') as json_file:
                json.dump(json_content, json_file, indent=4)
                
        print(f"Processed {file} into JSON format.")

text_to_json()
