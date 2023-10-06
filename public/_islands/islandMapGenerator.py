import noise
import random
import math
import os

def generate_islands(number_of_islands=1, width=10, height=10):
    """
    Generate and save a specified number of island maps.
    """
    directory = "./public/_islands/raw/"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for i in range(number_of_islands):
        island_map = generate_island(width, height)
        filename = f"{directory}island_{i+1}.txt"
        save_to_file(island_map, filename)
        print(f"Saved island_{i+1} to {filename}")

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

def generate_island(width, height):
    """
    Generate an island map based on noise and random placement.
    """
    scale_x, scale_y = 0.3, 0.3
    island_map = [['O' for _ in range(width)] for _ in range(height)]
    center_x, center_y = width / 2, height / 2
    has_town = False

    # Generate basic island shape using Perlin noise
    for y in range(height):
        for x in range(width):
            n = noise.pnoise2(x * scale_x, y * scale_y, octaves=2, persistence=0.5, lacunarity=2.0, repeatx=1024, repeaty=1024, base=42)
            n = (n + 1) / 2.0  # Normalize noise value
            distance_to_center = math.sqrt((x - center_x)**2 + (y - center_y)**2)
            threshold = 0.3 + distance_to_center / width * 0.5
            if n > threshold:
                island_map[y][x] = 'P' if n < 0.5 else ('H' if n < 0.7 else 'M')

    # Add forests
    for y in range(height):
        for x in range(width):
            if island_map[y][x] == 'P' and random.random() < 0.2:
                island_map[y][x] = 'F'

    # Add a town
    while not has_town:
        rand_x, rand_y = random.randint(0, width-1), random.randint(0, height-1)
        if island_map[rand_y][rand_x] in ['P', 'H', 'F', 'M'] and is_adjacent_to_water(rand_x, rand_y, island_map):
            island_map[rand_y][rand_x] = 'T'
            has_town = True

    adjust_border_tiles(island_map, 0.75)
    return island_map

generate_islands(20, 10, 10)
