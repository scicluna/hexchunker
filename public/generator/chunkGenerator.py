import random
import os
from processes.islandMapGenerator import generate_island
from processes.oceanMapGenerator import generate_ocean_with_island

def generate_random_chunks(chunkNo):
    directory = "./public/generator/raw/"
    # Clear out the raw folder
    if os.path.exists(directory):
        for file in os.listdir(directory):
            os.remove(os.path.join(directory, file))
    else:
        os.makedirs(directory)

    for i in range(chunkNo):
        chunk = generate_random_chunk(20)
        filename = f"{directory}chunk_{i+1}.txt"
        save_to_file(chunk, filename)
        print(f"Saved chunk_{i+1} to {filename}")
        

def generate_random_chunk(chunkSize=10):
    chunk_type = ['ocean', 'ocean', 'ocean', 'ocean', 'ocean', 'ocean', 'island']
    selected_chunk = random.choice(chunk_type)
    if selected_chunk == 'ocean':
        return generate_ocean_with_island(chunkSize,chunkSize)
    else:
        return generate_island(chunkSize,chunkSize)
    
def save_to_file(map, filename):
    """
    Save the given island map to a file.
    """
    with open(filename, 'w') as f:
        for row in map:
            f.write(''.join(row) + '\n')
        
generate_random_chunks(20)