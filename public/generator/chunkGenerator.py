import random
import os
from processes.landMapGenerator import generate_land
from processes.oceanMapGenerator import generate_ocean_with_island

def generate_random_chunks(chunkNo, chunkSize, chunkType):
    directory = "./public/generator/raw/"
    # Clear out the raw folder
    if os.path.exists(directory):
        for file in os.listdir(directory):
            os.remove(os.path.join(directory, file))
    else:
        os.makedirs(directory)

    for i in range(chunkNo):
        chunk = generate_random_chunk(chunkSize, chunkType)
        filename = f"{directory}chunk_{i+1}.txt"
        save_to_file(chunk, filename)
        print(f"Saved chunk_{i+1} to {filename}")
        

def generate_random_chunk(chunkSize, chunkType):
    chunk_ratio = {
       "island": ['ocean', 'ocean', 'ocean', 'ocean', 'ocean', 'ocean', 'ocean', 'land'],
       "flat": ['land', 'land', 'land', 'land', 'land', 'land', 'land'],
       "hilly": [ 'land', 'land', 'land', 'land', 'land', 'land', 'land'],
       "mountainous": ['land', 'land', 'land', 'land', 'land', 'land', 'land']
    }
    selected_chunk = random.choice(chunk_ratio[chunkType])
    if selected_chunk == 'ocean':
        return generate_ocean_with_island(chunkSize, chunkType)
    else:
        return generate_land(chunkSize, chunkType)
    
def save_to_file(map, filename):
    """
    Save the given island map to a file.
    """
    with open(filename, 'w') as f:
        for row in map:
            f.write(''.join(row) + '\n')
        
def main():
    # Get user input
    try:
        print("Choose a biome type:")
        print("1. Island (default)")
        print("2. Flat")
        print("3. Hilly")
        print("4. Mountainous")
        chunkType = input("Enter the number corresponding to your choice: ")
        chunkTypeDict = {
            '1': 'island',
            '2': 'flat',
            '3': 'hilly',
            '4': 'mountainous'
        }
        chunkType = chunkTypeDict.get(chunkType, 'island')
        
        chunkNo = int(input("How many chunks? (default 100): ") or 100)
        chunkSize = int(input("Chunk size? (default 10): ") or 10)

        # Add warnings
        if chunkNo > 100:
            print("Warning: Generating more than 100 chunks may affect performance.")
        if chunkSize > 10:
            print("Warning: A chunk size greater than 10 may affect performance.")

        generate_random_chunks(chunkNo, chunkSize, chunkType)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()