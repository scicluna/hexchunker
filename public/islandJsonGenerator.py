import os
import json

def islandScaffold(folder_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), 'r') as file:
                data = {}
                for line_idx, line in enumerate(file):
                    for idx, char in enumerate(list(line)):
                        data[idx + (10*line_idx)] = {'terrain': char}

                json_filename = os.path.join(output_folder, filename.replace(".txt", ".json"))
                with open(json_filename, 'w') as json_file:
                    json.dump(data, json_file, indent=4)

islandScaffold("./_islands/raw", "./_islands/processed")        
