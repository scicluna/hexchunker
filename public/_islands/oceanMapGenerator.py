import noise
import random
import math
import os

def save_to_file(island_map, filename):
    """
    Save the given island map to a file.
    """
    with open(filename, 'w') as f:
        for row in island_map:
            f.write(''.join(row) + '\n')

def adjust_border_tiles(island_map, chance_to_transform=0.75):
    """
    Adjust the border tiles of the island based on a given chance.
    """
    height, width = len(island_map), len(island_map[0])
    
    for y in range(height):
        for x in range(width):
            if x in [0, width-1] or y in [0, height-1]:
                if random.random() < chance_to_transform and island_map[y][x] != 'O':
                    island_map[y][x] = 'O'

def is_adjacent_to_water(x, y, island_map):
    """
    Check if a tile is adjacent to a water tile.
    """
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < len(island_map[0]) and 0 <= new_y < len(island_map):
            if island_map[new_y][new_x] == 'O':
                return True
    return False

def generate_open_ocean_with_islands(number_of_maps=1, width=10, height=10):
    """
    Generate and save a specified number of open ocean maps with occasional islands.
    """
    directory = "./public/_islands/raw/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_maps):
        ocean_map = generate_ocean_with_island(width, height)
        filename = f"{directory}ocean_{i+1}.txt"
        save_to_file(ocean_map, filename)
        print(f"Saved ocean_with_island_{i+1} to {filename}")

def generate_ocean_with_island(width, height):
    """
    Generate a mostly open ocean map with occasional islands.
    """
    scale_x, scale_y = 0.15, 0.15
    ocean_map = [['O' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width / 2, height / 2
    has_town = False

    # Generate open ocean with occasional islands using Perlin noise
    base_value = random.randint(0, 10000)
    for y in range(height):
        for x in range(width):
            n = noise.pnoise2(x * scale_x, y * scale_y, octaves=2, persistence=0.5, lacunarity=2.0, repeatx=1024, repeaty=1024, base=base_value)
            n = (n + 1) / 2.0  # Normalize noise value
            distance_to_center = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            threshold = 0.6 + distance_to_center / width * 0.2  # Higher threshold biased towards ocean
            if n > threshold:
                ocean_map[y][x] = 'M' if n < 0.7 else ('H' if n < 0.9 else 'P')

    # Add forests
    for y in range(height):
        for x in range(width):
            if ocean_map[y][x] == 'P' and random.random() < 0.2:
                ocean_map[y][x] = 'F'

    # Add a town (only if there are islands)
    max_attempts = 100
    attempts = 0

    # Add a town (only if there are islands)
    while not has_town and attempts < max_attempts:
        rand_x, rand_y = random.randint(0, width-1), random.randint(0, height-1)
        if ocean_map[rand_y][rand_x] in ['P'] and is_adjacent_to_water(rand_x, rand_y, ocean_map):
            ocean_map[rand_y][rand_x] = 'T'
            has_town = True
        attempts += 1

    # If after max_attempts we still don't have a town, print a message (or handle it in another way if needed)
    if not has_town:
        print("Could not find a suitable location for a town.")

    adjust_border_tiles(ocean_map, 0.95)  # Higher chance to convert border tiles to ocean
    return ocean_map

generate_open_ocean_with_islands(100, 10, 10)
